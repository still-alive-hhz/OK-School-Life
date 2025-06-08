import webview
from flask import Flask, jsonify, request, render_template, send_file
import random, os, json, sys, threading, webbrowser

if getattr(sys, 'frozen', False):
    # PyInstaller环境
    base_dir = sys._MEIPASS
    template_folder = os.path.join(base_dir, 'assets', 'templates')
    static_folder = os.path.join(base_dir, 'assets', 'static')
else:
    # 普通环境
    base_dir = os.path.dirname(__file__)
    template_folder = os.path.abspath(os.path.join(base_dir, '../assets/templates'))
    static_folder = os.path.abspath(os.path.join(base_dir, '../assets/static'))

# 初始化Flask应用
app = Flask(
    __name__,
    template_folder=template_folder
    # 不要设置 static_folder
)

# 动态获取路径
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
    json_path = os.path.join(base_dir, "assets/data/events.json")
else:
    json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/data/events.json"))

# 加载 JSON 文件
try:
    with open(json_path, "r", encoding="utf-8") as f:
        event_data = json.load(f)
except FileNotFoundError:
    print(f"Error: events.json 文件未找到！尝试路径：{json_path}")
    event_data = {}
except json.JSONDecodeError as e:
    print(f"Error: 无法解析 JSON 文件: {e}")
    event_data = {}

# 兼容新旧结构
def get_event_list():
    # 只取 metadata.start_options
    meta = event_data.get("metadata", {})
    return meta.get("start_options", [])

def get_group_events(group_key):
    # 只取 events.fixed_events.group_x
    events = event_data.get("events", {})
    fixed = events.get("fixed_events", {})
    return fixed.get(group_key, [])

def get_random_events():
    # 只取 events.random_events
    events = event_data.get("events", {})
    return events.get("random_events", [])

event_list = get_event_list()
event_1_list = get_group_events("group_1")
event_2_list = get_group_events("group_2")
event_3_list = get_group_events("group_3")
random_events = get_random_events()

# 让版本号作为变量方便调用，而不用手动修改
version = "v0.4.0"

user_state = {
    "school": None,
    "event_idx": 0,
    "stage": "fixed",
    "random_used": set()
}

achievements = []
used_event_indices = []
current_event = None
current_choices = {}
score = int(0)

def get_contributor_str(event):
    if "contributors" in event and event["contributors"]:
        return "（由" + "、".join(event["contributors"]) + "贡献）"
    return ""

def pick_result(result_value):
    """
    支持三种格式：
    1. 字符串：直接返回
    2. 概率数组：如 [{"rd_result": "...", "prob": 0.6}, ...]
    3. 兼容老格式 [{"text": "...", "prob": 0.5}]
    返回：(文本, 是否gameover)
    """
    if isinstance(result_value, list):
        probs = [item.get("prob") or item.get("prob", 1/len(result_value)) for item in result_value]
        chosen = random.choices(result_value, weights=probs, k=1)[0]
        text = chosen.get("rd_result") or chosen.get("text") or ""
        end_game = chosen.get("end_game", False)
        return text, end_game
    else:
        return result_value, False

# 创建 Flask API 路由
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/start_game', methods=['GET'])
def api_start_game():
    return jsonify({
        'message': f"欢迎来到OK School Life beta {version}！\n你将经历不同的事件和选择，看看你的学校生活会如何发展。",
        'options': [
            {'key': '1', 'text': '开始游戏'},
            {'key': '2', 'text': '查看成就'},
            {'key': '3', 'text': '清除数据'},
            {'key': '4', 'text': '关于'},
            {'key': '5', 'text': '退出'}
        ]
    })

