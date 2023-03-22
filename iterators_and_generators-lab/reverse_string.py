def reverse_text(word):
    for w in reversed(word):
        yield w

for char in reverse_text("step"):
    print(char, end='')
