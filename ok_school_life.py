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

# 让版本号作为变量方便调用，而不用手动修改
version = "v0.3.0"

# 初始化主窗口
root = tk.Tk()
root.title("OK School Life")
root.geometry("600x400")

# 全局变量
achievements = []  # 存储玩家获得的成就
used_event_indices = []  # 存储已触发的事件索引
current_event = None  # 当前事件
current_choices = {}  # 当前事件的选项

event_list = ['**你在一个富裕家庭**', '**你在一个普通家庭**', '**你在一个贫穷家庭**']
event_1_list = ['>>>第一周开家长会，校长讲话时间超出预计时间一小时，导致放学时间延迟，你会？',
                '>>>面对单休制，你开始了怎样的思考？',
                '>>>看到学校的电梯，你会怎么做？',]
event_2_list = ['>>>军训时你感到身体不适，你会？',
                '>>>社团招新，你会？',
                '>>>舍友睡觉呼噜声很大，你会？',]
event_3_list = ['>>>开学考试，你发现试题很难，你选择？',
                '>>>看到有同学乘坐黑色高级车，你会？',
                '>>>放学后时间很紧，你选择？',]
# 随机事件列表
random_events = [
    {
        "question": '>>>你在学校的食堂吃饭，发现菜品很差，你会？', 
        "choices": {"1": "继续吃饭",
                    "2": "投诉",
                    "3": "罢吃"},
        "results": {"1": "你选择了继续吃饭。\n你感到很失望。",
                    "2": "你选择了投诉。\n你被老师骂了，心情很不好。",
                    "3": "你选择了罢吃。\n你因颠覆学校而被开除，你失败了！。"},
        'end_game_choices': ["3"],
    },
    {
        "question": '>>>你在学校的图书馆借书，发现没有你想要的书，你会？',
        "choices": {"1": "继续借书",
                   "2": "去找老师",
                   "3": "大声辱骂学校藏书不够"},
        "results": {"1": "你选择了继续借书。\n你感到很失望。",
                    "2": "你选择了去找老师。\n老师告诉你没有书。",
                    "3": "你选择了大声辱骂学校藏书不够。\n你被年级主任骂了一顿，心情很不好。"},
        'end_game_choices': ["3"],
    },
    {
        "question": '>>>你在学校的操场上看到同学们打篮球，你会？',
        "choices": {"1": "加入这些人",
                    "2": "拍照发朋友圈",
                    "3": "去打篮球"},
        "results": {"1": "你选择了加入这些人。\n这些人嘲笑你打得太菜，你心情很不好。",
                    "2": "你选择了拍照发朋友圈。\n你喜欢的女生/男生看到了，问你要了照片。",
                    "3": "你选择了去打篮球。\n你感到很开心。"},
        'end_game_choices': [],
    },
    {
        "question": '>>>你在学校的实验室里做实验，发现实验器材损坏，你会？',
        "choices": {"1": "修理实验器材",
                    "2": "不管",
                    "3": "向老师报告"},
        "results": {"1": "你选择了修理实验器材。\n实验器材修好了，你受到老师的赞赏。",
                    "2": "你选择了不管。\n氯气泄漏，你中毒了！游戏结束。",
                    "3": "你选择了向老师报告。\n老师告诉你没事。"},
        'end_game_choices': ["2"],
    },
    {
        "question": '>>>你在学校的宿舍里，发现室友总是打游戏，你会？',
        "choices": {"1": "向班主任举报",
                   "2": "向年轻老师举报",
                   "3": "和室友商量"},
        "results": {"1": "你选择了向班主任举报。\n他们知道后，叫一群人把你打了一顿！你进医院了。",
                    "2": "你选择了向年轻老师举报。\n老师告诉你这是个人隐私。",
                    "3": "你选择了和室友商量。\n你们决定一起打游戏。"},
        'end_game_choices': ["1"],
    },
    { # event 5
        "question": '>>>你在学校的教室里，发现同学们在讨论考试作弊，你会？',
        "choices": {"1": "加入他们",
                    "2": "拍照发朋友圈",
                    "3": "忽视"},
        "results": {"1": "你选择了加入他们。\n你们一起作弊，被校长发现。你被开除了！",
                    "2": "你选择了拍照发朋友圈。\n校长看到了，表扬你的举报行为，并没收了你的手机。",
                    "3": "你选择了忽视。\n他们这次都比你考得高，你很难过。"},
        'end_game_choices': ["1"],
    },
    {
        "question": '>>>考试：sin x = cos ____？',
        "choices": {"1": "x + π",
                    "2": "x - π/2",
                    "3": "x + π/2"},
        "results": {"1": "你选择了x + π。\n你错得太离谱，被开除了！",
                    "2": "你选择了x - π/2。\n你过关！。",
                    "3": "你选择了x + π/2。\n你考得很差，父母把你骂了一顿。"},
        'end_game_choices': ["1"],
    },
    {
        "question": '>>>考试：sin 2x = ____？',
        "choices": {"1": "2(sinx)(cosx)",
                    "2": "π",
                    "3": "2x"},
        "results": {"1": "你选择了2(sinx)(cosx)。\n你过关！",
                    "2": "你选择了π。\n你错得太离谱，被开除了！",
                    "3": "你选择了2x。\n你考得很差，父母把你骂了一顿。"},
        'end_game_choices': ["2"],
    },
    {
        "question": '>>>考试：中国历史上的第一位皇帝是？',
        "choices": {"1": "泰始皇",
                    "2": "夏禹",
                    "3": "以上都不是"},
        "results": {"1": "你选择了泰始皇。\n你错得太离谱，被开除了！",
                    "2": "你选择了夏禹。\n你考得很差，父母把你骂了一顿。",
                    "3": "你选择了以上都不是。\n你得到了全班最高分，你感到很开心。"},
        'end_game_choices': ["1"],
        "achievements": {"3": "视力5.0"}, # 选择3触发成就
    },
    {
        "question": '>>>考试：tan x/2的周期是？',
        "choices": {"1": "x",
                    "2": "π/2",
                    "3": "2π"},
        "results": {"1": "你选择了x。\n你错得太离谱，被开除了！游戏结束。",
                    "2": "你选择了π/2。\n你考得很差，父母把你骂了一顿。",
                    "3": "你选择了2π。\n你过关！"},
        'end_game_choices': ["1"],
    },
    { # event 10
        "question": '>>>你和同学对比国摇和欧美摇滚，你会选择？',
        "choices": {"1": ""
        "国摇好",
                    "2": "欧美摇滚好",
                    "3": "尊重对方喜好"},
        "results": {"1": "你选择了国摇好。\n对方给你唱了一首《大石碎胸口》的尾奏。",
                    "2": "你选择了欧美摇滚好。\n对方给你唱了一首《Stairway to Heaven》的前奏。",
                    "3": "你选择了尊重对方喜好。\n你们愉快地交流了意见。"},
        'end_game_choices': [],
    },
    {
        "question": '>>>有同学组建“觉醒者联盟”，你选择？',
        "choices": {"1": "当普通成员",
                    "2": "当宣传部长",
                    "3": "向老师举报"},
        "results": {"1": "你选择了当普通成员。\n你们整天针砭时弊，成绩都下降了。",
                    "2": "你选择了宣传部长。\n东窗事发，你被警察调查后被学校开除了！",
                    "3": "你选择了向老师举报。\n老师夸赞你有独立头脑。"},
        'end_game_choices': ["2"],
    },
    {
        "question": '>>>你在学校的社团中，发现社团活动不符合你的兴趣，你会？',
        "choices": {"1": "继续待在社团",
                    "2": "退社并不加入其他社团",
                    "3": "跳槽喜欢的社团"},
        "results": {"1": "你选择了继续待在社团。\n你每周最烦恼的时刻就是社团课的40分钟。",
                    "2": "你选择了退社并不加入其他社团。\n你将社团时间用来学习，成绩猛涨。",
                    "3": "你选择了跳槽喜欢的社团。\n你得到了快乐，但是成绩下降了。"},    
        'end_game_choices': [],
    },
    {
        "question": '>>>班里有同学玩原神，你会？',
        "choices": {"1": "和他整天讨论",
                    "2": "背后说ta是OP",
                    "3": "当面说ta是OP"},
        "results": {"1": "你选择了和他整天讨论。\n你们很开心，但是成绩下降了。",
                   "2": "你选择了背后说他是OP。\n你们的友谊破裂了。",
                   "3": "你选择了当面说他是OP。\n他叫来一群同好，打了你一顿。你进医院了！"},
        'end_game_choices': ["3"],
        'achievements': {"1": "原神启动"} ,
    },
    {
        "question": '>>>班里有同学玩LOL，你会？',
        "choices": {"1": "和他讨论喜欢的英雄",
                    "2": "对他说不如王者荣耀",
                    "3": "无视他的存在"},
        "results": {"1": "你选择了和他讨论喜欢的英雄。\n你们很开心，但是成绩下降了。",
                    "2": "你选择了对他说不如王者荣耀。\n他叫来一群同好，打了你一顿。你失败了！",
                    "3": "你选择了无视他的存在。\n你深知学习最重要，考到了年级前20。"},
        'end_game_choices': ["2"],
        'achievements': {"3": "一心学习"},
    },
    { # event 15
        "question": '>>>今天早自习突然检查仪容仪表，你的头发被老师点名批评“不合规范”，你会？',
        "choices": {"1": "当场认错，说以后注意",
                    "2": "小声反驳，说这是个人风格",
                    "3": "大声吐槽老师审美落后"},
        "results": {"1": "你选择了当场认错，说以后注意。\n老师夸你知错就改，给你加了分。",
                    "2": "你选择了小声反驳，说这是个人风格。\n老师很生气，让你去办公室，给你剪了头发。",
                    "3": "你选择了大声吐槽老师审美落后。\n老师叫来了你的家长谈话，你被停课了！"},
        'end_game_choices': ["3"],
        'achievements': {"2": "理科发型"},
    },
    {
        "question": '>>>英语老师心血来潮临时宣布要测一张听写卷，你昨晚偏偏没背单词，你会？',
        "choices": {"1": "硬着头皮上",
                    "2": "装病逃课",
                    "3": "向学霸借速成小抄"},
        "results": {"1": "你选择了硬着头皮上。\n你考得很差，老师让你第二天重新默写。",
                   "2": "你选择了装病逃课。\n你被老师发现了，心情很不好。",
                   "3": "你选择了向学霸借速成小抄。\n你考得很好，你感到很开心。"},
        'end_game_choices': [],
    },
    {
        "question": ">>>学校食堂推出“健康套餐”，但卖相一般，面对它，你会？",
        "choices": {"1": "咬咬牙尝试一下，毕竟健康",
                    "2": "去小卖部买泡面",
                    "3": "拍照发群吐槽，带头抵制"},
        "results": {"1": "你选择了咬咬牙尝试一下\n非常难吃，使你下午的体育课反胃想吐。",
                   "2": "你选择了去小卖部买泡面。\n你感到很开心，但你被老师发现了，罚你写检查。",
                   "3": "你选择了拍照发群吐槽，带头抵制。\n你涉嫌颠覆学校食堂罪，被开除了！"},
        'end_game_choices': ["3"],
    },
    {
        "question": ">>>你被班主任安排参加1500米长跑选拔，你内心抗拒但又怕被扣分，你会？",
        "choices": {"1": "勉强上阵，全力跑完",
                    "2": "故意跑慢，装作不擅长",
                    "3": "提前和体育委员套好话，直接弃权"},
        "results": {"1": "你选择了勉强上阵，全力跑完。\n你跑到缺氧，进医院了。",
                   "2": "你选择了故意跑慢，装作不擅长。\n你被老师骂了，心情很不好。",
                   "3": "你选择了提前和体育委员套好话，直接弃权。\n你感到很开心，但是一部分同学对你议论纷纷。"},
        'end_game_choices': ["1"],
    },
    {
        "question": ">>>老师打开PPT，念稿40分钟，语速极慢，字还特别小。你会？",
        "choices": {"1": "努力集中精神，坚持到底",
                    "2": "大声呵斥老师",
                    "3": "偷偷写作业，节省时间"},
        "results": {"1": "你选择了努力集中精神。\n你感到很脑神经衰弱，视线模糊。",
                   "2": "你选择了大声呵斥老师。\n老师请来了你的家长，让你停课了！",
                   "3": "你选择了偷偷写作业，节省时间。\n你被老师发现了，老师把你的作业撕了。"},
        'end_game_choices': ["2"],
    },
    { # event 20
        "question": ">>>放学时突然下起大雨，你没带伞，你会？",
        "choices": {"1": "借同学的伞，送一段路再跑回家",
                    "2": "淋雨冲回家，冲凉省了",
                    "3": "在校门口避雨，顺便反思为何不看天气预报"},
        "results": {"1": "你选择了借同学的伞。\n虽然花了点时间，但是安全回家了。",
                   "2": "你选择了淋雨冲回家，冲凉省了。\n你第二天就发烧了，无法继续学习！",
                   "3": "你选择了在校门口避雨，顺便反思为何不看天气预报。\n你在风雨中多想了很多，也许成长就是这样被迫发生的。"},
        'end_game_choices': ["2"],
        'achievements': {"3": "成长"},
    },
    {
        "question": ">>>你这周要负责扫地，但今天作业太多，你想偷个懒。你会？",
        "choices": {"1": "找朋友帮忙，周末请ta喝饮料",
                    "2": "装作忘记，等老师点名再说",
                    "3": "拖延去扫，边扫边抱怨制度不合理"},
        "results": {"1": "你选择了找朋友帮忙。\n朋友满脸不情愿，但还是答应了。这种人情债，你记在心里了。",
                   "2": "你选择了装作忘记。\n老师点名了，你被扣分了。",
                   "3": "你选择了边扫边抱怨制度不合理。\n你涉嫌颠覆学校制度罪，被开除了！"},
        'end_game_choices': ["3"],
    },
    {
        "question": ">>>地理课，老师问：同学们，你们猜我是我们老李家第几代教书匠？",
        "choices": {"1": "你是老李家第二代教书匠",
                    "2": "你是老李家第三代教书匠",
                    "3": "你是老李家第四代教书匠"},
        "results": {"1": "你选择了你是老李家第二代教书匠。\n老师冷笑着说：你低估了我们家族的实力。",
                   "2": "你选择了你是老李家第三代教书匠。\n老师说：我不是第三代教书匠，但我是三分之一。",
                   "3": "你选择了你是老李家第四代教书匠。\n老师说夸你聪明，给你加了分。"},
        'end_game_choices': [],
    },
    {
        "question": ">>>遇到老师，你选择低头。老师走近问你为什么不给她打招呼，你会？",
        "choices": {"1": "低头",
                    "2": "微笑",
                    "3": "说“我没有看到人”"},
        "results": {"1": "你选择了低头。\n老师说：下次记得打招呼。",
                   "2": "你选择了微笑。\n老师看你无奈，原谅了你。",
                   "3": "你选择了说“我没有看到人”。\n老师生气地说：我不是人吗？请来了你的家长。"},
        'end_game_choices': ["3"],
    },
    {
        "question": ">>>校园传奇浴室，看到一群烟哥在吸烟，你会？",
        "choices": {"1": "私下向校长举报",
                    "2": "直接开骂",
                    "3": "微笑着说：我也来一根",
                    "4": "无视"},
        "results": {"1": "你选择了私下向校长举报。\n校长高度赞赏你的行为，并在大会上让你上台领奖。",
                   "2": "你选择了直接开骂。\n烟哥一人一根烟头把你烫没了！",
                   "3": "你选择了微笑着说：我也来一根。\n你们一起吸烟，被老师发现了，心情很不好。",
                   "4": "你选择了无视。\n好像什么也没有发生。"},
        'end_game_choices': ["2"],
    },
    { # event 25
        "question": ">>>考试的时候，你有点在意的女生/男生坐在你旁边，你会？",
        "choices": {"1": "毫不在意，纯西格玛",
                    "2": "看看ta做题做到哪了",
                    "3": "问问ta这道题怎么做",
                    "4": "站起来大声说你要换座位"},
        "results": {"1": "你选择了毫不在意，做西格玛人。\n你冷静发挥，这次考试考的很好，你在下一次考试坐得离ta远了一些。",
                   "2": "你选择了看看ta做题做到哪了。\n你发现ta已经做到第二面了，而你还在第一面，你汗流浃背，不停擦汗，你考得很差，你下一次坐得离ta很远。",
                   "3": "你选择了问问ta这道题怎么做\n作弊被老师发现，老师给你的卷子做了标记，这科变成了0分，你在下一次坐得离ta很远。",
                   "4": "你选择了站起来说你要换座位\n老师拒绝了你，并且班级里出现了你的流言，你觉得很不舒服。"},
        'end_game_choices': [],
        'achievements': {"1": "西格玛人"},
    },
    {
        "question": ">>>听到同学在聊网络爽文，你会？",
        "choices": {"1": "觉得这东西很没营养",
                    "2": "大声说“网文都是垃圾！”",
                    "3": "问问老师"},
        "results": {"1": "你觉得这东西很没营养。\n你继续读你喜欢的名著，文采越来越好。",
                     "2": "你选择了大声说“网文都是垃圾！”。\n一群网文爱好者把你打进医院了！",
                     "3": "你选择了问问老师。\n老师告诉你这是个人喜好。"},
        'end_game_choices': ["2"]
    },
    {
        "question": ">>>星期一就想放假，你会？",
        "choices": {"1": "大声喊“我想放假！”",
                    "2": "认为只要认真学习，一周很快就会过去",
                    "3": "装病给自己放假"},
        "results": {"1": "你选择了大声喊“我想放假！”。\n你喜欢的人默默认为你是傻子。",
                    "2": "你选择了认真学习。\n你很努力，成绩突飞猛进。",
                    "3": "你选择了装病放假。\n你被家长识破了，老师和家长一起把你教育了一顿！你心情很不好。"},
        'end_game_choices': [],
    },
    {
        "question": ">>>班主任说从你家长那里打听来你天天玩电脑，你会？",
        "choices": {"1": "说“我在学编程”",
                    "2": "说“我没有玩电脑”",
                    "3": "说“我要辍学自己做游戏”"},
        "results": {"1": "你选择说“我在学编程”。\n老师和开发者夸你有前途，给你加了分。",
                   "2": "你选择说“我没有玩电脑”。\n老师微微一笑，拿出了你玩电脑的照片。",
                   "3": "你选择说“我要辍学自己做游戏”。\n老师告诉你：“我满足你的愿望。”你被开除了！"},
        'end_game_choices': ["3"],
        'achievements': {"1": "开发者の认可"},
    },
    {
        "question": ">>>在学校看见穿着自己喜欢的专辑封面衣服的人，你会？",
        "choices": {"1": "对ta说终于找到同好了",
                    "2": "说出这个乐队的名字",
                    "3": "唱出这首专辑里的歌"},      
        "results": {"1": "你选择了对他说终于找到同好了。\n他说“我只听过一两首歌。”",
                   "2": "你选择了说出这个乐队的名字。\n你连着说了两遍，对方也没听懂你在说什么。",
                   "3": "你选择了唱出这首专辑里的歌。\n对方说“什么歌，这么难听。”"},
        'end_game_choices': [],
    },
    { # event 30
        "question": ">>>在宿舍流鼻血，你会？",
        "choices": {"1": "只是用纸堵住，相信会好",
                    "2": "叫救护车",
                    "3": "请假去医院"},
        "results": {"1": "你选择了只是用纸堵住，相信会好。",
                   "2": "你选择了叫救护车。\n你在救护车上不流鼻血了，半路被送了回来。",
                   "3": "你选择了请假去医院。\n医生告诉你没事。"},
        'end_game_choices': [],
    },
    {
        "question": ">>>你刚开学，在食堂看到了某社社长，你会？",
        "choices": {"1": "无视",
                    "2": "上前打招呼",
                    "3": "大喊“我想她了！”"},
        "results": {"1": "你选择了无视。\n好像什么也没有发生",
                    "2": "你选择了上前打招呼。\n对方在QQ群里说你是正义插队者。",
                    "3": "你选择了大喊“我想她了！”\n对方说“我也想你了。”"},
        'end_game_choices': [],
        'achievements': {"3": "正义插队者"},
    }
]

