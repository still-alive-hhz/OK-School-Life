'''
OK School Life
==============

A school life management application.

Authors: Still_Alive & WaiJade
Version: {version}
Copyright © 2025 Still_Alive & WaiJade
'''
import random
import tkinter as tk
from tkinter import messagebox
import yaml
with open("/Users/houhaozhe/Documents/GitHub/OK-School-Life/data/events.yaml", "r", encoding="utf-8") as f:
    event_data = yaml.safe_load(f)

# 读取事件数据
event_list = event_data["event_list"]
event_1_list = event_data["event_1_list"]
event_2_list = event_data["event_2_list"]
event_3_list = event_data["event_3_list"]
random_events = event_data["random_events"]

# 让版本号作为变量方便调用，而不用手动修改
version = "v0.3.10"

# 初始化主窗口
root = tk.Tk()
root.title("OK School Life")
root.geometry("1280x720")

# 全局变量
achievements = []  # 存储玩家获得的成就
used_event_indices = []  # 存储已触发的事件索引
current_event = None  # 当前事件
current_choices = {}  # 当前事件的选项
score = int(0)  # 玩家分数

# 添加全局变量来跟踪当前事件索引
current_event_1_index = 0
current_event_2_index = 0
current_event_3_index = 0

# 替换占位符
contributors = {
    "ctb_wai": "(由WaiJade贡献)",
    "adp_lag": "(由lagency亲身经历改编)",
    "ctb_zhi": "(由智心逍遥贡献)",
    "ctb_sky": "(由sky贡献)"
}

# 遍历事件并替换占位符
for event in event_data.get("random_events", []):
    if "question" in event:
        event["question"] = event["question"].format(**contributors)


# 显示欢迎界面
def show_welcome():
    global used_event_indices
    used_event_indices = []
    for widget in root.winfo_children():
        widget.destroy()
    
    # 加载图片
    try:
        welcome_image = tk.PhotoImage(file="/Users/houhaozhe/Documents/GitHub/OK-School-Life/assets/images/welcome_min.png")
        tk.Label(root, image=welcome_image).pack(pady=10)
        root.welcome_image = welcome_image  # 防止图片被垃圾回收
    except Exception as e:
        print(f"无法加载图片: {e}")

    tk.Label(root, text=f"欢迎来到 OK School Life beta {version}", font=(20)).pack(pady=20)
    tk.Button(root, text="开始游戏", command=start_game, font=(14)).pack(pady=10)
    tk.Button(root, text="查看成就", command=show_achievements, font=(14)).pack(pady=10)
    tk.Button(root, text="退出游戏", command=root.quit, font=(14)).pack(pady=10)

def start_game():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="你将经历不同的事件和选择，看看你的学校生活会如何发展。", font=(16), wraplength=500).pack(pady=20)
    tk.Button(root, text="开始事件", command=main, font=(14)).pack(pady=10)
    tk.Button(root, text="返回主菜单", command=show_welcome, font=(14)).pack(pady=10)


        # 测试函数的调用（放到函数外面了，不然无法运行）
    '''
        elif tostart == "3":
        test()
    '''

# 主函数
def main():
    for widget in root.winfo_children():
        widget.destroy()

    # 显示初始事件
    start_event = random.choices(event_list, weights=[0.2, 0.5, 0.3])[0]
    tk.Label(root, text=f"{start_event}。\n你中考考得很好，现在可以选择学校。", font=(16), wraplength=500).pack(pady=20)

    # 显示学校选择按钮
    tk.Button(root, text="羊县中学", command=lambda: handle_school_choice("1", start_event), font=(14)).pack(pady=5)
    tk.Button(root, text="闪西省汗中中学", command=lambda: handle_school_choice("2", start_event), font=(14)).pack(pady=5)
    tk.Button(root, text="汗中市龙港高级中学", command=lambda: handle_school_choice("3", start_event), font=(14)).pack(pady=5)

