from nose.tools import *
from gothonweb import lexicon, parser

def test_sentence():

    result1 = parser.parse_sentence(lexicon.scan('slowly place the bomb with care'))
    assert_equal(result1.verb, 'place')
    assert_equal(result1.object, 'bomb')

    result2 = parser.parse_sentence(lexicon.scan('purposefully shoot the Gothon'))
    assert_equal(result2.verb, 'shoot')
    assert_equal(result2.object, 'blank')

def test_parsererror():

    with assert_raises_regexp(parser.ParserError, "Expecting a verb next."):
        parser.parse_sentence(lexicon.scan('slowly ***** the bomb with care'))

    with assert_raises_regexp(parser.ParserError, "Expecting a verb next."):
        parser.parse_sentence(lexicon.scan('purposefully ***** the Gothon'))
