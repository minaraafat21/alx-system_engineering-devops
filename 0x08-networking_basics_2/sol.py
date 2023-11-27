class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        my_string = self.my_s(n)
        print(my_string[k-1 ])
       

    def my_s(self, n):
        if n > 1:
            return self.my_s(n-1) + "1" + self.reverse(self.invert(self.my_s(n-1))) 
        else:
            return "0"

    def reverse(self, s):
        return s[::-1]

    def invert(self, s):
        for n in s:
            if n == "0":
                s = s.replace(n, "1")
            else:
                s = s.replace(n, "0")
        return s
    
Solution().findKthBit(4, 0)
