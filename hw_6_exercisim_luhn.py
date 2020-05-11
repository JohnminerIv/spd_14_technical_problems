"""
Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of
identification numbers, such as credit card numbers and Canadian Social
Insurance Numbers.

The task is to check if a given string is valid.

Validating a Number
Strings of length 1 or less are not valid. Spaces are allowed in the input, but
they should be stripped before checking. All other non-digit characters are
disallowed.

Example 1: valid credit card number
4539 1488 0343 6467
The first step of the Luhn algorithm is to double every second digit, starting
from the right. We will be doubling

4_3_ 1_8_ 0_4_ 6_6_
If doubling the number results in a number greater than 9 then subtract 9 from
the product. The results of our doubling:

8569 2478 0383 3437
Then sum all of the digits:

8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid. This number is
valid!

Example 2: invalid credit card number
8273 1232 7352 0569
Double the second digits, starting from the right

7253 2262 5312 0539
Sum the digits

7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
57 is not evenly divisible by 10, so this number is not valid.
"""
# So the goal is to return whether or not the given string is luhn validated?
# I assume that there will not be letters in the string only spaces and numbers in the correct order.
# Other than that this question is pretty explicit as too what is desired.
# I'm just going to return a bool value


def luhn_validator(st):
    if len(st) == 19:
        is_valid = 0
        i, s = 0, 0
        while i < 19:
            if st[i] >= '0' and st[i] <= '9':
                if (i - s) % 2 == 0:
                    if int(st[(i)])*2 >= 10:
                        is_valid += (int(st[(i)])*2) - 9
                    else:
                        is_valid += (int(st[(i)])*2)
                else:
                    is_valid += int(st[(i)])
            elif st[i] == ' ':
                s += 1
            else:
                return False
            i += 1
        if is_valid % 10 == 0:
            return True
    return False


print(luhn_validator('4539 1488 0343 6467'))
print(luhn_validator('8273 1232 7352 0569'))
