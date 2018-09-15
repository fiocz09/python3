class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, verb, obj):
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expecting a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    else:
        return ('noun', 'blank')

def parse_sentence(word_list):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(verb, obj)
