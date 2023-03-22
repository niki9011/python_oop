def number_increment(numbers):

    def increase():
        number_increment = [n + 1 for n in numbers]
        return number_increment
    return increase()


print(number_increment([1, 2, 3]))
