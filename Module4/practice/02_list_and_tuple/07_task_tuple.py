# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа

tup = (2, 4, 6, -4, 12, 0, 5)

my_list = list(tup)
my_list.sort()
my_list.reverse()

print(my_list[0])
