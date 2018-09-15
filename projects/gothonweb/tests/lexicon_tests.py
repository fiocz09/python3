from nose.tools import *
from gothonweb import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("tell"), [('verb', 'tell')])
    result = lexicon.scan("tell throw place")
    assert_equal(result, [('verb', 'tell'),
                          ('verb', 'throw'),
                          ('verb', 'place')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bomb"), [('noun', 'bomb')])
    result = lexicon.scan("bomb joke")
    assert_equal(result, [('noun', 'bomb'),
                          ('noun', 'joke')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bomb IAS joke")
    assert_equal(result, [('noun', 'bomb'),
                          ('error', 'IAS'),
                          ('noun', 'joke')])
