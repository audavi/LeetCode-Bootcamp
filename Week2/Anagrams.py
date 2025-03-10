class Solution(object):
    def findAnagrams(self, s, p):
        anagram = ''.join(sorted(p))
        window = ''
        indicies = []
        window_start = 0

        for char in s:
            window += char
            if len(window) == len(anagram):
                if ''.join(sorted(window)) == anagram:
                    indicies.append(window_start)
                window = window[1:] # remove left char of window
                window_start += 1
        return indicies

        
