# Проект 0. Угадай число

## [ -Оглавление](#Оглавление)

[1. Описание проекта](.README.md#Описание-проекта)<br>
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)<br>
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)<br>
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)<br>
[5. Результат](.README.md#Результат)<br>
[6. Выводы](.README.md#Выводы)<br>

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:
### оглавление

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**
- Компьютер загадывает целое число от 1 до 100, и сам же его отгадывает. Под «угадать»,
подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений.
Необходимо добиться минимального количества попыток.

**Что практикуем**
Учимся писать хороший код на python.
Учимся работать с IDE.
Учимся работать с GitHub.


### Краткая информация о данных
Случайное число от 1 до 100. И две ф-ции для расчета среднего количества попыток.
Применяем метод бинарного поиска.
  
:arrow_up:[к оглавлению](.README.md#Оглавление)

### Этапы работы над проектом
1. Генерируем случайное число.
2. Подставляем в функцию game_core_v3 и получаем кол-во попыток угадывания.
3. Потом используем эту же ф-цию в качестве аргумента для ф-ции score_game_v1 и
получаем среднее количество попыток угадывания.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Результаты:
Получаем среднее число попыток угадывания числа.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Выводы:
Использование эффективных алгоритмов дает возможность угадать число меньше чем
за 20 попыток.

:arrow_up:[к оглавлению](.README.md#Оглавление)

Если информация по этому проекту покажется вам интересной или полезной, то я
буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами