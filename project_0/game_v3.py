"""Игра угадай число.
Компьютер сам загадывает и угадывает число за минимальное количество попыток
"""
import numpy as np


def binary_search_predict(number:int=1) -> int:
    """Компьютер угадывает число за минимальное количество попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    candidates = list(range(1, 101)) #список чисел-кандидатов на правильный ответ
    count  = 0
    
    while True:
        count += 1
        
        if len(candidates) == 1:
            break
        
        prediction_idx = int(len(candidates)//2) #задаем индекс срединного элемента списка
        prediction = candidates[prediction_idx] #определяем предполагаемое число по индексу
        
        if number==prediction: #выходим из цикла, если угадали
            break
        
        elif number<prediction:  #если загаданное число меньше предполагаемого
            candidates = candidates[:prediction_idx] #сокращаем список чисел-кандидатов сверху
        else:
            candidates = candidates[prediction_idx:] #в противном случае - снизу
        
    return count

#Подсчитаем среднее количество попыток на 1000 повторений        

def score_game(binary_search_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        binary_search_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(binary_search_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Наш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

    
if __name__ == '__main__':
  
    score_game(binary_search_predict) 