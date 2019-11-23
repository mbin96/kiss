# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define f = Character('김성아', color="#c833c8")
define b = Character('이은혁', color="#ff00c8")
define q = Character('???', color="#005fc8")
define c = Character('괴물', color="#5555c8")
$renpy.layer.at_list(shake, "master")
transform duribun :
    linear 0.1 xzoom -1 
    xalign 0.6
    time 0.4
    linear 0.1 xzoom 1 
    xalign 0.5

    
transform goRight :
    linear 0.5 xalign 1.0 
transform standUp :
    yzoom 0 
    linear 0.5 yzoom 1

transform right_ :
    xalign 0.7

transform left_ :
    xalign 0.2

transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0
    
# 여기에서부터 게임이 시작합니다.



label start:

    "어느날 서울에 정체모를 폭탄이 떨어진뒤"
    "그날 이후 한국은 멸망했다."
    "이것은 멸망의 이야기"
    scene bg subway 
    with fade
    show f idle
    with dissolve
    play music "audio/A_happy.mp3" fadein 2
    "내 이름은 김성아. 의과를 진학중인 대학생으로, 오늘도 여느때와 같이 대학교에 등교중이다."
    f "으아... 지친다 지처. 오늘도 지하철엔 사람이 많네."
    "여느때와 같이 지하철을 타고 건대입구 역에서 내린뒤 학교로 걸어가는 평범한 일상."
    "오늘은 조금 다른길로 가볼까?"
    menu :
        "여느때와 같이 건대입구에서 내린다. ": #badend
            f "그냥 평소랑 똑같이 가자"
            stop music fadeout 2
            hide f
            "그렇게 매일매일과 같은 평범한 일상을 보냈다."
            jump badend_boom
            return

        "오늘은 구의역에서 내려서 간다." : # keepgoing
            f "오늘은 구의역으로 가보자. "

    scene bg backstreet
    with fade
    show f panic
    with dissolve

    "구의 역에서 내려, 길을 건너고 구청을 지나 골목길로 들어갔다."
    "그런데 골목길에서 학교로 들어가는 문이 나와야 할텐데 길을 잘못들은걸까?"
    "학교는 커녕 낡은 빌라와 단독주택뿐이다."
    show f panic at duribun

    f "어떡해... 길 잃어 버렸나봐..."
    "학교로 가는길이 대체 어딜까?"
    play music "audio/A_scared.mp3" fadeout 2
    "그런데 골목길 한쪽 건물에서 괴기한 소리가 나는것 같다."
    q "그어어어......"

    show f scared at shake

    "괴기한, 소름끼치는 소리다."
    "누군가 다치기라도 한걸까? 아니면 다른 무언가...?"
    
    menu :
    
        "-그 건물에 가본다":
            show f scared at goRight
            "호기심이 동한 나는 그만, 끌리듯 그 건물로 발걸음을 옮겼다."
        "-가보지 않는다.":
            f "신경 쓰지말자. 학교에 가는게 우선이지."
            stop music fadeout 2
            hide f
            "그렇게 겨우 지각을 면한 나는 수업을 듣느라 정신없이 하루를 보냈다."
            jump badend_boom

    
    #blackout
    scene bg bf with dissolve
    "그 건물 지하에 있었던것은"
    #bg creature
    "형체를 알아볼수 없는 괴물이였다."
    show none with dissolve
    pause 3
    scene bg caffe

    show f scared
    with dissolve

    "겨우 괴물이 있던 건물을 빠져나왔다."
    "방금 본건 도대체 뭐지? 세상에 저런 동물이 있었던가? 내눈으로 본게 도저히 믿어지지 않는다."
    "후들후들 거리는 다리를 겨우 진정시키고 카페에 들어가 앉았다."
    "이제서야 조금 머리가 돌아가는것 같다. 방금 본 괴물은 분명 시람의 형태와 흡사했다."
    "마치 사람이 괴물로 변한듯한......"
    "이거 혹시..."
    "설마? 아냐... 아닐꺼야..."
    "나는 연락처를 뒤져 1년 만에 오빠에게 전화를 걸었다."
    "뚜루루"
    "뚜루루"
    show f at left_ with move
    show b smile at right 
    show b smile at right_ 
    with dissolve
    b "여보세요? 뭐야 너가 연락을 다하고."
    "여느때와 같은 활기찬 목소리."
    f "오빠. 긴말 안할께. 오늘 건물 지하에 있는 괴물을 봤어."
    f "혹시 이거... 오빠가 낸 연구에 나온 그거 아니지? 아닌거지?"
    show b idle
    b "..."
    "수화기 너머로 긴침묵이 흘렀다."
    f "오빠! 오빠!!! 말좀해!"
    "긴 침묵을 깨고 나온 말은 "
    b "나도... 이렇게 될줄 몰랐어"
    "너무나 절망적이였다."
    b "이젠 더이상 나도 막을 방법이 없어."
    "뚝"
    hide b
    show f at center with move
    "전화를 끊었다. "
    "이제 어떡해야 할까."
    "이제 곧 세상은 멸망할꺼다."
    "멸망을 알지만 나는 어찌할수 없다는 냉혹한 현실에 무력감에 빠졌다."
    "그건 평범한 괴물이 아니였다."
    "분명 그건..."
    "사람이 유전자 변형 당해 만들어진 괴물이다."
    stop music fadeout 2
    scene none
    "1년전 유전공학계의 파장을 불러온 논문이 있었다."
    "방금 전화한 사람은 이은혁, 천재 신동으로 불리며 대학을 17살에 졸업하고 지금은 박사과정을 밟는 대학원생으로"
    "일년전 이은혁이 발표한 논문은 사람의 유전자를 변형시켜, 신체능력을 놀랍게 변형시킬수 있다는 논문이였다."
    "세상은 뒤집혔고, 곧 사람을 대상으로 했다는 윤리적인 비판과 터무니 없는 연구결과에 관한 진실공방이 벌어졌다."
    "아마도 저 괴물은, 그 연구에 의해 만들어 졌을꺼다."
    "누군가 괴물을 이용하려 한다면 세상은 멸망하겠지. "
    "일단 오늘은 집에 들어가자."

    #black out
    pause 2

    scene bg konkuk
    show f idle
    play music "audio/A_emergency.mp3"
    "몇일뒤, 여느때처럼 등교하던날."
    "서울 하늘에 무언가 떨어졌고 폭발했다."
    "눈이 부시도록 빛나더니 갑자기 주변의 사람들이 이상해졌다."
    "피를 토하거나, 입에 이상한 빛깔의 거품을 물고 쓰러진 사람들."
    "그중 일부는 다시 일어나는가 싶더니"
    q "크와아아악"
    show f scared at shake
    "이상한 소리와 함께 나를 향해 달려오기 시작했다."
    f "꺅!"
    "나를 향해 달려오는 사람을 겨우 피하고 보니, 다른 사람들도 모두 이상해져있었다."
    "빨리 이곳을 도망가야 한다"
    "어떻게 하지?"
    menu :
        "공과 대학 강의실에 들어간다.":
            scene bg classroom
            show f scared
            "공대의 빈 강의실로 들어가 문을 걸어 잠궜다."
            
    
    "저번에 괴물을 본 이후 이런 일이 일어날것 같다는 생각은 했지만 이렇게 일찍 벌어질 꺼라고는 생각도 못했다."
    f "아으..아아으아..아..."
    stop music fadeout 2
    show blackout1
    "의식이 점점 흐려진다."
    "나도 괴물이 되는걸까"
    show none with dissolve
    pause 3
    #black out

    q "...야..정..려"
    scene bg classroom
    show blackout1
    with dissolve
    "뭐지"
    "여긴 사후세계인걸까?"
    q "..아 정신...려...성아야!"
    b "성아야 정신좀 차려!"
    show b angry with dissolve
    
    "다행히 사람 얼굴이 보이는걸 보니 죽은건 아닌가보다."
    f "누구...세요?"
    "누군지 모를사람이 나를 열심히 깨우고 있었다. 아까 본 일들이 다 꿈이였으면"
    b "나야 은혁이"
    hide blackout1
    
    show b angry at right_ with move
    show f idle at left 
    show f idle at left_ 
    with dissolve
    
    "익숙한 이름에 갑자기 정신이 번쩍하고 들었다."
    f "오빠?!"
    show b idle
    b "성아야 정신이 좀 드니?"
    f "응 어어... 뭐 무슨일이야 여긴 어디지?"
    "왜 은혁 오빠가 앞에 있는걸까? 날 구하러 온것 같은데"
    b "너 구해주러 왔어. 여긴 아직 학교 교실이야"
    b "지금 빨리 밖으로 나가야해. 여긴 위험해"
    "역시 아까본건 꿈이 아니였나보다."
    "사람들은 다 괴물이 되어버린걸까? 나는 왜 안변한거지?"
    menu :
        "-오빠를 따라간다." :
            "머리속이 혼란스러웠지만, 일단 오빠를 따라 가자"
        "-오빠를 믿을수 없다. 따라가지 않는다." : #badend
            jump badend_ee
    scene bg gonghak
    with fade
    show b idle at right
    show b idle at right_
    show f idle at left 
    show f idle at left_ 
    with dissolve
    play music "audio/A_emergency.mp3"

    "교실밖으로 나와 공대를 벗어나니 앞엔 괴물들이 돌아다니고 있었다. 시선을 옆으로 돌리자 빠루를 든 오빠가 보인다."
    show f scared
    f "오빠... 저게 대체 뭐야?"
    b "내가 1년전에 발표했던 연구 기억나?"
    "그걸 잊었을리 없잖아. 그렇게 난리가 났었는데. "
    b "그 연구가 발표되고 난 엄청난 논란과 비난에 휩싸였었어"
    b "너에게서도 연락이 끊겼고."
    f "미...미안..."
    "아니 연락좀 안할수도 있지 쪼잔하게"
    b "어쨌든 그 이후에 군관계자가 찾아왔어. 연구에 대해 흥미가 있다면서 지원을 해준다고 말이야."
    b "군대에서 신체 강화에 쓰려는 목적 정도일꺼라고 생각한 나는, 제안을 받아들이고 내 연구자료를 제공했고, 지원을 받아 연구를 지속해 나갔어"
    b "그런데 한달 전 쯤이였을까, 인터넷에 신체 일부가 이상해진 사람들이 목격되었다는 소문이 들려오기 시작했지."
    b "너도 알잖아? 내연구의 부작용"
    b "내 연구는 인간의 신체와 정신능력을 강화하는 거였지만, 부작용으로 신체의 일부가 기형적으로 변하는 점이 있었어."
    b "아마 정부의 목적은 부작용이였던것 같아. 사람들을 괴물로 만들어 버리려고."
    "정부에서 그런일을 한다니 정말 믿기지가 않는다."
    f "도대체 왜 그런짓을..."
    b "내 추측으로는 정권 교체를 위한 도박이 아닌가 싶은데..."
    b "군 내부에서도 군부 정권 시절의 영향력을 그리워 하는 사람도 많다고 들었어."
    "권력때문에... 그런건가... 세상엔 왜이렇게 이상한사람이 많을까."
    f "오빠는 정말 몰랐던 거야?"
    b "응... 정말 몰랐어. 이럴줄 알았다면 지원을 받지 말았어야 하는데."
    b "이미 서울은 괴물로 변한 사람들 천지야."
    b "아마 유전자 변형 정도를 잘못 조절해서 모든 사람들이 괴물로 변한것 같아."
    "이미 괴물로 다 변했다니... 설마 부모님이랑 동생도"
    "아냐 무사할꺼야 그런생각 하지말자."
    b "학교 안에 안전한 곳이 있어. 그곳으로 가자"
    show f idle
    f "그래 알았어"
    "오빠와 함께 조심스럽게 발을 내딛는다. 앞에 있는 괴물들이 눈치채지 못하도록 조심히."
    #scene change 공대 문과대
    scene bg saecheonyeon
    with fade
    show b idle at right
    show b idle at right_
    show f idle at left 
    show f idle at left_ 
    with dissolve
    "공대를 지나, 문과대 앞에서 새천년관쪽으로 이동했다."
    "겨우 새천년관앞에 도착했지만 새천년관 문 앞에 괴물이 보인다."
    c "그우우우.."
    "일단 새천년관 앞 흡연구역에 멈춰서서 몸을 숨긴뒤 괴물을 확인했다."
    "괴물은 문앞에 서서 가끔 이상한 소리를 낼 뿐 미동도 하지 않았다."
    f "어쩌지?"
    b "그러게... 방법이 없네."
    b "일단 내가 가서 저녀석을 어떻게든 해볼테니 넌 여기서 기다려"
    "빠루를 들고 있는 오빠가 이렇게 믿음직 스러울 줄이야. 항상 랩실에 썩어 사는줄만 알았는데"
    f "정말 방법이 그것밖에 없는것 같네..."
    f "다치지 않겠다고 약속해줘"
    b "물론이지. 빨리 다녀올게"
    hide b with dissolve
    "오빠는 그런말을 하고는 앞으로 발을 내딛었다."
    "괴물이 제발 오빠를 발견못하기를, 오빠가 무사하기를"
    "도저히 밖을 내다볼수가 없어서 웅크려 앉은채 기도하고 있던 그때"
    "바스락"
    "이게 무슨소리지? 방금 무언가 소리가 들린것 같은 느낌에 나는 눈을떴고"
    show f scared at shake
    "눈을 뜬 내 앞에는 괴물이 있었다."
    f "아...으.....아...윽."
    "어디서 나타났는지 나타난 괴물을 나를 노려보고있었다."
    "나는 말도 제대로 내지 못하고 그저 사시나무 떨듯 떨뿐이였다."
    c "크아아악"
    "괴물이 나를 덮친다. "
    "나는 이제 정말 끝인가보다. 죽을때가 되면 슬로우 모션처럼 이런저런 생각이 난다던데"
    "어머니와 아버지는 무사할까? 사랑하는 내동생은? 그리고........"
    "마지막으로 생각난건 웃기게도 이은혁이였다."
    "한때 짝사랑했던 사람. 연구와 결혼한 사람이라 내가 자기 좋아했던건 절대 몰랐겠지."
    "이렇게 죽게 될줄 알았으면 고백이라도 해볼껄 그랬다."
    "그때"
    stop music fadeout 2
    show b angry at right
    show b angry at right_
    b "으아앗!"
    "푸직"
    "영화처럼 오빠가 나타났다."
    "오빠가 빠루로 괴물을 내려치자, 끈적한 핏덩이와 함께 구멍뚤린 육신이 쓰러졌다."
    show b idle
    b "괜찮아?"
    "오빠다. 오빠가 와 주었다."
    f "왜...이제왔어"
    f "바보...바보..."
    "순간적으로 안도해서인지 감정이 자제되지 않아 울어버렸다."
    b "괜찮아...다 끝났어... "
    b "이젠 정말 안전한곳으로 가자"
    "이사람이라면 믿어도 괜찮겠다고 생각하며 오빠와 함께 걸음을 내딛는다."

    #blackout

    scene bg bunker
    with fade
    show b idle at right
    show b idle at right_
    show f idle at left 
    show f idle at left_ 
    with dissolve
    play music "audio/A_peacefull.mp3" 
    "오빠와 함께 도달한 곳은 새천년관 지하에 있는 벙커였다. 학교안에 이런곳이 있었을 줄은 미처 몰랐지만"
    "오빠는 일감호 지하 벙커의 소문 발상지가 여기일 꺼라며 농담삼아 말을 해주었다."
    f "그래도 학교에 이런곳도 있다니 놀랍네"
    show b smile
    b "건축법상 대피용 지하시설이 있어야 된다나봐. 우리한텐 다행이지."
    "정말이다. 여기엔 어느정도 식량도 있으니 어느정도는 버틸수 있을것 같다."
    "어쩌면 이미 밖은 세상의 종말이 다가왔고, 우리 둘만 남은 세상이라 아무 소용 없을지도 모르지만."
    "그러니까 더욱 지금 말해야만 한다. "
    f "저기..."
    b "응?"
    f "사실은 나 오빠 좋아했었어"
    "떨리는 나의 목소리에 당황해하는 오빠가 보인다."
    b "어..."
    f "오빠는 나한테 전혀 관심도 없는것 같아서 말 안했었지만"
    b "아... 그랬구나..."
    b "..."
    b "미안 전혀 몰랐어."
    f "그럴것 같았어"
    "정말... 그럴줄 알았다. "
    b "......"
    f "......"
    b "......"
    "아 이 순둥이. 무안해진 분위기 어떡할꺼야."
    f "...저기..."
    b "...으..응?"
    show f smile at center with move
    f "키스할래?"
    b "어...어?"
    f "방금 어라고 했다?"
    "뭐어때, 세상에 둘밖에 안남았을지도 모르는데 무드가 중요한게 아니잖아."
    "..."
    "세계가 멸망한 뒤의 키스는 정말로 달콤해서"
    "이렇게 둘만의 시간이 영원히 계속되기를 바랬다."
    show none with dissolve
    call credits from _call_credits
    stop music fadeout 2
    pause 3 
    return


label badend_boom:
    scene none with dissolve
    "그리고 몇일 뒤"
    "여느때와 같이 일상을 보내다 창밖을 보니 타오르는 불꽃같은 폭발이 일어나고 있었다."
    "날라오는 파편과 열에 나는 그만 의식을 잃었다."
    window hide
    show bg gameover with dissolve
    pause 3
    return

label badend_ee:
    scene none with dissolve
    "오빠를 믿을순 없다. 연구의 당사자 아닌가?"
    "그렇게 오빠를 뿌리치고 온자 학교를 탈출하려고 하다가, 난 괴물과 마주쳤고"
    "이루 말할 새도 없이 괴물에게 덮쳐졌다."
    window hide
    show bg gameover with dissolve
    pause 3
    return


label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene none #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('일러스트 여자', '최희은'), ('일러스트 남자', '조현종'), ('배경음악', '김민제'), ('배경', '강명수'), ('시나리오 원안', '정규태'), ('시나리오 편집', '조현종'), ('프로그래밍', '조현종'), ('프로그래밍', '주형진'),  ('발표', 'ㅁㅁ')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.3.5.606" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)