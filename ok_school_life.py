import random

event_list = ['**你在一个富裕家庭**', '**你在一个普通家庭**', '**你在一个贫穷家庭**']
event_1_list = ['**第一周开家长会，校长讲话时间超出预计时间一小时，导致放学时间延迟，你会？',
                '**面对单休制，你开始了怎样的思考？',
                '**看到学校的电梯，你会怎么做？',]
event_2_list = ['**军训时你感到身体不适，你会？',
                '**社团招新，你会？',
                '**舍友睡觉呼噜声很大，你会？',]
event_3_list = ['**开学考试，你发现试题很难，你选择？',
                '**看到有同学乘坐黑色高级车，你会？',
                '**放学后时间很紧，你选择？',]
random_event_list = ['**你在学校的食堂吃饭，发现菜品很差，你会？',
                     '**你在学校的图书馆借书，发现没有你想要的书，你会？',
                     '**你在学校的操场上看到同学们打篮球，你会？',
                     '**你在学校的实验室里做实验，发现实验器材损坏，你会？',
                     '**你在学校的宿舍里，发现室友总是打游戏，你会？',
                     '**你在学校的教室里，发现同学们在讨论考试作弊，你会？',
                     '**考试：sin x = cos ____？',
                     '**考试：sin 2x = ____？',
                     '**考试：中国历史上的第一位皇帝是？',
                     '**考试：tan x/2的周期是？',
                     '**你和同学对比国摇和欧美摇滚，你会选择？',
                     '**有同学组建“觉醒者联盟”，你选择？',
                     '**你在学校的社团中，发现社团活动不符合你的兴趣，你会？',
                     '**班里有同学玩原神，你会？',
                     '**班里有同学玩LOL，你会？',
                     '**今天早自习突然检查仪容仪表，你的头发被老师点名批评“不合规范”，你会？',
                     '**英语老师心血来潮临时宣布要测一张听写卷，你昨晚偏偏没背单词，你会？',
                     '**学校食堂推出“健康套餐”，但卖相一般，你中午来到食堂，面对它，你会？',
                     '**你被班主任安排参加1500米长跑选拔，你内心抗拒但又怕被扣分，你会？',
                     '**老师打开PPT，念稿40分钟，语速极慢，字还特别小。你会？',
                     '**放学时突然下起大雨，你没带伞，你会？',
                     '**你这周要负责扫地，但今天作业太多，你想偷个懒。你会？',
                     '**地理课，老师问：同学们，你们猜我是我们老李家第几代教书匠？',
                     '**遇到老师，你选择低头.老师走近问你为什么不给她打招呼。你会？',
                     '**校园传奇浴室，看到一群烟哥在吸烟，你会？',
                     '**在考试的时候，你有点在意的女子坐在你旁边考试，你会？',
                     ]
last_event = None

def start():
    print("欢迎来到OK School Life beta v0.2！")
    print("你将经历不同的事件和选择，看看你的学校生活会如何发展。")
    tostart = input("按“1”以开始游戏，按“2”以退出：")
    if tostart == "1":
        print("游戏开始！")
        main()
    elif tostart == "2":
        print("感谢游玩，期待下次再见！")
        sys.exit()
    else:
        print("无效的输入，请重新输入。")
        start()

def main():    
    start_event = random.choices(event_list, weights=[0.2, 0.5, 0.3])[0]
    print(f"{start_event}。\n你中考考得很好，现在可以选择学校。")
    print("1.羊县中学")
    print("2.闪西省汗中中学")
    print("3.汗中市龙港高级中学")
    
    while True:  # 使用循环代替递归
        choice = input("请选择你要去的学校（输入数字）：")
        if choice == "1":
            print("你选择了羊县中学。")
            event_1()
            break
        elif choice == "2":
            print("你选择了闪西省汗中中学。")
            event_2()
            break
        elif choice == "3":
            print("你选择了汗中市龙港高级中学。")
            if start_event == event_list[2]:
                print("你家境贫寒，直接破产了！\n游戏结束。")
                exit()
            event_3()    
            break
        else:
            print("无效的选择，请重新输入。")

