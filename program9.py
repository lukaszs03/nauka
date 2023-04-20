import time
def function_performance(func, arg, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum

setContainer = {i for i in range(10000)}
listContainer = [i for i in range(10000)]

def findInCointainter(what_value):
    if what_value in setContainer:
        return True
    else:
        return False
    
def findInCointainter2(what_value):
    if what_value in listContainer:
        return True
    else:
        return False

print(function_performance(findInCointainter, 8764, how_many_times=340))
print(function_performance(findInCointainter2, 8764, how_many_times=340))   
