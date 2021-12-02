def star(func):
    def inner(*args, **kwargs):
        print(args[1] * 30)
        func(*args, **kwargs)
        print(args[1] * 30)
    return inner

@star
def printer(msg, mark):
    print(msg)
printer("Hello", "&")