# 显示欢迎界面
def show_welcome():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text=f"欢迎来到 OK School Life beta {version}", font=("", 20)).pack(pady=20)
    tk.Button(root, text="开始游戏", command=start_game, font=("", 14)).pack(pady=10)
    tk.Button(root, text="查看成就", command=show_achievements, font=("", 14)).pack(pady=10)
    tk.Button(root, text="退出游戏", command=root.quit, font=("", 14)).pack(pady=10)

def start_game():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="你将经历不同的事件和选择，看看你的学校生活会如何发展。", font=("", 16), wraplength=500).pack(pady=20)
    tk.Button(root, text="开始事件", command=main, font=("", 14)).pack(pady=10)
    tk.Button(root, text="返回主菜单", command=show_welcome, font=("", 14)).pack(pady=10)


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
    tk.Label(root, text=f"{start_event}。\n你中考考得很好，现在可以选择学校。", font=("", 16), wraplength=500).pack(pady=20)

    # 显示学校选择按钮
    tk.Button(root, text="羊县中学", command=lambda: handle_school_choice("1", start_event), font=("", 14)).pack(pady=5)
    tk.Button(root, text="闪西省汗中中学", command=lambda: handle_school_choice("2", start_event), font=("", 14)).pack(pady=5)
    tk.Button(root, text="汗中市龙港高级中学", command=lambda: handle_school_choice("3", start_event), font=("", 14)).pack(pady=5)

