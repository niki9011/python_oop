class vowels:

    VOWELS = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]

    def __init__(self, word):
        self.word = word
        self.start = 0
        self.index = len(word)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.index:
            raise StopIteration

        ch = self.word[self.start]
        self.start += 1

        if ch not in vowels.VOWELS:
            return self.__next__()

        return ch

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
