class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
    
        left, right = 0, len(digits) - 1
        while left < right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
    
        return True
