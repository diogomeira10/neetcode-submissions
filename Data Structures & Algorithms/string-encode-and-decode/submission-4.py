class Solution:

    def encode(self, strs: list[str]) -> str:

        if not strs:
            return ""

        encoded_string = []

        for string in strs:
            encoded_string.append(str(len(string)))
            encoded_string.append("#")
            encoded_string.append(string)

        return "".join(encoded_string)

    def decode(self, s: str) -> list[str]:

        if not str:
            return []

        i = 0
        decoded_strings = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i : j])
            i = j + 1
            j = i + length
            word = s[i : j]
            decoded_strings.append(word)
            i = j
            

        return decoded_strings


