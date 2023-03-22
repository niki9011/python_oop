def even_numbers(function):

    def wrapper(numbers):
        evens = function(numbers)
        even_list = [e for e in evens if e % 2 == 0]

        return even_list

    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
