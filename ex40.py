class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

twist = Song(["Everybody, twist",
              "",
              "They're twisting in Cleveland",
              "In Kansas City too",
              "They're wailing in Warwood",
              "In Pittsburgh and St Lou",
              "So, baby, get ready",
              "I'm gonna twist with you"])

smooth = Song(["Man, it's a hot one",
               "Like seven inches from the midday sun",
               "Well, I hear you whispering in the words, to melt everyone",
               "But you stay so cool",
               "My muñequita, my Spanish Harlem, Mona Lisa",
               "You're my reason for reason",
               "The step in my groove"])

twist.sing_me_a_song()
smooth.sing_me_a_song()
