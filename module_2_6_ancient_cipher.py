import random

def key_cipher(number):
    str_ = ''
    for i in range(1, 20):
        temp = ''
        temp_1 = ''
        for j in range(1, 20):
            temp = str(i) + str(j)
            temp_1 = str(j) + str(i)
            if number % (i + j) == 0 and str_.find(temp) == -1 and str_.find(temp_1) == -1 \
                    and i != j:
                str_ += str(i) + str(j)
    return str_

first_box = random.randrange(3,20)  #получаем случайное число в первой ячейке
print('Число в первой ячейке: ', first_box)
print('Ключ к выходу: ', key_cipher(first_box))


