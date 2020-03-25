# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: dj_103.rpy
#  description: (story scripts) Dongji Main Story 10.3
#  Story Author: Alan Li
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dj_103:

label .s14villa:
    scene

    show text "2018年10月3日" at truecenter
    with dissolve
    pause 1

    scene bg s14villa
    with fade

    "- 清晨6:00 -"
    ming"出租车已经在路口那等候了，大家赶快点吧。"
    lian"走走，凑齐四个人就上车出发吧，千万别误船了。"
    shou"那个啥，诺诺还在化妆，大家先走吧……"
    conway"要化妆早点起啊！"
    shou"害，她四点就起来了，洗澡化妆鼓捣了现在……"
    "……""……"
    nuo"来了来了~~"
    "众人纷纷上了出租车，陆续出发。"


label .s15port:
    scene bg port
    with fade
    "车上你有些困倦不知不觉睡着了，等醒来已经到了码头。"
    "不知为何还不到七点的码头都已经熙熙攘攘了。"
    dan"为啥这么早就这么多人了？"
    me"奇怪，这不离早班还有好久吗？"
    zhuang"那我们先吃点早饭吧。"
    "众人寻觅了一会，找到了一家门上贴着封条痕迹的面馆。"
    "但老板热情的招呼了大家，看大家人多就让上二楼去吃面。"
    "虽然所谓的肉丝面只有几根肉丝、海鲜面也只有几个未知的贝类生物，但热腾腾的汤还是让大家十分满意。"
    "距离登船只有不到十五分钟了，你们决定去码头等着，也看看海景。"

label .s16port:
    "终于到了检票的时间……"
    yinyin"诶我怎么身份证刷不出来了过不了闸机"
    lian"我试试，诶好像也不行啊"
    yourong"我也不行诶？"
    shou"赶紧去咨询处问问？"
    "咨询处小姐姐""你们的票是早上六点半的啊，现在误船了。"
    "众人""什么！？"
    me"你们最早的班次不就是8：45这班吗？"
    "咨询处小姐姐""现在国庆增加了最早的6：30一班"
    "众人""……"
    "你赶紧给淘宝老板打电话，三次之后终于接通，说明情况之后，希望老板能帮忙解决一下问题。"
    "老板""你们自己误了船，出票信息就写的6.30，返程票已经下单了，那部分的钱也不可能退的。"
    me"谁知道你最上面这个6.30是什么意思，正常人写时间不都是6:30吗？"
    "老板""那没办法了。"
    "随即老板挂了电话，再也打不通。"
    default menuset = set()
    menu .s16port_ques:
        set menuset
        "你们该怎么办..."
        "mmp啊这可咋整，坑爹的淘宝老板，换个手机给他打":
            "果然换个手机号，淘宝老板接电话了，但刚没说两句，老板就又给挂掉了。"
            jump .s16port_ques

        "事情已经发生了，我们试试找码头工作人员求情":
            jump .s17port

        "算了自认倒霉吧，到舟山找个民宿打牌也挺好":
            $ dunhuang_value -= 10
            "你们在舟山找到了一家价格合适的小别墅。"
            # TODO: jump Label 57ghostTaxi
            jump dbgend

        "舟山到东极也不过是两个多小时船程，不如我们一起游过去吧":
            $ dunhuang_value += 30
            "你们一行十多人，经过十个小时的游泳，终于抵达了东极岛。"
            "当地媒体听说了你们的英勇行为，前来采访你们："
            "记者""你们为何一定要登岛呢？"
            "你们一起唱：东极岛啊东极岛啊 除了这里 我们哪儿都不想去……"
            jump .s24villa

