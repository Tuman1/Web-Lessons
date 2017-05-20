# Programming Terms: Closures - How to Use Them and Why They Are Useful

# Closures
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()
