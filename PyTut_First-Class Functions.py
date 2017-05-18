# Programming Terms: First-Class Functions
def square(x):
    return x*x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for item in arg_list:
        result.append(func(item))
    return result

square = my_map(cube, range(1,6))

print(square)