label .s17port:
    "你们自动分成三波，大部队留在旁边查找舟山的酒店，一小部分在购票处排长队，你和另外几人准备找工作人员求情。"
    $ menuset = set()
    menu .s17port_ques:
        set menuset
        "找哪个工作人员呢？"
        "售票处忙碌着收钱卖票、操着本地口音的阿姨":
            "阿姨""排队去。"
            me"我们不是想买票"
            "阿姨""排队去。"
            me"我们..."
            "阿姨""排队去。"
            "……"
            jump .s17port_ques

        "咨询处非常同情我们遭遇、但表示无可奈何的的小姐姐":
            "小姐姐""是的我很同情你们这个遭遇，但是确实没有办法，船上也没有多的座位了。"
            jump .s17port_ques

        "检票处的看起来对我们有些兴趣、没事就瞅瞅我们的小哥":
            "小哥""以后要注意看官网的消息，不要走黄牛代购啊。"
            jump .s17port_ques

        "售票处管排队秩序的、胸前戴着党徽但说话有点凶的大叔":
            pass

    "大叔""现在确实船上没有空座位了，你们也看到了。"
    me"是...但我们大学生出来玩，实在没办法了，您能通融一下吗？"
    "大叔""你们每个人都有票对吧？"
    me"对，都是6:30的票"
    "大叔""当时买票花了多少钱？"
    me"每个人多了100代购费"
    "大叔""呵呵，你们先到旁边等着吧。" 
    "你们听不出来大叔语气中的意思，只好站到一边去了...."
    jump .s18port

label .s18port:
    ming"我们刚才看到了一个价格适合的酒店，还有一个套间目前空出。"
    han"套件确实适合我们去住。"
    menu:
        "这时你们准备怎么办？"
        "继续等着，但很担心酒店房间被别人抢定下来，先下单吧，就当花钱买保险了":
            $ dunhuang_value -= 10
            $ money += 200
            "携程上说这个酒店如果取消订单要亏两百块……"
            "还是订了吧。"
            
        "还是不等了，现在就下单直接去酒店吧":
            $ dunhuang_value -= 20
            "你们在舟山找到了一家价格合适的小别墅。"
            # TODO: jump Label 57ghostTaxi
            jump dbgend

        "想想还有什么骚操作":
            "小明突然意识到可以先给酒店打个电话，让他们给我们留着，结果发现酒店真的答应了"
            
    conway"刚才那个大叔最后问我们花多少钱买票是什么意思啊？"
    me"不会是想让我们给他点好处费吧？"
    "大家想了想觉得有道理。"
    lian"那么...大家有没有现金，四百五百块应该差不多？"
    "小老弟""我这有两百"
    yourong"我一点现金都没有"
    wqbh"我这三百"
    zheng"够了够了。"
    menu:
        "你准备："
        "当众“行贿”？？？这可不行，我们是新时代大学生，赶紧制止大家":
            $ dunhuang_value -= 20
            jump .s20port

        "五百块可能不够吧？他问我们花了多少代购费，我们竟然实话说了每人100，就算折半也得800吧":
            $ dunhuang_value += 10
            jump .s19port

        "可以先准备800现金准备好，先把400块放里面，如果他暗示不够，再把另外400补上":
            jump .s19port

label .s19port:
    "你包好了钱，再走到大叔面前。"
    "大叔""不是说了让你们在旁边等着吗？"
    menu:
        "你准备怎么说？"
        "“辛苦您了，这是我们的一点小心意”，说着把纸包递过去":
            pass

        "“那个...我们...想...这个...嗯...”":
            $ dunhuang_value -= 10

        "“你咋还没搞定啊，不就是想要钱吗？800块给你，我们时间很紧的，搞快点。”":
            $ dunhuang_value += 20

    "大叔""你们在干什么？说让你们在旁边等着就等着啊"

    "你们更加二丈和尚摸不到头脑。"
    zheng"难道是刚才做的太明显了 ，旁边这么多人，他没法收？"
    "陷入沉默..."
    "这时淫淫和兽兽终于排队到达了售票处，朝众人招手："
    shou"还需要买票吗？"
    me"有几张？"
    shou"3张"
    zheng"那还差得远啊……"
    lian"要不算了，同进退吧。"
    yinyin"嗯。"
    jump .s20port

label .s20port:
    "你们都回到大部队处。"
    han"这会卜文添他们应该起来了，要不给他们打个电话告诉他们这个好消息？"
    ming"是滴，他和小汪可以两个人住那么多房间了"
    yourong"哈哈哈万万没想到"
    dan"都怪我们忘记禁言诺诺了才误了船"
    nuo"狗屎"
    "……可能的解决方案几乎都试过，虽然都没走通，但气氛也因此轻松起来了。"
    "大家开始愉快的讨论这两天在舟山玩什么，以及如何举报这个黑心商家。"
    jump .s21port

