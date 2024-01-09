"""
What is decorators?
Decorators allow us to wrap another function in order to extend the behaviour of wrapped function
without permanently modifying it.
                                    or
Decorators changes the behaviour of existing function during runtime.
Decorate using @
"""

def sqr_num(func):
    def wrapper():
        x = func()
        sqr = x**2
        return sqr
    return wrapper

@sqr_num
def number():
    return 10

print(number())


def cub_num(func):
    def wrapper():
        x = func()
        cub = x**3
        return cub
    return wrapper
@cub_num
def number():
    return 30
print(number())