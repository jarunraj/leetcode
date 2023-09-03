class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i, j = 0, len(s)-1
        vowels = 'aeiouAEIOU'
        slist = list(s)

        while i < j:
            while i < j and slist[i] not in vowels:
                i += 1
            while i < j and slist[j] not in vowels:
                j -= 1
            if i < j:
                slist[i], slist[j] = slist[j], slist[i]
                i, j = i + 1, j - 1

        return "".join(slist) 