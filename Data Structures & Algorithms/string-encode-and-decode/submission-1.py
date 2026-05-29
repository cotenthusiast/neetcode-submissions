class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = '#'
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += sep 
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        sep = '#'
        returnlist = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != sep:
                j+=1
            length = int(s[i:j])
            returnlist.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return returnlist