def event_1():
    for event_1_choice in event_1_list:
        print(f"{event_1_choice}")
        if event_1_choice == event_1_list[0]:
            print("1.继续听演讲\n2.请假回家\n3.向老师投诉")
            choices = {"1": "你选择了继续听演讲。\n演讲结束后，你感到很疲惫。",
                   "2": "你选择了请假回家。\n你被家长骂了。",
                   "3": "你选择了向老师投诉。\n你失败了。老师难道能管校长的事？"}
        elif event_1_choice == event_1_list[1]:
            print("1.符合无钱补课者的利益\n2.不合理的制度\n3.有的学校两周一放，知足常乐")
            choices = {"1": "你选择了符合无钱补课者的利益。\n你感到很开心。",
                   "2": "你选择了不合理的制度。\n你开始对此抱有异见。",
                   "3": "你选择了有的学校两周一放，知足常乐。\n你感到压抑且自由。"}
        elif event_1_choice == event_1_list[2]:
            print("1.乘坐电梯\n2.走楼梯\n3.不管")
            choices = {"1": "你选择了乘坐电梯。\n你违反了学生条例，游戏失败。",
                   "2": "你选择了走楼梯。\n你感到很累。",
                   "3": "你选择了不管。\n好像什么也没有发生。"}
        else:
            return

        while True:
            choice = input("请选择（输入数字）：")
            if choice in choices:
                print(choices[choice])           
                if event_1_choice == event_1_list[0] and choice == "3" or \
                   event_1_choice == event_1_list[2] and choice == "1":
                   print("游戏结束。")
                   exit()
                break
            else:
                print("无效的选择，请重新输入。")
    random_event()

def event_2():
    for event_2_choice in event_2_list:
        print(f"{event_2_choice}")
        if event_2_choice == event_2_list[0]:
            print("1.烈日下硬撑着\n2.向老师说明\n3.大声呵斥军训不人性化")
            choices = {"1": "你选择了烈日下硬撑着。\n你中暑进医院了！",
                       "2": "你选择了向老师说明。\n老师夸你勇敢，让你休息了。",
                       "3": "你选择了大声呵斥军训不人性化。\n你被教官骂了一顿，心情很不好。"}
        elif event_2_choice == event_2_list[1]:
            print("1.加入社团\n2.不加入社团\n3.向老师举报")
            choices = {"1": "你选择了加入社团。\n你感到很开心。",
                       "2": "你选择了不加入社团。\n你感到很无聊。",
                       "3": "你选择了向老师举报。\n老师告诉你这是正常操作。"}
        elif event_2_choice == event_2_list[2]:
            print("1.忍耐\n2.向老师投诉\n3.把舍友打一顿")
            choices = {"1": "你选择了忍耐。\n你整晚没睡好，你很烦躁。",
                       "2": "你选择了向老师投诉。\n老师告诉你这是正常现象，你很无奈。",
                       "3": "你选择了把舍友打一顿。\n你因违反校规被开除！"}
        else:
            return

        while True:
            choice = input("请选择（输入数字）：")
            if choice in choices:
                print(choices[choice])           
                if event_2_choice == event_2_list[0] and choice == "1" or \
                   event_2_choice == event_2_list[2] and choice == "3":
                   print("游戏结束。")
                   exit()
                break
            else:
                print("无效的选择，请重新输入。")
    random_event()