@app.route('/api/choose_start', methods=['POST'])
def api_choose_start():
    user_state["school"] = None
    user_state["event_idx"] = 0
    user_state["stage"] = "fixed"
    user_state["random_used"] = set()
    user_state["last_random_idx"] = None

    choice = request.json.get('choice')
    if choice == '5':
        return jsonify({
            'message': '感谢游玩，期待下次再见！',
            'game_over': True
        })
    start_event = random.choices(event_list, weights=[0.2, 0.5, 0.3])[0]
    return jsonify({
        'message': f"{start_event}。\n你中考考得很好，现在可以选择学校。",
        'options': [
            {'key': '1', 'text': '羊县中学'},
            {'key': '2', 'text': '闪西省汗忠中学'},
            {'key': '3', 'text': '汗忠市龙港高级中学'}
        ],
        'start_event': start_event,
        'next_event': 'choose_school'
    })

@app.route('/api/choose_school', methods=['POST'])
def api_choose_school():
    school = request.json.get('school')
    start_event = request.json.get('start_event')
    user_state["school"] = school
    user_state["event_idx"] = 0
    user_state["stage"] = "fixed"
    user_state["random_used"] = set()
    user_state["last_random_idx"] = None

    if school == '1':
        event = event_1_list[0]
    elif school == '2':
        event = event_2_list[0]
    elif school == '3':
        event = event_3_list[0]
    else:
        return jsonify({'message': '未知学校', 'game_over': True})

    # 如果是字符串，直接返回；如果是对象，拼接贡献者
    if isinstance(event, dict):
        msg = event['question'] + get_contributor_str(event)
        options = [{'key': k, 'text': v} for k, v in event['choices'].items()]
    else:
        msg = event
        options = []
    return jsonify({
        'message': msg,
        'options': options,
        'next_event': 'school_event'
    })

@app.route('/api/school_event', methods=['POST'])
def api_school_event():
    global score
    choice = request.json.get('choice')
    school = user_state["school"]
    idx = user_state["event_idx"]

    if school == '1':
        event_list_now = event_1_list
    elif school == '2':
        event_list_now = event_2_list
    elif school == '3':
        event_list_now = event_3_list
    else:
        return jsonify({'message': '未知学校', 'game_over': True})

    event = event_list_now[idx]
    if isinstance(event, dict):
        result, is_end = pick_result(event['results'][str(choice)])
        msg = event['question'] + get_contributor_str(event)
        options = [{'key': k, 'text': v} for k, v in event['choices'].items()]
        achievements_dict = event.get('achievements', {})
        end_game_choices = event.get('end_game_choices', [])
    else:
        result, is_end = "", False
        msg = event
        options = []
        achievements_dict = {}
        end_game_choices = []

    triggered_achievements = []
    for k, ach in achievements_dict.items():
        if str(choice) == k:
            triggered_achievements.append(ach)
            if ach not in achievements:
                achievements.append(ach)

    # 概率死亡 或 固定死亡
    if is_end or str(choice) in end_game_choices:
        return jsonify({
            'result': result,  # 或者空字符串
            'message': "你失败了，游戏结束！",
            'game_over': True,
            'achievements': triggered_achievements
        })

    user_state["event_idx"] += 1
    score += 1

    if user_state["event_idx"] < len(event_list_now):
        next_event = event_list_now[user_state["event_idx"]]
        if isinstance(next_event, dict):
            next_msg = next_event['question'] + get_contributor_str(next_event)
            next_options = [{'key': k, 'text': v} for k, v in next_event['choices'].items()]
        else:
            next_msg = next_event
            next_options = []
        return jsonify({
            'result': result,  # 新增：只放上一个结果
            'message': next_msg,  # 新问题
            'options': next_options,
            'next_event': 'school_event',
            'achievements': triggered_achievements
        })
    else:
        user_state["stage"] = "random"
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({
                'result': result,
                'message': "所有事件已完成，游戏结束！",
                'achievements': triggered_achievements,
                'game_over': True,
                'options': []
            })
        idx = random.choice(unused)
        user_state["random_used"].add(idx)
        event = random_events[idx]
        msg = event['question'] + get_contributor_str(event)
        options = [{'key': k, 'text': v} for k, v in event['choices'].items()]
        return jsonify({
            'result': result,  # 只放上一个结果
            'message': msg,    # 新问题
            'options': options,
            'next_event': 'random_event',
            'achievements': triggered_achievements
        })

