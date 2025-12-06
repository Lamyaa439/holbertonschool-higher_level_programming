#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    length = len(roman_string)

    for i in range(length):
        # Get the value of the current character
        current_value = roman_dict.get(roman_string[i], 0)
        
        # Check if there is a next character
        if i < length - 1:
            next_value = roman_dict.get(roman_string[i + 1], 0)
            
            # Subtraction Rule (e.g., IV: 1 < 5)
            if current_value < next_value:
                result -= current_value
            else:
                result += current_value
        else:
            # Always add the last character
            result += current_value

    return result
