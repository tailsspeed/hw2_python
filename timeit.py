import time
def calculate_time(func):
    def wrapper(*args, **kwargs): #*args, **kwargs allows arbitrary nubmer of positional and keyword args
            start = time.time()
            func(*args, **kwargs) #without it, error occurs about positional args
            end = time.time()
            print("Total time " + str(end-start))
    return wrapper
