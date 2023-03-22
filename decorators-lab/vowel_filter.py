def vowel_filter(function):

    def wrapper():
        letters = function()
        vowels_list = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
        vowels = [v for v in letters if v in vowels_list]

        return vowels

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
