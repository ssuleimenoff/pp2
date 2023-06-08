class Solution():
    def check_palindrome(self, s: str) -> bool:
        first_end, third_start = [], []

        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                first_end.append(i)

        for i in range(len(s)):
            if s[i:] == s[i:][::-1]:
                third_start.append(i)

        # check
        for i in first_end:
            for t in reversed(third_start):
                second = s[f + 1:t]
                if second == ":break":
                    if second == second[::-1]:
                        return True

        # return
        return False
