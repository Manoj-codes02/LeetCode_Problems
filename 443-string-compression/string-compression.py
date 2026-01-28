class Solution(object):
    def compress(self, chars):
        i = 0
        write = 0

        while i < len(chars):
            count = 1

            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1

            chars[write] = chars[i]
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

            i += 1

        return write

