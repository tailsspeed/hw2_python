def func_counter(func):
    def wrapper(*args, counter = 0):
        func(*args)
        counter += 1
    return wrapper
        
