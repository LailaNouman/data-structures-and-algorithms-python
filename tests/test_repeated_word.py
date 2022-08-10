from hashmap_repeated_word.hashmap_repeated import repeated_word

def test_capital_words():
    actual = repeated_word('Hello world, the world is a beautiful place')
    expected = 'world'
    assert actual == expected


def test_small_text():
    actual = repeated_word('once upon a time, there was a brave princess')
    expected = 'a'
    assert actual == expected


def test_not_repeated():
    actual = repeated_word('Hi, how are you?')
    expected = None
    assert actual == expected