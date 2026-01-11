from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        print(freq )
        # print(i)

        # Loops through the string in original order
        #  i → index
        # ch → character

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                print(i)
                return i

        return -1

str="loveleetcode"

obj=Solution()
ans=obj.firstUniqChar(str)
print(ans)