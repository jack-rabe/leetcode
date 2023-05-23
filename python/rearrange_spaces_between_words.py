class Solution(object):
    def reorderSpaces(self, text):
        ans = ""
        num_spaces = 0
        tmp = text.split(" ")
        words = []
        for word in tmp:
            if word != "":
                words.append(word)

        # handle case w/ 1 word
        if len(words) == 1:
            return words[0] + (" " * (len(text) - len(words[0])))

        # count number of spaces
        for char in text:
            if char == " ":
                num_spaces += 1
        # calculate number of spaces per word
        spaces_per_word = int(num_spaces / (len(words) - 1))
        leftover_spaces = num_spaces - (spaces_per_word * (len(words) - 1))
        # construct answer
        for word in words:
            ans += word
            if spaces_per_word > 0:
                ans += " " * spaces_per_word
        # chop off extra spaces and append leftover spaces
        ans = ans[:-spaces_per_word] + (" " * leftover_spaces)

        return ans
