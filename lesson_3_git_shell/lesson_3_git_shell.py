#!/usr/bin/python3

'''
Фунцкия возведения чисел в определенную степень.
'''


def timing_decorator(func):
    import time       
    def wrapper(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        stop_time = time.time()
        time_diff = stop_time - start_time
        print(f'Время выполнения: {time_diff} секунд.')
        return return_value
    return wrapper


@timing_decorator
def expone(*args, exponenta=2):
    after_exp = []
    for x in args:
        for y in x:
            y = y**exponenta
            after_exp.append(y)
    return after_exp, exponenta


try: 
    input_numbers = [] 
    while True: 
        input_numbers.append(int(input("Введите целое число для добавлени в список. Для окончания списка введи любую букву: ")))  
except: 
    print("Список чисел сформирован!")


input_exponenta = int(input("Введите степень числа: "))

result = expone(input_numbers, exponenta=input_exponenta)

print(result)
