my_list = []

my_list.insert(0, 10)
my_list.insert(1, 20)
my_list.insert(2, 30)
my_list.insert(3, 40)
my_list.insert(1, 15)

anotherList = [50, 60, 70]

my_list.extend(anotherList)

my_list.pop()

my_list.sort()
for x in range(len(my_list)):
    if my_list[x] == 30:
        print(x)