label .s21port:
    "突然，大叔朝大家打招呼，你赶紧过去……"
    "大叔""你们每个人确实都有票是吗？"
    me"是的"
    "大叔""跟上级请示过了，说可以让你们用6:30的纸质票过检上船。"
    me"太棒了！！！谢谢您！"
    "大叔""但是没有座位哈，年轻人应该还行。拿着身份证去咨询处开纸质票吧。"
    me"没关系！谢谢大叔！！！奥利给！"
    "你们感到非常惊喜，满满的正能量！"

    "时间紧迫，距离开船还有五分钟，你们一行人赶紧去打印纸质票。"
    "但奇怪的是，淫淫等四人莫名其妙打印出了两张去程的船票，一张是6：30，另一张是14：30的。"
    menu:
        "你们准备？"
        "时间紧任务重，管他三七二十一，多开就拿着，先上了船再说":
            jump .s22ship

        "是你们系统的bug吧？我们有程序员，需不需要留下来协助你们修复系统？时薪很高的哦":
            $ dunhuang_value += 20
            "于是淫淫被留下来debug了，等到大家从东极回来，他把大家旅行的费用都挣回来了，表示“我土豪，我请客”"
            jump .s22ship

        "这个票不是我们买的，你们留下吧，可以送给有缘人":
            $ dunhuang_value += 10
            jump .s22ship

label .s22ship:
    scene bg s22ship
    with fade

    """
    终于，一顿操作猛如虎，你们竟然在五分钟内提着行李过安检上了船。
    
    果然没有座位了，你们只好回到货仓，在冷藏肉水果萝卜白菜可乐啤酒旁边安置了行李。
    
    船开了，大家吹着海风，回想起当年在密云螺旋稳赶火车的操作，不禁感慨。
    
    闲聊间，突然手机响了，原来是那个可恶的淘宝老板……
    """
    menu:
        "你准备？"
        "狗屎，你不是说不管我们了吗？怎么又来电话？接？接个p！":
            "众人纷纷说：“可以！”"
            "于是你怒挂了电话。"
            
        "接，大家轮流骂他一通":
            $ dunhuang_value += 10
            "众人纷纷口吐芬芳，但因为船上是在是太吵了，老板什么都没听到。"
            
        "接，跟他说明情况返程票不要退":
            "因为船上是在是太吵了，你们互相之间什么都没听到。"

    lian"还是跟他打字说一下吧，返程票千万别被他退掉了。"
    me"有道理。"
    "于是通过淘宝客服跟老板说明了现在的情况。"
    "过了一会儿……"
    "老板""你们是不是多取了四张票？"
    me"码头那边是多打了几张重复的。"
    "老板""那是我给你们买的，你们要补钱啊。"
    me"我们没有请宁给我们买票吧？宁当时直接挂电话，我们最终自行解决了上船的问题。"
    "老板""你们不补钱的话，小心返程还会出问题。"
    me"那你这是在威胁我们了？" 
    "老板""你们下船之后在对面码头问问能不能退。"
    me"多的票能退的话，我们会把钱还给你。但如果返程敢出问题，我们只好请平台介入了。"

    """
    一路在广阔的海平面上没有信号，好久没有这么惬意了。
    
    听着海浪和引擎的轰鸣声，不远的天空还飞着几只海鸥。
    
    大家分成三三两两吹海风聊天，连南靠在行李上睡着了……
    
    不知过了多久，船终于靠岸了，你们纷纷下船，民宿老板娘过来接你们。
    
    跟着老板娘，你们走在渔村的小路上，唱着东极岛岛歌：“东极岛 东极岛 我们不会离开你 生是你的老百姓 死是你的小精灵……”

    ……
    """
    jump .s24villa

label .s24villa:
    scene bg djvilla
    with fade
    "终于到了住宿的地方，原来是相距两百米的两栋民宅。"
    "于是你们决定，大的这栋作为闹腾活动场地，小的民宅作为晚上累了的人休息的地方。"
    $ menuset = set()
    menu .s24villa_ques:
        "距离上一顿早餐已经快七个小时了，你们准备："
        "让民宿老板帮忙介绍一家岛上正宗馆子":
            "老板""那你们可问对人了，到我朋友那去吧，保证实惠！"
            jump .s25restaurant

        "从舟山带过来了这么多食材，自己做吧！":
            wqbh"累死了！我不要做饭"
            "众人""任劳任怨的厨房大师傅主席要是在就好了"
            jump .s24villa_ques

        "冲冲冲，直接下海捞海鲜啊":
            $ dunhuang_value += 20
            "你们被渔民用渔网救了起来，当地媒体听说了你们的英勇行为，前来采访："
            "记者""请问你们为何一定要在东极岛亲自下海呢？"
            "你们一起唱：“东极岛啊东极岛啊 除了这里 我们哪儿都不想去……”"
            jump .s25restaurant