# 处理学校选择
def handle_school_choice(choice, start_event):
    if choice == "1":
        tk.Label(root, text="你选择了羊县中学。", font=("", 14)).pack(pady=10)
        event_1()
    elif choice == "2":
        tk.Label(root, text="你选择了闪西省汗中中学。", font=("", 14)).pack(pady=10)
        event_2()
    elif choice == "3":
        if start_event == event_list[2]:
            messagebox.showinfo("游戏结束", "你家境贫寒，直接破产了！\n游戏结束。")
            show_welcome()
        else:
            tk.Label(root, text="你选择了汗中市龙港高级中学。", font=("", 14)).pack(pady=10)
            event_3()

def event_1():
    for widget in root.winfo_children():
        widget.destroy()

    # 显示事件问题
    event_1_choice = random.choice(event_1_list)
    tk.Label(root, text=event_1_choice, font=("", 16), wraplength=500).pack(pady=20)

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
        tk.Button(root, text=value, command=lambda k=key: handle_event_1_choice(k, event_1_choice, results), font=("", 14)).pack(pady=5)

# 处理事件 1 的选择
def handle_event_1_choice(choice, event_1_choice, results):
    result = results[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_1_choice == event_1_list[0] and choice == "3") or (event_1_choice == event_1_list[2] and choice == "1"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        random_event()

def event_2():
    for widget in root.winfo_children():
        widget.destroy()

    # 显示事件问题
    event_2_choice = random.choice(event_2_list)
    tk.Label(root, text=event_2_choice, font=("", 16), wraplength=500).pack(pady=20)

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
        tk.Button(root, text=value, command=lambda k=key: handle_event_2_choice(k, event_2_choice, results), font=("", 14)).pack(pady=5)

# 处理事件 2 的选择
def handle_event_2_choice(choice, event_2_choice, results):
    result = results[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_2_choice == event_2_list[0] and choice == "1") or (event_2_choice == event_2_list[2] and choice == "3"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        random_event()

def event_3():
    for widget in root.winfo_children():
        widget.destroy()

    # 显示事件问题
    event_3_choice = random.choice(event_3_list)
    tk.Label(root, text=event_3_choice, font=("", 16), wraplength=500).pack(pady=20)

    # 根据事件显示选项
    if event_3_choice == event_3_list[0]:
        choices = {"1": "你选择了大声呼救。\n老师以为你有精神病，将你遣返回原籍。",
                   "2": "你选择了硬着头皮做。\n你考得很差，父母把你骂了一顿。",
                   "3": "你选择了把试卷撕了。\n老师夸你有胆量，并给你一套高考真题。"}
    elif event_3_choice == event_3_list[1]:
        choices = {"1": "你选择了巴结这位同学。\n你成为了ta的众多跟班之一。",
                   "2": "你选择了去看ta的父母是何方神圣。\nta的父亲对你说：好好学，争取以后能当上ta的秘书。",
                   "3": "你选择了偷拍ta家的车，并发布到网上。\n一封邮件让你删除视频，第二天你因为进教室先迈左脚被开除！"}
    elif event_3_choice == event_3_list[2]:
        choices = {"1": "你选择了先写作业。\n你写到熄灯时间也没写完。",
                   "2": "你选择了先洗澡。\n你感到很舒服，但是被没写作业的恐慌占据。",
                   "3": "你选择了去天台看夜景。\n班主任发现了你，让心理老师和你谈心一晚上。你很疲惫。"}
    else:
        return

    # 显示选项按钮
    for key, value in choices.items():
        tk.Button(root, text=f"选项 {key}", command=lambda k=key: handle_event_3_choice(k, event_3_choice, choices), font=("", 14)).pack(pady=5)

# 处理事件 3 的选择
def handle_event_3_choice(choice, event_3_choice, choices):
    result = choices[choice]
    messagebox.showinfo("结果", result)

    # 检查游戏结束条件
    if (event_3_choice == event_3_list[0] and choice == "1") or (event_3_choice == event_3_list[1] and choice == "3"):
        messagebox.showinfo("游戏结束", "游戏结束。")
        show_welcome()
    else:
        random_event()

def check_random_results(event, choice):
    if event["question"] == ">>>在宿舍流鼻血，你会？" and choice == "1":
        # 定义随机结果
        rd_30_results = [
            "流了几分钟就不流了，没事。",
            "你因失血过多进医院了！"
        ]
        # 根据权重随机选择结果
        result = random.choices(rd_30_results, weights=[0.6, 0.4])[0]
        messagebox.showinfo("随机结果", result)

        # 如果结果是严重后果，结束游戏
        if result == "你因失血过多进医院了！":
            messagebox.showinfo("游戏结束", "游戏结束！")
            show_achievements()
            root.quit()

used_event_indices = []

# 随机事件处理
def random_event():
    global last_event
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
            break

    event = random_events[idx]
    last_event = event

    # 显示事件问题
    tk.Label(root, text=event["question"], font=("", 16), wraplength=500).pack(pady=20)

    # 显示选项按钮
    for key, value in event["choices"].items():
        tk.Button(root, text=value, command=lambda k=key: handle_random_choice(event, k), font=("", 14)).pack(pady=5)

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
    tk.Label(root, text="你的成就", font=("", 20)).pack(pady=20)
    if achievements:
        for achievement in achievements:
            tk.Label(root, text=f"- {achievement}", font=("", 14)).pack(pady=5)
    else:
        tk.Label(root, text="你还没有获得任何成就。", font=("", 14)).pack(pady=5)
    tk.Button(root, text="返回主菜单", command=show_welcome, font=("", 14)).pack(pady=20)


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

# Version beta 0.3.0
# Designed by Still_Alive with Github Copilot and OpenAI ChatGPT
# Contributed by WaiJade with DeepSeek and KiMi
# 2025.04.13 12:09 China Standard Time
# Thank you for playing!