def event_3():
    for event_3_choice in event_3_list:
        print(f"{event_3_choice}")
        if event_3_choice == event_3_list[0]:
            print("1.大声呼救\n2.硬着头皮做\n3.把试卷撕了")
            choices = {"1": "你选择了大声呼救。\n老师以为你有精神病，将你遣返回原籍。",
                       "2": "你选择了硬着头皮做。\n你考得很差，父母把你骂了一顿。",
                       "3": "你选择了把试卷撕了。\n老师夸你有胆量，并给你一套高考真题。"}
        elif event_3_choice == event_3_list[1]:
            print("1.巴结这位同学\n2.去看ta的父母是何方神圣\n3.偷拍ta家的车，并发布到网上")
            choices = {"1": "你选择了巴结这位同学。\n你成为了ta的众多跟班之一。",
                       "2": "你选择了去看ta的父母是何方神圣。\nta的父亲对你说：好好学，争取以后能当上ta的秘书。",
                       "3": "你选择了偷拍ta家的车，并发布到网上。\n一封邮件让你删除视频，并且你因为进教室先迈左脚被开除！"}
        elif event_3_choice == event_3_list[2]:
            print("1.先写作业\n2.先洗澡\n3.去天台看夜景")
            choices = {"1": "你选择了先写作业。\n你写到熄灯时间也没写完。",
                       "2": "你选择了先洗澡。\n你感到很舒服，但是被没写作业的恐慌占据。",
                       "3": "你选择了去天台看夜景。\n班主任发现了你，让心理老师和你谈心一晚上。你很疲惫。"}
        else:
            return

        while True:
            choice = input("请选择（输入数字）：")
            if choice in choices:
                print(choices[choice])           
                if event_3_choice == event_3_list[0] and choice == "1" or \
                   event_3_choice == event_3_list[1] and choice == "3":
                   print("游戏结束。")
                   exit()
                break
            else:
                print("无效的选择，请重新输入。")
    random_event()


