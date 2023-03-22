def multiply(times):

    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            sum_numbers = times * result

            return sum_numbers

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))
