class Solution:
    def __init__(self):
        self.separated_lines = []
        self.words = None
        self.maxWidth = None

    def get_line(self, i):

        cur_count = 0
        cur_line = []
        word_count = -1

        while i < len(self.words) and cur_count + word_count + len(self.words[i]) < self.maxWidth:
            cur_count += len(self.words[i])
            cur_line.append(self.words[i])
            i += 1
            word_count += 1

        self.separated_lines.append([cur_line, cur_count + word_count])

        return i

    def add_spaces(self, line):

        spaces = self.maxWidth - line[1]

        if len(line[0]) == 1:
            line[0][0] = line[0][0] + ' ' * spaces
            return

        i = 0
        while spaces > 0:
            exp = i % len(line[0])
            if exp != len(line[0]) - 1:
                line[0][exp] = line[0][exp] + ' '
                spaces -= 1
            i += 1

    def fullJustify(self, words, maxWidth: int):

        self.words = words
        self.maxWidth = maxWidth

        i = 0
        while i < len(self.words):
            i = self.get_line(i)

        for line in self.separated_lines[:-1]:
            self.add_spaces(line)

        self.separated_lines[-1][0][-1] = self.separated_lines[-1][0][-1] + ' ' * \
                                          (self.maxWidth - self.separated_lines[-1][1])

        for l in range(len(self.separated_lines)):
            self.separated_lines[l] = ' '.join(self.separated_lines[l][0])

        return self.separated_lines