label .s25restaurant:
    scene bg dj_restaurant
    with fade
    "老板带着你们走到了海边的一家大排档，门口摆着各种活蹦乱跳的、不知名的海洋生物，1000元包席，保证海鲜过半管饱。"
    "你们立刻决定就在这家吃了，感受渔家的原始与新鲜。"
    conway"大家都客气点啊！我就不客气了。"

    menu:
        "桌上自然分为了两派，你是哪一派？"
        "不吃贝壳不吃虾，青椒肉丝西红柿鸡蛋是我的爱":
            "你很快加入了冠军、壮壮等人对家常菜的抢夺战，可恶的谭康威竟然一个人抢走了半盘青椒肉丝！"

        "海产怎么选？小孩子才做选择，成年人全都要":
            "这也太棒了吧，果然1000元海产几乎吃不完，啥都有了。"

    "风卷残云，不一会桌上就没剩什么菜了。"
    "这时卜文添突然说他们俩上岛了。"

    menu:
        "于是你们准备？"
        "赶紧吃完，一点都不给他们留！":
            pass

        "等他们来了再一起吃，让他们也摊钱哈哈哈哈哈哈":
            $ dunhuang_value += 20
            
    "不一会卜汪两人终于到了，听完我们讲述刚刚经历的传奇，感觉他们来岛实在是顺利。"
    ming"太久没吃过这么爽的海鲜了！"
    zhuang"我虚了，只能吃海草，这竟然没有鱼香肉丝。"
    nuo"我去，都三点了"
    conway"我们到石头那里拍个合影吧。"
    "众人进行了“东极”游客打卡沙雕合影，随后回民宿睡觉。"
    jump .s26villa

label .s26villa:
    scene bg dj_villa
    with fade
    """
    一觉睡的昏天暗地，起床都快六点了。

    喊醒众人，简单洗漱之后，你来到厨房，不知如何下手。
    
    万万没想到，小明竟然这次接替主席食堂大师傅的身份，担当了掌勺的重任，万千等人也纷纷下场做了几道炒菜。
    """
    han"你们这些老学姐怎么回事？怎么一个个的都不会做菜，还得人家学妹上场。"
    nuo"嘻嘻嘻嘻我会吃就行。"
    zheng"谁倒下垃圾啊，桶都装满了！"
    shou"专业倒垃圾的卜文添怎么还不来？"
    "……""……"
    jump .s27villa

label .s27villa:
    "而你和老板娘聊的非常投机。"
    "老板娘""其实我是专门跑到这里隐居的。"
    "难不成这是个富婆？？"
    "老板娘""这边生活真的很舒适，我也喜欢吃海鲜。我是北京人，北航毕业的，后来觉得工作没什么意思，就跑到东极岛开民宿了。"
    me"哇，北航吗这么厉害！"
    "老板娘""你们看起来也是大学生吧？什么大学？"
    me"什么大学都有23333我们是高中同学。"
    "……"
    "这时，连南正在和韩韩有容两位身高担当一起挂桃旗，找来找去终于决定悬挂到小院的面前，十分满意。"
    "老板娘""你们这个旗子是什么含义啊？"
    me"这是一个很长的故事了……"
    "……"
    "最终，老板娘表示相逢是缘，送你们一件东极岛特产的啤酒。"
    jump .s28villa

label .s28villa:
    "终于开饭了，仍然是依照传统“大樱桃的饭和菜”，所有人都不准坐下，抢菜的气氛一度非常愉悦。"
    "酒虽不足，但煮的十五包方便面十分管饱，果然最后吃不完。"
    menu:
        "于是你选择："
        "不如喂给他们家的斗牛犬狗不理！":
            "狗不理吃的很开心，但也只吃了一盆，还有半盆怎么办呢？"
            
        "不能浪费粮食，死撑也要撑进去！":
            $ dunhuang_value += 10
            "你们又坐下来继续吃，人多力量大，大家齐心协力把一盆分了，但还是剩下半盆。"
            
        "唉，只能倒掉了，没办法":
            $ dunhuang_value -= 10
            
    "唉没办法，只能倒掉了，可惜就可惜了。大家平时在海底捞可不是这个样子……"
    "大家开始很自觉地刷锅洗碗收拾桌子，各司其职。"
    "昏暗的灯光下，你看到这种景象感觉很美好。"
    "收拾完后已经十点半了，你们回到一个最大的房间。"
    jump .s29villa

