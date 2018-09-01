from nose.tools import *
from ex48 import lexicon, parser

def test_sentence():

    result1 = parser.parse_sentence(lexicon.scan('gigantic spooky creepy Cthulhu eat a yummy snickers causually'))
    assert_equal(result1.subject, 'Cthulhu')
    assert_equal(result1.verb, 'eat')
    assert_equal(result1.object, 'snickers')

    result2 = parser.parse_sentence(lexicon.scan('run insanely down to the dungeon'))
    assert_equal(result2.subject, 'player')
    assert_equal(result2.verb, 'run')
    assert_equal(result2.object, 'down')

def test_parsererror():

    with assert_raises_regexp(parser.ParserError, "Expecting a verb next."):
        parser.parse_sentence(lexicon.scan('gigantic spooky creepy ******* *** a yummy ******** causually'))

    with assert_raises_regexp(parser.ParserError, "Expecting a verb next."):
        parser.parse_sentence(lexicon.scan('gigantic spooky creepy Cthulhu *** a yummy snickers causually'))

    with assert_raises_regexp(parser.ParserError, "Expecting a noun or direction next."):
        parser.parse_sentence(lexicon.scan('gigantic spooky creepy Cthulhu eat a yummy ******** causually'))
