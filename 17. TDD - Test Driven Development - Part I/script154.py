def cnt(string):
    vowels = ["a", "e", "i", "o", "u"]
    words = string.split()
    begin_with_vowels = [word for word in words if word[0].lower() in vowels]
    return len(begin_with_vowels)


def test_cnt():
    assert cnt("dog cat egg") == 1, '"dog cat egg" failed'
    assert cnt("Apple igloo pet") == 2, '"Apple igloo pet" failed'
    assert cnt("file disk") == 0, '"file disk" failed'
    assert cnt("xyz") == 0, '"xyz" failed'
    assert cnt("") == 0, '"" failed'
