# Задача про треугольники
storona1 = 5
storona2 = 10
storona3 = 15
if storona1 == storona2 == storona3:
    print("Треугольник равносторониий")
elif storona1 < storona2 > storona3:
    print("Треугольник разносторонний")
else:
    print("Такого треугольника не существует")
# Возраст человека
n1 = int(input("Введите свой возраст:"))
if 25<=n1<31:
    print("Вам " + str(n1)+" лет")
elif 21<n1<25:
    print("Вам " + str(n1)+" года")
else:
    print("Вам " + str(n1)+" год")