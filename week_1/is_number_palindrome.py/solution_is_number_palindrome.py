"""
Number palindrome checker
"""

def is_number_palindrome(number):
    '''
    Determines if a given number is 
    a palindrome.

    Args:
        number(number): The number to be checked

    Returns:
        boolean: True if number is a palindrom 
        else False
    '''
    # Convert number to string
    number_string = str(number)

    # Setting start and end pointers
    start = 0
    end = len(number_string) - 1

    while start <= end:
        # Check for valid numeric items
        # before procedding, if not adjust
        # the pointer
        if number_string[start].isnumeric() is False:
            start += 1
            continue

        if number_string[end].isnumeric() is False:
            end -= 1
            continue

        # If any inequality is found its
        # not a palindrome
        if number_string[start] != number_string[end]:
            return False

        # Adjust pointers
        start += 1
        end -= 1
    return True
