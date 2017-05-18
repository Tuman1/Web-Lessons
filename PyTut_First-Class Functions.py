# Programming Terms: First-Class Functions

# def square(x):
#     return x*x
#
# def cube(x):
#     return x * x * x
#
# def my_map(func, arg_list):
#     result = []
#     for item in arg_list:
#         result.append(func(item))
#     return result
#
# square = my_map(cube, range(1,6))
#
# print(square)

##Example of Closures
# def logger(msg):
#
#     def log_message():
#         print("Log: ", msg)
#
#     return log_message
#
# log_hi = logger('Hi!')
# log_hi()

def html_tag(tag):

    def warp_text(msg):
        print('<{0}><{1}><\{0}>'.format(tag, msg))

    return warp_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
