def make_underline(function):
    def wrapper(*args):

        return f"<u>{function(*args)}</u>"
    return wrapper


def make_italic(function): # italiac
    def wrapper(*args):

        return f"<*>{function(*args)}</*>"
    return wrapper


def make_bold(function):
    def wrapper(*args):

        return f"<*>{function(*args)}</*>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

