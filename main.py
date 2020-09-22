class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        c = 0
        while c < len(s):
            if s[c:c + 1] == 'I':
                if s[c + 1:c + 2] == 'V':
                    sum += 4
                    c += 2
                    continue
                elif s[c + 1:c + 2] == 'X':
                    sum += 9
                    c += 2
                    continue
                else:
                    sum += 1
            elif s[c:c + 1] == 'X':
                if s[c + 1:c + 2] == 'L':
                    sum += 40
                    c += 2
                    continue
                elif s[c + 1:c + 2] == 'C':
                    sum += 90
                    c += 2
                    continue
                else:
                    sum += 10
            elif s[c:c + 1] == 'C':
                if s[c + 1:c + 2] == 'D':
                    sum += 400
                    c += 2
                    continue
                elif s[c + 1:c + 2] == 'M':
                    sum += 900
                    c += 2
                    continue
                else:
                    sum += 100
            elif s[c:c + 1] == 'V':
                sum += 5
            elif s[c:c + 1] == 'L':
                sum += 50
            elif s[c:c + 1] == 'D':
                sum += 500
            elif s[c:c + 1] == 'M':
                sum += 1000
            c += 1
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt(s='MCMXCIV'))
