def sort_list(input):
    n = len(input) #number of elements in list
    i = 0; #index 0 of the list
    while i < n:
        j = 0
        while j < n - i - 1:
            if input[j] > input[j+1]:
                #swap
                temp = input[j]
                input[j] = input[j+1]
                input[j+1] = temp
            j = j + 1
        i = i + 1
    return input
