from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_case1():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected


def test_case2():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected


def test_case3():
    actual = validate_brackets("()[[True]]")
    expected = True
    assert actual == expected

def test_case4():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected

def test_case5():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected

def test_case6():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected

def test_case7():
    actual = validate_brackets("[")
    expected = False
    assert actual == expected

def test_case8():
    actual = validate_brackets("}")
    expected = False
    assert actual == expected