def random_event():
    # 使用全局变量记录上一次的随机事件
    global last_event
    random_event_choice = random.choice(random_event_list)
     # 确保新事件与上一次的事件不同
    while random_event_choice == last_event:
        random_event_choice = random.choice(random_event_list)

    # 更新 last_event 为当前事件
    last_event = random_event_choice
    print(f"{random_event_choice}")
    if random_event_choice == random_event_list[0]:
        print("1.继续吃饭\n2.投诉\n3.罢吃")
        choices = {"1": "你选择了继续吃饭。\n你感到很失望。",
                   "2": "你选择了投诉。\n你被老师骂了，心情很不好。",
                   "3": "你选择了罢吃。\n你因颠覆学校而被开除，你失败了！。"}
    elif random_event_choice == random_event_list[1]:
        print("1.继续借书\n2.去找老师\n3.大声辱骂学校藏书不够")
        choices = {"1": "你选择了继续借书。\n你感到很失望。",
                   "2": "你选择了去找老师。\n老师告诉你没有书。",
                   "3": "你选择了大声辱骂学校藏书不够。\n你被年级主任骂了一顿，心情很不好。"}
    elif random_event_choice == random_event_list[2]:
        print("1.加入这些人\n2.拍照发朋友圈\n3.去打篮球")
        choices = {"1": "你选择了加入这些人。\n这些人嘲笑你打得太菜，你心情很不好。",
                   "2": "你选择了拍照发朋友圈。\n你喜欢的女生/男生看到了，问你要了照片。",
                   "3": "你选择了去打篮球。\n你感到很开心。"}
    elif random_event_choice == random_event_list[3]:
        print("1.修理实验器材\n2.不管\n3.向老师报告")
        choices = {"1": "你选择了修理实验器材。\n实验器材修好了，你受到老师的赞赏。",
                   "2": "你选择了不管。\n氯气泄漏，你中毒了！游戏结束。",
                   "3": "你选择了向老师报告。\n。老师告诉你没事。"}
    elif random_event_choice == random_event_list[4]:
        print("1.向班主任举报\n2.向年轻老师举报\n3.和室友商量")
        choices = {"1": "你选择了向班主任举报。\n他们知道后，叫一群人把你打了一顿！",
                   "2": "你选择了向年轻老师举报。\n老师告诉你这是个人隐私。",
                   "3": "你选择了和室友商量。\n你们决定一起打游戏。"}
    elif random_event_choice == random_event_list[5]:
        print("1.加入他们\n2.拍照发朋友圈\n3.忽视")
        choices = {"1": "你选择了加入他们。\n你们一起作弊，被校长发现。你被开除了！",
                   "2": "你选择了拍照发朋友圈。\n校长看到了，表扬你的举报行为，并没收了你的手机。",
                   "3": "你选择了忽视。\n他们这次都比你考得高，你很难过。"}
    elif random_event_choice == random_event_list[6]:
        print("1.x + π\n2.x - π/2\n3.x + π/2")
        choices = {"1": "你选择了x + π。\n你错得太离谱，被开除了！",
                   "2": "你选择了x - π/2。\n你过关！。",
                   "3": "你选择了x + π/2。\n你考得很差，父母把你骂了一顿。"}
    elif random_event_choice == random_event_list[7]:
        print("1.2(sinx)(cosx)\n2.π\n3.2x")
        choices = {"1": "你选择了2(sinx)(cosx)。\n你过关！",
                   "2": "你选择了π。\n你错得太离谱，被开除了！",
                   "3": "你选择了2x。\n你考得很差，父母把你骂了一顿。"}
    elif random_event_choice == random_event_list[8]:
        print("1.泰始皇\n2.夏禹\n3.以上都不是")
        choices = {"1": "你选择了泰始皇。\n你错得太离谱，被开除了！",
                   "2": "你选择了夏禹。\n你考得很差，父母把你骂了一顿。",
                   "3": "你选择了以上都不是。\n你得到了全班最高分，你感到很开心。"}
    elif random_event_choice == random_event_list[9]:
        print("1.x\n2.π/2\n3.2π")
        choices = {"1": "你选择了x。\n你错得太离谱，被开除了！游戏结束。",
                   "2": "你选择了π/2。\n你考得很差，父母把你骂了一顿。",
                   "3": "你选择了2π。\n你过关！"}
    elif random_event_choice == random_event_list[10]:
        print("1.国摇好\n2.欧美摇滚好\n3.尊重对方喜好")
        choices = {"1": "你选择了国摇好。\n对方给你唱了一首《大石碎胸口》的尾奏。",
                   "2": "你选择了欧美摇滚好。\n对方给你唱了一首《Stairway to Heaven》的前奏。",
                   "3": "你选择了尊重对方喜好。\n你们愉快地交流了意见。"}
    elif random_event_choice == random_event_list[11]:
        print("1.当普通成员\n2.当宣传部长\n3.向老师举报")
        choices = {"1": "你选择了当普通成员。\n你们整天针砭时弊，成绩都下降了。",
                   "2": "你选择了宣传部长。\n东窗事发，你被警察调查后被学校开除了！",
                   "3": "你选择了向老师举报。\n老师夸赞你有独立头脑。"}
    elif random_event_choice == random_event_list[12]:
        print("1.继续待在社团\n2.退社并不加入其他社团\n3.跳槽喜欢的社团")
        choices = {"1": "你选择了继续待在社团。\n你每周最烦恼的时刻就是社团课的40分钟。",
                   "2": "你选择了退社并不加入其他社团。\n你将社团时间又来学习，成绩猛涨。",
                   "3": "你选择了跳槽喜欢的社团。\n你得到了快乐，但是成绩下降了。"}
    elif random_event_choice == random_event_list[13]:
        print("1.和他整天讨论\n2.背后说他是OP\n3.当面说他是OP")
        choices = {"1": "你选择了和他整天讨论。\n你们很开心，但是成绩下降了。",
                   "2": "你选择了背后说他是OP。\n你们的友谊破裂了。",
                   "3": "你选择了当面说他是OP。\n他叫来一群同好，打了你一顿。你失败了！"}
    elif random_event_choice == random_event_list[14]:
        print("1.和他讨论喜欢的英雄\n2.对他说不如王者荣耀\n3.无视他的存在")
        choices = {"1": "你选择了和他讨论喜欢的英雄。\n你们很开心，但是成绩下降了。",
                   "2": "你选择了对他说不如王者荣耀。\n他叫来一群同好，打了你一顿。你失败了！",
                   "3": "你选择了无视他的存在。\n你深知学习最重要，考到了年级前20."}
    elif random_event_choice == random_event_list[15]:
        print("1.当场认错，说以后注意\n2.小声反驳，说这是个人风格\n3.大声吐槽老师审美落后")
        choices = {"1": "你选择了当场认错，说以后注意。\n老师夸你知错就改，给你加了分。",
                   "2": "你选择了小声反驳，说这是个人风格。\n老师很生气，在年级主任的陪同下教育了你一顿。",
                   "3": "你选择了大声吐槽老师审美落后。\n老师叫来了你的家长谈话，你被停课了。"}
    elif random_event_choice == random_event_list[16]:
        print("1.硬着头皮上\n2.装病逃课\n3.向学霸借速成小抄")
        choices = {"1": "你选择了硬着头皮上。\n你考得很差，老师让你第二天重新默写。",
                   "2": "你选择了装病逃课。\n你被老师发现了，心情很不好。",
                   "3": "你选择了向学霸借速成小抄。\n你考得很好，你感到很开心。"}
    elif random_event_choice == random_event_list[17]:
        print("1.咬咬牙尝试一下，毕竟健康\n2.去小卖部买泡面\n3.拍照发群吐槽，带头抵制")
        choices = {"1": "你选择了咬咬牙尝试一下\n非常难吃，使你下午的体育课反胃想吐。",
                   "2": "你选择了去小卖部买泡面。\n你感到很开心，但你被老师发现了，罚你写检查。",
                   "3": "你选择了拍照发群吐槽，带头抵制。\n你涉嫌颠覆学校食堂罪，被开除了！"}
    elif random_event_choice == random_event_list[18]:
        print("1.勉强上阵，全力跑完\n2.故意跑慢，装作不擅长\n3.提前和体育委员套好话，直接弃权") 
        choices = {"1": "你选择了勉强上阵，全力跑完。\n你跑到缺氧，进医院了。",
                   "2": "你选择了故意跑慢，装作不擅长。\n你被老师骂了，心情很不好。",
                   "3": "你选择了提前和体育委员套好话，直接弃权。\n你感到很开心，但是一部分同学对你议论纷纷。"}
    elif random_event_choice == random_event_list[19]:
        print("1.努力集中精神，坚持到底\n2.大声呵斥老师\n3.偷偷写作业，节省时间")
        choices = {"1": "你选择了努力集中精神。\n你感到很脑神经衰弱，视线模糊。",
                   "2": "你选择了大声呵斥老师。\n老师请来了你的家长，让你停课了！",
                   "3": "你选择了偷偷写作业，节省时间。\n你被老师发现了，老师把你的作业撕了。"}
    elif random_event_choice == random_event_list[20]:
        print("1.借同学的伞，送一段路再跑回家\n2.淋雨冲回家，冲凉省了\n3.在校门口避雨，顺便反思为何不看天气预报")
        choices = {"1": "你选择了借同学的伞。\n虽然花了点时间，但是安全回家了。",
                   "2": "你选择了淋雨冲回家，冲凉省了。\n你第二天就发烧了，无法继续学习！",
                   "3": "你选择了在校门口避雨，顺便反思为何不看天气预报。\n你在风雨中多想了很多，也许成长就是这样被迫发生的。"}
    elif random_event_choice == random_event_list[21]:
        print("1.找朋友帮忙，周末请ta喝饮料\n2.装作忘记，等老师点名再说\n3.拖延去扫，边扫边抱怨制度不合理")
        choices = {"1": "你选择了找朋友帮忙。\n朋友满脸不情愿，但还是答应了。这种人情债，你记在心里了。",
                   "2": "你选择了装作忘记。\n老师点名了，你被扣分了。",
                   "3": "你选择了边扫边抱怨制度不合理。\n你涉嫌颠覆学校制度罪，被开除了！"}
    elif random_event_choice == random_event_list[22]:
        print("1.你是老李家第二代教书匠\n2.你是老李家第三代教书匠\n3.你是老李家第四代教书匠")
        choices = {"1": "你选择了你是老李家第二代教书匠。\n老师冷笑着说：你低估了我们的家族实力。",
                   "2": "你选择了你是老李家第三代教书匠。\n老师说：我不是第三代教书匠，但我是三分之一。",
                   "3": "你选择了你是老李家第四代教书匠。\n老师说夸你聪明，给你加了分。"}
    elif random_event_choice == random_event_list[23]:
        print("1.低头\n2.微笑\n3.说：我没有看到人")
        choices = {"1": "你选择了低头。\n老师说：下次记得打招呼。",
                   "2": "你选择了微笑。\n老师看你无奈，原谅了你。",
                   "3": "你选择了说：我没有看到人。\n老师生气地说：我不是人吗？请来了你的家长。"}
    elif random_event_choice == random_event_list[24]:
        print("1.私下向校长举报\n2.直接开骂\n3.微笑着说：我也来一根\n4.无视")
        choices = {"1":"你选择了私下向校长举报。\n校长高度赞赏你的行为，并在大会上让你上台领奖。",
                   "2": "你选择了直接开骂。\n烟哥一人一根烟头把你烫没了！",
                   "3": "你选择了微笑着说：我也来一根。\n你们一起吸烟，被老师发现了，心情很不好。",
                   "4": "你选择了无视。\n好像什么也没有发生。"}
    elif random_event_choice == random_event_list[25]:
        print("1.毫不在意，纯西格玛\n2.看看她做题做到哪了\n3.问问她这道题怎么做\n4.站起来大声说你要换座位")
        choices = {"1":"你选择了毫不在意，做西格玛真男人。\n你冷静发挥，这次考试考的很好，你在下一次考试坐的离她很远。",
                   "2": "你选择了看看她做题做到哪了。\n你发现她已经做到第二面了，而你还在第一面，你汗流浃背，不停擦汗，你考的很差，你在下一次坐的离她很远。",
                   "3": "问问她这道题怎么做\n作弊被老师发现，老师给你的卷子做了标记，这科变成了0分，你在下一次坐的离她很远。",
                   "4": "你选择了站起来说你要换座位\n老师拒绝了你，并且班级上出现了你的流言，你觉得很不舒服。"
                   }
    else:
        return
    
    while True:
        choice = input("请选择（输入数字）：")
        if choice in choices:
            print(choices[choice])
            if random_event_choice == random_event_list[0] and choice == "3" or \
                random_event_choice == random_event_list[3] and choice == "2" or \
                random_event_choice == random_event_list[4] and choice == "1" or \
                random_event_choice == random_event_list[5] and choice == "1" or \
                random_event_choice == random_event_list[6] and choice == "1" or \
                random_event_choice == random_event_list[7] and choice == "2" or \
                random_event_choice == random_event_list[8] and choice == "1" or \
                random_event_choice == random_event_list[9] and choice == "1" or \
                random_event_choice == random_event_list[11] and choice == "2" or \
                random_event_choice == random_event_list[13] and choice == "3" or \
                random_event_choice == random_event_list[14] and choice == "2" or \
                random_event_choice == random_event_list[15] and choice == "3" or \
                random_event_choice == random_event_list[17] and choice == "3" or \
                random_event_choice == random_event_list[18] and choice == "1" or \
                random_event_choice == random_event_list[19] and choice == "2" or \
                random_event_choice == random_event_list[20] and choice == "2" or \
                random_event_choice == random_event_list[21] and choice == "3" or \
                random_event_choice == random_event_list[23] and choice == "3" or \
                random_event_choice == random_event_list[24] and choice == "2":
                print("游戏结束。")
            else:
                random_event()
            break
        else:
            print("无效的选择，请重新输入。")

start()

# Version beta 0.2.4
# Designed by Still_Alive with Github Copilot
# Contribued by WaiJade with his brain
# 2025.04.06 12:44