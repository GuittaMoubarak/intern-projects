def ex1(list1):
    count = 0
    i = 0
    while i < len(list1):
        j = i+1
        while j < len(list1):
            if list1[j] == list1[i]:
                count += 1
            j = j+1
        i = i + 1
    if count == 0:
        print("no matching numbers")
    else:
        print("some numbers are the same")


list1 = [1, 2, 3, 4, 5, 5, 6, 7]
# ex1(list1)


def ex2(list1):
    while len(list1) > 2:
        a = list1[2]
        print(a)
        list1.remove(a)
    print(list1)
    print("the list1 cannot become empty")

# ex2(list1)


def ex3(list1):
    min = list1[0]
    for n in list1:
        if min > n:
            min = n
    print(min)

# ex3(list1)


def ex4(list1):
    sum = 0
    for n in list1:
        sum += n
    print(sum)

# ex4(list1)


def ex5(list1):
    i = 0
    while i < len(list1):
        count = 0
        j = 1
        while j < len(list1):
            if list1[j] == list1[i]:
                count += 1
            j = j+1
        if count == 1:
            print(list1[i])
        i = i + 1

# list12 = [2, 3, 4, 5, 2, 4, 2, 2, 5, 4, 5, 4, 5]
# ex5(list12)


def ex6(list1):
    for n in list1:

        for i in range(2, n):
            if n % i == 0:
                return False
    return True


# print(ex6(list1))

def ex7(list12):
    i = 0
    while i < len(list12):
        j = i + 1
        while j < len(list12):
            if list12[i] == list12[j]:
                a = list12[j]
                list12.remove(a)
            j = j+1
        i = i + 1
    print(list12)
# list12 = [3, 4, 5, 6, 7, 8, 2, 3, 5]
# ex7(list12)


def ex8(list1):
    list2 = []
    for n in list1:
        list2.append(str(n))
    list1 = list2
    print(list1)
    list2.clear()


ex8(list1)
