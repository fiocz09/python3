class lexicon(object):

    def __init__(self):
        #lexicon
        self.directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verbs = ['go', 'stop', 'kill', 'eat']
        self.stops = ['the', 'in', 'of', 'from', 'at', 'it']
        self.nouns = ['door', 'bear', 'princess', 'cabinet']

    def tuplify(self, word):
        word_lower = word.lower()
        if(word_lower in self.directions):
            i = ('direction', word)
        elif(word_lower in self.verbs):
            i = ('verb', word)
        elif(word_lower in self.stops):
            i = ('stop', word)
        elif(word_lower in self.nouns):
            i = ('noun', word)
        elif(convert_number(word) != None):
            i = ('number', int(word))
        else:
            i = ('error', word)
        return i

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    word_list = []
    for word in words:
        i = lexicon().tuplify(word)
        word_list.append(i)
    return word_list
