from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    quips = ["人的生命是有限的。",
             "即使你怎么尽全力努力，也只能续到一点点。",
             "祝您遇快！合家欢落！谢谢！"]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class HKJournal(Scene):
    def enter(self):
        print(dedent("""
                     江主席，你觉得董先生连任好不好啊？
                     中央也支持他吗？
                     那为什么这么早就提出了，有没有别的人选呢？
                     现在呢那么早呢你们就是说支持董先生呢，
                     会不会给人一种感觉就是内定了、钦点了董先生呢？
                     """))
        action = input("> ")
        if action == "no comment":
            print(dedent("""
                         我很抱歉，我今天是作为一个长者——给你们讲的。
                         我不是新闻工作者，但是我见得太多了，
                         我……我有这个必要告诉你们一点，人生的经验。
                         我刚才呢……我刚才我很想啊，就是我每一次碰到你们我就讲
                         中国有一句话叫“闷声大发财”，我就什么话也不说。这是最好的！
                         但是我想，我见到你们这样热情啊，一句话不说也不好。
                         所以你刚才你一定要——在宣传上将来如果你们报道上有偏差，你们要负责。
                         我没有说要钦定（董建华），没有任何这个意思。
                         但是你问……你一定要觉得要问我……对董先生支持不支持。
                         我们不支持他？他现在是当特首，我们怎么能不支持特首？
                         """))
            return 'death'
        elif action == "too young":
            print(dedent("""
                         我觉得你们啊，你们……我感觉你们新闻界还要学习一个，
                         你们非常熟悉西方的这一套理论。
                         你们毕竟还 too young（太年轻），明白这意思吧。
                         我告诉你们我是身经百战了，见得多了！
                         啊，西方的哪一个国家我没去过？媒体他们——
                         你……你们要知道，美国的华莱士，那比你们不知道高到哪里去了。
                         啊，我跟他谈笑风生！
                         所以说媒体啊，要……还是要提高自己的知识水平！
                         懂我的意思——识得唔识得啊？
                         """))
            return 'death'
        elif action == "angry":
            print(dedent("""
                         诶，连任也要按照香港的法律啊，对不对？
                         要要……要按照香港的……当然我们的决定权也是很重要的。
                         香港的特区……特别行政区是属于中国……人民共和的中央人民政府啊。
                         啊？到那个时候我们会表态的！
                         明白这意思吧？
                         你们啊，不要想……喜欢……弄个大新闻，说现在已经钦定了，再把我批判一番。
                         你们啊，naïve!
                         """))
            return 'visit_united_engineering_company'
        else:
            print("你说神末啊？！")
            return 'scold_hongkong_journalist'

class CUE(Scene):
    def enter(self):
        print(dedent("""
                     二院从二分局成立至今已经经历了56年的历史，
                     从白手起家经历了风雨磨砺。到了改革开放，
                     从一个从事工业设计的事业单位，发展到现在具备工程设计综合资质，
                     又能够提供工程建设全过程服务的科技型工程公司。
                     特别是在2008年，我们公司成为共和国首批获得综合资质的9家单位之一。
                     我们也知道，到现在为止能取得这样的成绩，我们老在反思，
                     实际上跟江主席你们第一代二院人原来打下很好的基础是分不开的，
                     我们也一定会继承和发扬你们老一辈的优良传统和优秀文化，
                     特别是按照江主席的题词要求去谋划未来。
                     下面有请江主席讲三个数字。
                     """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guess != "excited" and guess != code and guesses < 9:
            print(dedent("""
                         这个engineering drawing呢，我们就有几年用鸭嘴的笔，
                         旁边一个小盒子。最痛苦的，就是鸭嘴笔把这个水弄到里面，
                         描图的时候一下子就……然后就用刀片刮，这个就是描图最痛苦的，
                         而且这个效率efficiency……
                         """))
            guesses += 1
            guess = input("[keypad]> ")
        if guess == "excited" or guess == code:
            print(dedent("""
                         人呐就都不知道，自己就不可以预料。
                         一个人的命运啊，当然要靠自我奋斗，但是也要考虑到历史的行程。
                         我绝对不知道，我作为一个上海市委书记怎么把我选到北京去了，
                         所以邓小平同志跟我讲话，说“中央都决定啦，你来当总书记”，
                         我说另请高明吧。我实在我也不是谦虚，
                         我一个上海市委书记怎么到北京来了呢？
                         但是呢，小平同志讲“大家已经研究决定了”，
                         所以后来我就念了两首诗，叫“苟利国家生死以，岂因祸福避趋之”，
                         那么所以我就到了北京。
                         很惭愧，就做了一点微小的工作，谢谢大家。
                         """))
            return 'talk_cheerfully_with_Wallace'
        else:
            print(dedent("""
                         我在想我估计是快要离休了，我想我应该去当教授。
                         """))
            return 'death'

class Wallace(Scene):
    def enter(self):
        print(dedent("""
                     A dictator is somebody who forcibly
                     whether it's free press or free religion
                     or free private enterprise now you're beginning
                     to come a little closer to that.
                     Your father knows best and if you get in the way of father,
                     father will take care of you.

                     You are the last major communist dictatorship in the world.
                     """))
        action = input("> ")
        if action == "not decide":
            print(dedent("""
                         Your way of describing what things are like in China
                         is absurd as what Arabian nights may sound like.
                         The National People's Congress selects
                         the central committee of the Communist Party,
                         and the central committee has a politburo,
                         and the politburo has a standing committee,
                         of which I am a member,
                         and no decision is made unless all the members agree.
                         """))
            return 'death'
        elif action == "friendship":
            print(dedent("""
                         On the whole, the relations between China and
                         the United States are good.
                         However, I would like to use words people used to
                         describe nature to describe the state of China-US relations.
                         Our relations have experienced wind, rain
                         and sometimes cloud or even dark clouds.
                         However sometimes it clears up.
                         We all sincerely hope to build a constructive partnership
                         between China and the United States.
                         """))
            return 'finished'
        else:
            print("This is a big mistake.")
            return "talk_cheerfully_with_Wallace"

class Finished(Scene):
    def enter(self):
        print("成功续命！+1s")
        return 'finished'

class Map(object):
    scenes = {'scold_hongkong_journalist': HKJournal(),
              'visit_united_engineering_company': CUE(),
              'talk_cheerfully_with_Wallace': Wallace(),
              'death': Death(),
              'finished': Finished(),
             }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('scold_hongkong_journalist')
a_game = Engine(a_map)
a_game.play()
