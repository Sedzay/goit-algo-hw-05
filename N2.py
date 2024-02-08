from typing import Callable
import re

def generator_numbers(text: str):
    #return [float(num) for num in re.findall(r'\d+\.\d+',text)]  #було б цікавіше
    for num in re.findall(r'\d+\.\d+',text): #визначення всіх чисел в тексті
        yield float(num)
    
    
def sum_profit(text: str, func: Callable):
    return sum(func(text)) #підрахунок суми


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")