label .s29villa:
    "你们决定开一个全员讨论会，告知大家淘宝船票店家的情况。"
    "在下午，你告知了船票老板，这边码头不给退票的情况，他却咬死要求你们把多买的那几张票的尾款补齐，不然威胁返程可能会出问题。"

    lian"这件事还比较严重，可能必须得我们全员讨论才能做决定了。"
    conway"嗯，其实说起来也简单，两个选择"
    menu:
        "这时你赞同哪一种呢？"
        "多花钱买平安，但出了不该出的钱，憋屈":
            $ dunhuang_value -= 20
            "但众人在各自发表看法之后，发现还是认为店家不敢动手脚的人居多。"
            "他们的理由也很有道理：台风即将来袭，如果他动手脚导致我们困在岛上，之后投诉他，甚至告他，他需要赔偿的就多了。"
            "于是你最终也赞同了这个观点。"

        "冒着风险，笃定他不敢在返程票上做手脚":
            $ dunhuang_value += 10
            "大部分人和你持有相同的观点：台风即将来袭，如果他动手脚导致我们困在岛上，之后投诉他，甚至告他，他需要赔偿的就多了。"
            
    "最终你们决定，跟老板说明情况，并以这个理由反威胁他，量他也不敢做手脚，之后不再接老板的电话。"

label .s30villa:
    "严肃的话题说完了，连南拿出祖传的两大盒UNO，这次有十几个人一起打，从来没有这么多过。"
    "都是熟练玩家了，游戏速度如同快了二倍速一般，完全应接不暇。"
    "不知过了多久，疯狂加四已经是老套路了，大家有点困了。"

    menu:
        "这时你说："
        "我们大家去睡觉吧！":
            $ dunhuang_value -= 20
            "大家说你不行，看日出前喊你。"
            "于是你去睡觉了，直到第二天凌晨四点多被喊醒。"
            # TODO: jump label 39villa2GetUp
            jump dbgend

        "对了，我记得上次淫淫说有个新玩法，我们可以试试！":
            pass

        "我们来换个活动，爱情保卫战吧！":
            jump .s31villa

    yinyin"对对对，可可跟我说了个很有趣的玩法。"
    yinyin"就是，不能说“他她它”这三个字。"
    "你们觉得很有意思，开始进行游戏了！"
    ming"啊？啥啥意思啊？"
    conway"你真是个憨批，不管你"
    menu:
        "于是你："
        "冠军好凶啊，还是给小明讲一下吧":
            me"就是，不能说“他她它”三个字。"
            "大家一起坏笑起来："
            "众人""冠军两张桃神三张！快摸！"
            "md原来小明在钓鱼！真是臭狗屎！"

        "冠军说得对，小明就是憨批":
            $ dunhuang_value += 10
            me"大家别管他，他就是憨批。"
            "大家一起坏笑起来："
            "众人""都要摸两张摸两张！哈哈哈哈……"
            "md原来小明在钓鱼！真是臭狗屎！"

        "虽然你也没太听懂规则，但还是默不作声吧……":
            $ dunhuang_value -= 10
            "于是淫淫又把规则讲了一遍。"
            "话音刚落，大家一起坏笑起来："
            "众人""摸三张摸三张！哈哈哈哈……"
            "原来小明在钓鱼。哈哈哈哈哈哈哈笑死我了我也想钓！"

    "欢声笑语中，大家都不敢说话，但又憋不住，随着大家手里的牌越来越多，全场笑做一片。"
    dan"坑爹小明，艾要明牌了！大家别看！"
    "艾是什么鬼？靠原来是英语啊"
    "真是一场诡异的污诺局！牌组的牌都几乎快被大家拿在手上，甚至可以比谁牌多了。"

    if dj_withgirl:
        # FIXME: This value need discussion
        if dj_girl_opinion > 80:
            # TODO: jump dj_girl label 12 girl message
            jump dbgend
        else:
            # TODO: jump dj_girl label 16 girl love
            jump dbgend
    else:
        jump .s31love

label .s31love:
    # TODO: complete here and remove this dbgend
    jump dbgend