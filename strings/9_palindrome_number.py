class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        len_x = len(str_x) - 1
        count = math.ceil(len_x / 2) - 1

        while count >= 0:
            if str_x[0 + count] != str_x[len_x - count]:
                return False
            count -= 1
        
        return True