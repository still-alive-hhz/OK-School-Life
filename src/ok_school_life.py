import webview
from flask import Flask, jsonify, request, render_template
from pathlib import Path
import random, os, yaml

# 初始化Flask应用
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '../static')
)

# 加载游戏数据
with open(Path(__file__).parent.parent / 'data' / 'events.yaml', encoding='utf-8') as f:
    game_data = yaml.safe_load(f)

# 动态获取路径
base_dir = os.path.dirname(os.path.abspath(__file__))
yaml_path = os.path.join(base_dir, "../data/events.yaml")

# 加载 YAML 文件
try:
    with open(yaml_path, "r", encoding="utf-8") as f:
        event_data = yaml.safe_load(f)
except FileNotFoundError:
    print("Error: events.yaml 文件未找到！")
    event_data = {"random_events": []}
except yaml.YAMLError as e:
    print(f"Error: 无法解析 YAML 文件: {e}")
    event_data = {"random_events": []}

# 读取事件数据
event_list = event_data["event_list"]
event_1_list = event_data["event_1_list"]
event_2_list = event_data["event_2_list"]
event_3_list = event_data["event_3_list"]
random_events = event_data["random_events"]

# 让版本号作为变量方便调用，而不用手动修改
version = "v0.4.0"

# 新增：定义用户状态
user_state = {
    "school": None,      # 记录选择的学校
    "event_idx": 0,      # 当前固定事件索引
    "stage": "fixed",    # "fixed" 或 "random"
    "random_used": set() # 已用的随机事件索引
}

achievements = []  # 存储玩家获得的成就
used_event_indices = []  # 存储已触发的事件索引
current_event = None  # 当前事件
current_choices = {}  # 当前事件的选项
score = int(0)  # 玩家分数

# 替换占位符
contributors = {
    "ctb_wai": "(由WaiJade贡献)",
    "adp_lag": "(由lagency亲身经历改编)",
    "ctb_zhi": "(由智心逍遥贡献)",
    "ctb_sky": "(由sky贡献)",
    'ctb_tmt': '(由Tomato贡献)',
    'ctb_guo': '(由GuoHao贡献)',
    'ctb_yax': '(由YaXuan贡献)',
    'ctb_wai, guo': '(由WaiJade和GuoHao贡献)',
}

# 遍历事件并替换占位符
for event in event_data.get("random_events", []):
    if "question" in event:
        event["question"] = event["question"].format(**contributors)



# 创建 Flask API 路由
@app.route('/')
def home():
    """返回前端HTML页面"""
    return render_template('index.html')

# 保留你原有的API路由
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
    # 只重置与本局流程相关的状态
    user_state["school"] = None
    user_state["event_idx"] = 0
    user_state["stage"] = "fixed"
    user_state["random_used"] = set()
    user_state["last_random_idx"] = None
    # 不清空 achievements、score 等

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
    user_state["last_random_idx"] = None  # 新增：重置

    if school == '1':
        event = event_1_list[0]
    elif school == '2':
        event = event_2_list[0]
    elif school == '3':
        event = event_3_list[0]
    else:
        return jsonify({'message': '未知学校', 'game_over': True})

    # 只返回问题，不拼接结果
    return jsonify({
        'message': event['question'],
        'options': [{'key': k, 'text': v} for k, v in event['choices'].items()],
        'next_event': 'school_event'
    })

# 类似地为每个事件类型创建API端点...
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
    result = event['results'][str(choice)]

    # 成就判断（每次都返回本次触发的成就，无论是否已获得）
    achievements_dict = event.get('achievements', {})
    triggered_achievements = []
    for k, ach in achievements_dict.items():
        if str(choice) == k:
            triggered_achievements.append(ach)
            if ach not in achievements:
                achievements.append(ach)

    # 死亡判断（提前，且带成就返回）
    end_game_choices = event.get('end_game_choices', [])
    if str(choice) in end_game_choices:
        return jsonify({
            'message': result + "\n你失败了，游戏结束！",
            'game_over': True,
            'achievements': triggered_achievements
        })

    user_state["event_idx"] += 1
    score += 1  # 每经历一个事件分数+1

    if user_state["event_idx"] < len(event_list_now):
        next_event = event_list_now[user_state["event_idx"]]
        return jsonify({
            'message': result + "\n" + next_event['question'],
            'options': [{'key': k, 'text': v} for k, v in next_event['choices'].items()],
            'next_event': 'school_event',
            'achievements': triggered_achievements
        })
    else:
        user_state["stage"] = "random"
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({
                'message': result + "\n所有事件已完成，游戏结束！",
                'achievements': triggered_achievements,
                'game_over': True
            })
        idx = random.choice(unused)
        user_state["random_used"].add(idx)
        event = random_events[idx]
        return jsonify({
            'message': result + "\n" + event['question'],
            'options': [{'key': k, 'text': v} for k, v in event['choices'].items()],
            'next_event': 'random_event',
            'achievements': triggered_achievements
        })

@app.route('/api/random_event', methods=['POST'])
def api_random_event():
    global score
    choice = request.json.get('choice')
    # 如果是第一次进入随机事件，choice 为空，直接出题
    if choice is None or user_state.get("last_random_idx") is None:
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({'message': '所有事件已完成，游戏结束！', 'game_over': True})
        idx = random.choice(unused)
        user_state["last_random_idx"] = idx
        event = random_events[idx]
        return jsonify({
            'message': event['question'],
            'options': [{'key': k, 'text': v} for k, v in event['choices'].items()],
            'next_event': 'random_event'
        })

    # 否则，choice 有值，先显示结果
    idx = user_state.get("last_random_idx")
    if idx is None:
        unused = [i for i in range(len(random_events)) if i not in user_state["random_used"]]
        if not unused:
            return jsonify({'message': '所有事件已完成，游戏结束！', 'game_over': True})
        idx = random.choice(unused)
        user_state["last_random_idx"] = idx
    event = random_events[idx]
    result = event['results'][str(choice)]

    # 死亡判断
    end_game_choices = event.get('end_game_choices', [])
    if str(choice) in end_game_choices:
        user_state["random_used"].add(idx)
        # 成就判断（每次都返回本次触发的成就，无论是否已获得）
        achievements_dict = event.get('achievements', {})
        triggered_achievements = []
        for k, ach in achievements_dict.items():
            if str(choice) == k:
                triggered_achievements.append(ach)
                if ach not in achievements:
                    achievements.append(ach)
        return jsonify({
            'message': result + "\n你失败了，游戏结束！",
            'game_over': True,
            'achievements': triggered_achievements
        })

    # 成就判断（每次都返回本次触发的成就，无论是否已获得）
    achievements_dict = event.get('achievements', {})
    triggered_achievements = []
    for k, ach in achievements_dict.items():
        if str(choice) == k:
            triggered_achievements.append(ach)
            if ach not in achievements:
                achievements.append(ach)

    user_state["random_used"].add(idx)
    score += 1  # 每经历一个事件分数+1

    # 进入下一个随机事件
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
    return jsonify({
        'message': result + "\n" + next_event['question'],
        'options': [{'key': k, 'text': v} for k, v in next_event['choices'].items()],  # 修正这里
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

def run_flask():
    app.run(debug=False, port=5001)  # port=0 让系统自动选择可用端口

if __name__ == '__main__':
    # 先启动Flask服务器
    import threading
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # 创建PyWebView窗口
    window = webview.create_window(
        title=f"OK School Life {version}",
        url="http://localhost:5001",  # 端口
        width=800,
        height=600,
        resizable=True
    )
    
    # 启动GUI
    webview.start()

# 2025.5.30 22.13, China Standard Time