# 处理学校选择
def handle_school_choice(choice, start_event):
    if choice == "1":
        tk.Label(root, text="你选择了羊县中学。", font=(14)).pack(pady=10)
        event_1()
    elif choice == "2":
        tk.Label(root, text="你选择了闪西省汗中中学。", font=(14)).pack(pady=10)
        event_2()
    elif choice == "3":
        if start_event == event_list[2]:
            messagebox.showinfo("游戏结束", "你家境贫寒，直接破产了！\n游戏结束。")
            show_welcome()
        else:
            tk.Label(root, text="你选择了汗中市龙港高级中学。", font=(14)).pack(pady=10)
            event_3()

# 添加一个全局变量来跟踪当前事件索引
current_event_1_index = 0

def event_1():
    global current_event_1_index

    # 检查是否还有未执行的事件
    if current_event_1_index >= len(event_1_list):
        random_event()  # 继续随机事件
        return

    for widget in root.winfo_children():
        widget.destroy()

    # 显示当前事件问题
    event_1_choice = event_1_list[current_event_1_index]
    tk.Label(root, text=event_1_choice, font=(16), wraplength=500).pack(pady=20)

    # 根据事件显示选项
    if event_1_choice == event_1_list[0]:
        choices = {"1": "继续听演讲", "2": "请假回家", "3": "向老师投诉"}
        results = {"1": "你选择了继续听演讲。\n演讲结束后，你感到很疲惫。",
                   "2": "你选择了请假回家。\n你被家长骂了。",
                   "3": "你选择了向老师投诉。\n你失败了。老师难道能管校长的事？"}
    elif event_1_choice == event_1_list[1]:
        choices = {"1": "符合无钱补课者的利益", "2": "不合理的制度", "3": "有的学校两周一放，知足常乐"}
        results = {"1": "你选择了符合无钱补课者的利益。\n你感到很开心。",
                   "2": "你选择了不合理的制度。\n你开始对此抱有异见。",
                   "3": "你选择了有的学校两周一放，知足常乐。\n你感到压抑且自由。"}
    elif event_1_choice == event_1_list[2]:
        choices = {"1": "乘坐电梯", "2": "走楼梯", "3": "不管"}
        results = {"1": "你选择了乘坐电梯。\n你违反了学生条例，游戏失败。",
                   "2": "你选择了走楼梯。\n你感到很累。",
                   "3": "你选择了不管。\n好像什么也没有发生。"}
    else:
        return

    # 显示选项按钮
    for key, value in choices.items():
        tk.Button(root, text=value, command=lambda k=key: handle_event_1_choice(k, event_1_choice, results), font=(14)).pack(pady=5)

