# Слова и переводы (пары, где перевод — правильный вариант)
word1_ru = "яблоко"
word1_en = "apple"

word2_ru = "дом"
word2_en = "house"

word3_ru = "кот"
word3_en = "cat"

# Варианты для каждого слова (смешаны, один правильный)
options1_a = "apple"
options1_b = "banana"
options1_c = "pear"

options2_a = "car"
options2_b = "house"
options2_c = "window"

options3_a = "dog"
options3_b = "cat"
options3_c = "bird"

# Счётчик правильных ответов и количество вопросов
score = 0
questions_asked = 0
max_questions = 3

# Первый вопрос
print("Переведите слово:", word1_ru)
print("1)", options1_a)
print("2)", options1_b)
print("3)", options1_c)
answer = input("Ваш ответ (номер): ")
if answer == "1":
    print("Верно!")
    score += 1
else:
    print("Неверно. Правильный ответ:", word1_en)
questions_asked += 1
print()

# Второй вопрос
print("Переведите слово:", word2_ru)
print("1)", options2_a)
print("2)", options2_b)
print("3)", options2_c)
answer = input("Ваш ответ (номер): ")
if answer == "2":
    print("Верно!")
    score += 1
else:
    print("Неверно. Правильный ответ:", word2_en)
questions_asked += 1
print()

# Третий вопрос
print("Переведите слово:", word3_ru)
print("1)", options3_a)
print("2)", options3_b)
print("3)", options3_c)
answer = input("Ваш ответ (номер): ")
if answer == "2":
    print("Верно!")
    score += 1
else:
    print("Неверно. Правильный ответ:", word3_en)
questions_asked += 1
print()

# Итог
print("Игра окончена. Ваш счёт:", score, "из", max_questions)