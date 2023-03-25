def even_parameters(function):

    def wapper(*args):
        not_even = "Please use only even numbers!"

        for x in args:
            if isinstance(x, int):
                if x % 2 != 0:
                    return not_even

            else:
                return not_even

        return function(*args)

    return wapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