@app.route('/api/random_event', methods=['POST'])
def api_random_event():
    global score
    choice = request.json.get('choice')
    if choice is None or user_state.get("last_random_idx") is None:
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({
                'result': "",
                'message': "所有事件已完成，游戏结束！",
                'game_over': True,
                'options': []
            })
        idx = random.choice(unused)
        user_state["last_random_idx"] = idx
        event = random_events[idx]
        msg = event['question'] + get_contributor_str(event)
        options = [{'key': k, 'text': v} for k, v in event['choices'].items()]
        return jsonify({
            'result': "",
            'message': msg,
            'options': options,
            'next_event': 'random_event'
        })

    idx = user_state.get("last_random_idx")
    if idx is None:
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({'message': '所有事件已完成，游戏结束！', 'game_over': True})
        idx = random.choice(unused)
        user_state["last_random_idx"] = idx
    event = random_events[idx]
    result, is_end = pick_result(event['results'][str(choice)])
    end_game_choices = event.get('end_game_choices', [])
    achievements_dict = event.get('achievements', {})
    triggered_achievements = []
    for k, ach in achievements_dict.items():
        if str(choice) == k:
            triggered_achievements.append(ach)
            if ach not in achievements:
                achievements.append(ach)
    if is_end or str(choice) in end_game_choices:
        user_state["random_used"].add(idx)
        return jsonify({
            'result': result,
            'message': "游戏结束！",
            'game_over': True,
            'achievements': triggered_achievements,
            'options': []  # 明确返回空选项，防止前端渲染出错
        })
    user_state["random_used"].add(idx)
    score += 1
    unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
    if not unused:
        return jsonify({
            'message': result + "\n所有事件已完成，游戏结束！",
            'achievements': triggered_achievements,
            'game_over': True
        })
    next_idx = random.choice(unused)
    user_state["last_random_idx"] = next_idx
    next_event = random_events[next_idx]
    msg = next_event['question'] + get_contributor_str(next_event)
    options = [{'key': k, 'text': v} for k, v in next_event['choices'].items()]
    return jsonify({
        'result': result,  # 新增：只放上一个结果
        'message': msg,    # 新问题
        'options': options,
        'next_event': 'random_event',
        'achievements': triggered_achievements
    })

@app.route('/api/get_achievements', methods=['GET'])
def api_get_achievements():
    return jsonify({
        'score': score,
        'achievements': achievements
    })

@app.route('/api/clear_data', methods=['POST'])
def api_clear_data():
    achievements.clear()
    global score
    score = 0
    return jsonify({'message': '数据已清除！'})

@app.route('/assets/images/<path:filename>')
def custom_static_images(filename):
    if getattr(sys, 'frozen', False):
        assets_dir = os.path.join(sys._MEIPASS, 'assets', 'images')
    else:
        assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets/images'))
    # 兼容分隔符
    safe_filename = filename.replace('/', os.sep).replace('\\', os.sep)
    full_path = os.path.join(assets_dir, safe_filename)
    print("Trying to serve image:", full_path)
    if not os.path.isfile(full_path):
        print("File not found:", full_path)
        return "Not Found", 404
    return send_file(full_path)

def run_flask():
    app.run(debug=False, port=5001)

if __name__ == '__main__':
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    # 打开默认浏览器访问本地页面
    webbrowser.open("http://localhost:5001")
        # 如果你还需要 webview 窗口，也可以保留Add commentMore actions
    window = webview.create_window(
        title=f"OK School Life {version}",
        url="http://localhost:5001",
        width=800,
        height=600,
        resizable=True
    )
    webview.start()

# 2025.6.8 03:05, UTC+08:00