class reverse_iter:

    def __init__(self, ll):
        self.ll = ll
        self.index = len(self.ll)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.ll[self.index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
