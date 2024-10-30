"""
String palindrome checker
"""

def is_string_palindrome(word):
    '''
    Determines if a given word is 
    a palindrome.

    Args:
        word(string): The word to be checked

    Returns:
        boolean: True if word is a palindrom 
        else False
    '''

    # Convert word to lower case
    word = word.lower()

    # Setting start and end pointers
    start = 0
    end = len(word) - 1

    while start <= end:
        # Check if the letter is a valid 
        # alphabet before procedding, if
        # not adjust the pointera
        if word[start].isalpha() is False:
            start += 1
            continue

        if word[end].isalpha() is False:
            end -= 1
            continue

        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True
