"""
The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.
"""
# You would like an integer from a sting that conatins numbers?

# Is it possible that ther ar no numbers in the string?
# It is possible that there are characters after the string?
# Is it possbile that it'll receive an empty string?
# Is there a limit to the size of then numbers being converted?

"""
The string can contain additional characters after those that form the
integral number, which are ignored and have no effect on the behavior of this
function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
value is out of the range of representable values, INT_MAX (231 − 1) or
INT_MIN (−231) is returned.
"""

# My solution would be to loop through the string unil I find a none whitespace
# Then if the next char is not a number or sign then return 0
# else hold the the sign and begin scanning the number that follows
# and holding the number in an int. Continually check if the number is greater
# than the max number and if it is return the max number.


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        started = False
        number = 0
        sign = 1
        index = 0
        if str[0] == '-':
            sign = -1
            index += 1

        for j in range(len(str)):
            if started is True and (str[j] >= '0' and str[j] <= '9') is False:
                return sign * number
            elif str[j] == ' ':
                pass
            elif ((str[j] == '+') or (str[j] == '-')) and j+1 < len(str):
                if (str[j+1] >= '0' and str[j+1] <= '9'):
                    if str[j] == '-':
                        sign = -1
                        started = True
                else:
                    return 0
            elif (str[j] >= '0' and str[j] <= '9') is True:
                started = True
                number = number * 10 + (ord(str[j]) - ord('0'))
            else:
                return 0
            if started is True and sign == 1 and number >= 2147483647:
                return 2147483647
            if started is True and sign == -1 and number >= 2147483648:
                return -2147483648
        return sign * number

# I can't think of a wayt to do this without a loop so is can't really think
# of a way to not do this in constant time and it definitly needs a lot of
# conditionals some of which might be avoidable or condensable but it might take
# me a while. Over all I think that this is an okay solution. I know that there
# are probably more optimised ways ot do this.
