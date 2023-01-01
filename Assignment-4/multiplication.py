def multiplication(n1: int, n2: int) -> int:
    arr1 = []
    arr2 = []
    arr1.append(n1)
    arr2.append(n2)
    i = n1
    while i > 1:
        i = int(i/2)
        arr1.append(i)
    lenght = len(arr1)
    
    i = 0
    for i in range(lenght - 1):
        arr2.append(arr2[i] * 2)

    print(arr1)
    print(arr2)

    i = 0
    for i in range(lenght - 1):
        if arr1[i] % 2 == 0:
            arr2[i] = 0

    print(arr2)

    sum = 0
    i = 0
    for i in range(lenght):
        sum += arr2[i]
        i += 1

    return sum

if __name__ == "__main__":
    print(multiplication(23, 42))
