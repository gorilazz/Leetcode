class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        rev_s = s[::-1]
        ls = rev_s.split(' ')
        rev_word_s = ""
        for word in ls:
            if word:
                rev_word = word[::-1]
                rev_word_s += ' ' + rev_word
        
        return rev_word_s.strip()