numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in numbers:
    if i == 1:  #если число явл-ся 1 , пропускаем код ниже
        continue
    count = 0   #счетчик делителей
    for j in range(1, i + 1):   #цикл для подсчета делителей
        if count > 2:   #если кол-во делитлей уже больше 2-х, то оно точно составное
            break
        elif i % j == 0:    #иначе счситаем кол-во делителей
            count +=1
    if count == 2:  #если 2 делителя, то число простое
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые числа из списка: ', primes)
print('Составные числа из списка: ', not_primes)