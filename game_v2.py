"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np #импортируем модуль numpy


number = np.random.randint(1, 101) #генерим случайное число от 1 до 100
def game_core_v3(number: int = 1) -> int:
  """Определяем за какое кол-во попыток наш алгоритм отгадает число

  Args:
      game_core_v3 (number): аргументом является случайное число от 1 до 100

  Returns:
      int: количество попыток
  """
  count = 0 #начальное значение счетчика попыток
  min = 0 #нижний предел
  max = 100 #верхний предел
  while True:
    predict = round((min+max)/2) #находим серединное значение между пределами
    count += 1 #увеличиваем значение счетчика
    if number == predict: #если сгенерированное случайное число равно серединному значению
      break #выходим из цикла
      #в иных случаях преверяем случайное число больше или меньше серединного значения
    elif number > predict:
      min = predict #если больше приравниваем нижний предел к серединному значению
      round((max + min) / 2)
    elif number < predict:
      max = predict #если меньше приравниваем верхний предел к серединному значению
      round((max + min) / 2)
  return count #количество попыток


def score_game_v1 (game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        score_game_v1 (game_core_v3): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

if __name__ == "__main__":
    # RUN
    score_game_v1(game_core_v3)