# 处理事件 1 的选择
def handle_event_1_choice(choice, event_1_choice, results):
    global current_event_1_index

    result = results[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_1_choice == event_1_list[0] and choice == "3") or (event_1_choice == event_1_list[2] and choice == "1"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        # 继续下一个事件
        current_event_1_index += 1
        event_1()

def event_2():
    global current_event_2_index

    # 检查是否还有未执行的事件
    if current_event_2_index >= len(event_2_list):
        random_event()  # 继续随机事件
        return

    for widget in root.winfo_children():
        widget.destroy()

    # 显示当前事件问题
    event_2_choice = event_2_list[current_event_2_index]
    tk.Label(root, text=event_2_choice, font=(16), wraplength=500).pack(pady=20)

    # 根据事件显示选项
    if event_2_choice == event_2_list[0]:
        choices = {"1": "烈日下硬撑着", "2": "向老师说明", "3": "大声呵斥军训不人性化"}
        results = {"1": "你选择了烈日下硬撑着。\n你中暑进医院了！",
                   "2": "你选择了向老师说明。\n老师夸你勇敢，让你休息了。",
                   "3": "你选择了大声呵斥军训不人性化。\n你被教官骂了一顿，心情很不好。"}
    elif event_2_choice == event_2_list[1]:
        choices = {"1": "加入社团", "2": "不加入社团", "3": "向老师举报"}
        results = {"1": "你选择了加入社团。\n你感到很开心。",
                   "2": "你选择了不加入社团。\n你感到很无聊。",
                   "3": "你选择了向老师举报。\n老师告诉你这是正常操作。"}
    elif event_2_choice == event_2_list[2]:
        choices = {"1": "忍耐", "2": "向老师投诉", "3": "把舍友打一顿"}
        results = {"1": "你选择了忍耐。\n你整晚没睡好，你很烦躁。",
                   "2": "你选择了向老师投诉。\n老师告诉你这是正常现象，你很无奈。",
                   "3": "你选择了把舍友打一顿。\n你因违反校规被开除！"}
    else:
        return

    # 显示选项按钮
    for key, value in choices.items():
        tk.Button(root, text=value, command=lambda k=key: handle_event_2_choice(k, event_2_choice, results), font=(14)).pack(pady=5)

# 处理事件 2 的选择
def handle_event_2_choice(choice, event_2_choice, results):
    global current_event_2_index

    result = results[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_2_choice == event_2_list[0] and choice == "1") or (event_2_choice == event_2_list[2] and choice == "3"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        # 继续下一个事件
        current_event_2_index += 1
        event_2()

def event_3():
    global current_event_3_index

    # 检查是否还有未执行的事件
    if current_event_3_index >= len(event_3_list):
        random_event()  # 继续随机事件
        return

    for widget in root.winfo_children():
        widget.destroy()

    # 显示当前事件问题
    event_3_choice = event_3_list[current_event_3_index]
    tk.Label(root, text=event_3_choice, font=(16), wraplength=500).pack(pady=20)

    # 根据事件显示选项
    if event_3_choice == event_3_list[0]:
        choices = {"1": "大声呼救",
                   "2": "硬着头皮做",
                   "3": "把试卷撕了"}
        results = {"1": "你选择了大声呼救。\n老师以为你有精神病，将你遣返回原籍。",
                     "2": "你选择了硬着头皮做。\n你考得很差，父母把你骂了一顿。",
                     "3": "你选择了把试卷撕了。\n老师夸你有胆量，并给你一套高考真题。"}
    elif event_3_choice == event_3_list[1]:
        choices = {"1": "巴结这位同学",
                   "2": "去看ta的父母是何方神圣",
                   "3": "偷拍ta家的车，并发布到网上"}
        results = {"1": "你选择了巴结这位同学。\n你成为了ta的众多跟班之一。",
                   "2": "你选择了去看ta的父母是何方神圣。\nta的父亲对你说：好好学，争取以后能当上ta的秘书。",
                   "3": "你选择了偷拍ta家的车，并发布到网上。\n一封邮件让你删除视频，第二天你因为进教室先迈左脚被开除！"}
    elif event_3_choice == event_3_list[2]:
        choices = {"1": "先写作业",
                   "2": "先洗澡",
                   "3": "去天台看夜景"}
        results = {"1": "你选择了先写作业。\n你写到熄灯时间也没写完。",
                   "2": "你选择了先洗澡。\n你感到很舒服，但是被没写作业的恐慌占据。",
                   "3": "你选择了去天台看夜景。\n班主任发现了你，让心理老师和你谈心一晚上。你很疲惫。"}
    else:
        return

    # 显示选项按钮
    for key, value in choices.items():
        tk.Button(root, text=value, command=lambda k=key: handle_event_3_choice(k, event_3_choice, results), font=(14)).pack(pady=5)

# 处理事件 3 的选择
def handle_event_3_choice(choice, event_3_choice, results):
    global current_event_3_index

    result = results[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_3_choice == event_3_list[0] and choice == "1") or (event_3_choice == event_3_list[1] and choice == "3"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        # 继续下一个事件
        current_event_3_index += 1
        event_3()

def check_random_results(event, choice):
    if event["question"] == ">>>在宿舍流鼻血，你会？" and choice == "1":
        # 定义随机结果
        rd_results = [
            "流了几分钟就不流了，没事。",
            "你因失血过多进医院了！"
        ]
        # 根据权重随机选择结果
        result = random.choices(rd_results, weights=[0.6, 0.4])[0]
        messagebox.showinfo("随机结果", result)

        # 如果结果是严重后果，结束游戏
        if result == "你因失血过多进医院了！":
            messagebox.showinfo("游戏结束", "游戏结束！")
            show_achievements()
            root.quit()
    elif event["question"] == ">>>语文课上，老师点人背诵来决定作业，点到你，选择：{ctb_zhi}" and choice == "3":
        # 定义随机结果
        rd_results = [
            '老师告诉你下课后给她背，并免了作业。',
            '老师罚全班作业，你被同学鄙夷。',
            '老师大骂全班，你被同学们打进医院！',
        ]
        # 根据权重随机选择结果
        result = random.choices(rd_results, weights=[0.15, 0.7,0.15])[0]
        messagebox.showinfo("随机结果", result)
        # 如果结果是严重后果，结束游戏
        if result == "老师大骂全班，你被同学们打进医院！":
            messagebox.showinfo("游戏结束", "游戏结束！")
            show_achievements()
            root.quit()

used_event_indices = []

# 随机事件处理
def random_event():
    global last_event, score
    for widget in root.winfo_children():
        widget.destroy()

    # 检查是否所有事件都已触发
    if len(used_event_indices) == len(random_events):
        messagebox.showinfo("游戏结束", "所有随机事件已体验完，游戏结束！")
        show_achievements()
        return

    # 随机选择一个未触发的事件
    while True:
        idx = random.randint(0, len(random_events) - 1)
        if idx not in used_event_indices:
            used_event_indices.append(idx)
            score += 1
            break

    event = random_events[idx]
    last_event = event


    # 显示事件问题
    tk.Label(root, text=event["question"], font=(16), wraplength=500).pack(pady=20)

    # 显示选项按钮
    for key, value in event["choices"].items():
        tk.Button(root, text=value, command=lambda k=key: handle_random_choice(event, k), font=(14)).pack(pady=5)

# 处理随机事件的选择
def handle_random_choice(event, choice):
    result = event["results"][choice]
    messagebox.showinfo("结果", result)

    # 检查是否有随机结果
    check_random_results(event, choice)

    # 检查是否解锁成就
    handle_achievements(event, choice)

    # 检查是否是游戏结束选项
    if "end_game_choices" in event and choice in event["end_game_choices"]:
        messagebox.showinfo("游戏结束", "游戏结束！")
        show_achievements()
        return

    # 继续下一个随机事件
    random_event()

# 处理成就
def handle_achievements(event, choice):
    if "achievements" in event and choice in event["achievements"]:
        achievement = event["achievements"][choice]
        if achievement not in achievements:
            achievements.append(achievement)
            messagebox.showinfo("成就解锁", f"恭喜你获得了成就：{achievement}！")

# 显示成就
def show_achievements():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="游戏记录页", font=(20)).pack(pady=20)
    tk.Label(root, text=f"你的分数为{score}", font=(14)).pack(pady=5)
    if achievements:
        for achievement in achievements:
            tk.Label(root, text=f"- {achievement}", font=(14)).pack(pady=5)
    else:
        tk.Label(root, text="你还没有获得任何成就。", font=(14)).pack(pady=5)
    tk.Button(root, text="返回主菜单", command=show_welcome, font=(14)).pack(pady=20)


# 这个函数用于测试随机结果的可行性，已经成功，为以后测试做模板，以注释形式保留。
''' def test():
    rd_30_consequence = random.choices(rd_30_results, weights = [0.6, 0.4])[0]
    print(rd_30_consequence)
    if rd_30_consequence == rd_30_results[0]:
        random_event()
    else:
        print("游戏结束。")
'''


if __name__ == "__main__":
    # 启动程序
    show_welcome()
    root.mainloop()

# Version beta 0.3.10
# Designed by Still_Alive with Github Copilot and OpenAI ChatGPT
# Contributed by WaiJade with DeepSeek and Kimi
# 2025.05.09 03:00 China Standard Time
# Thank you for playing!