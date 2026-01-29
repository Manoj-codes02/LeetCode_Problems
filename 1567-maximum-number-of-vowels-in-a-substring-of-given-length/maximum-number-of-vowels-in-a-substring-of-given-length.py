class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        count = 0

        # first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # slide window
        for i in range(k, len(s)):
            if s[i] in vowels:        # add right
                count += 1
            if s[i - k] in vowels:    # remove left
                count -= 1

            max_count = max(max_count, count)

        return max_count
