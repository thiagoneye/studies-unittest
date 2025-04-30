"""
You have the palindrome checking function.

This function checks if a string is a palindrome by first converting it to lowercase and removing all whitespace characters.

It then checks if the resulting string is equal to its reverse.

Implement the test_is_palindrome() function that tests the is_palindrome() function.

Use assert statements five different inputs:
- "racecar"
- "hello"
- "A man a plan a canal Panama"
- "12321"
- "not a palindrome"
"""

def is_palindrome(string: str) -> bool:
    """
    Determines whether the given string is a palindrome.

    :param string: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    string = string.lower().replace(" ", "")
    return string == string[::-1]
    
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("not a palindrome") == False

if __name__ == '__main__':
    test_is_palindrome()
