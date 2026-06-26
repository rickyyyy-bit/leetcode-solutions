class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)

        if x == 0:
            return 0

        while string_x[(len(string_x) - 1)] == "0":
            string_x = string_x[0:(len(string_x) - 1)]

        output = ""
        
        if string_x[0:1] == "-":
            output = "-" + string_x[:0:-1]
        else:
            output = string_x[::-1]
        
        if int(output) < (-2**31) or int(output) > (2**31 - 1):
            return 0
        else:
            return int(output)
