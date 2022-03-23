def solution(n, arr1, arr2):
    answer = []

    map1 = make_map(n, arr1)
    map2 = make_map(n, arr2)

    map = []
    for yi in range(n):
        map.append([])
        for xi in range(n):
            map[yi].append(" ")

    for yi in range(n):
        for xi in range(n):
            if map1[yi][xi] == "#" or map2[yi][xi] == "#":
                map[yi][xi] = "#"

    for yi in range(n):
        line = ''
        for xi in range(n):
            line += map[yi][xi]
        map[yi] = line
    answer = map

    # print(arr1_map)
    return answer

def make_map(n, arr):
    arr_map = []
    for i in range(len(arr)):
        arr_bits = extend_bits(n, num_to_bits(arr[i]))
        arr_mapline = ''
        for j in range(n):
            if arr_bits[j] == '0':
                arr_mapline += ' '
            elif arr_bits[j] == '1':
                arr_mapline += '#'
        arr_map.append(arr_mapline)
    return arr_map

def extend_bits(n, bits):
    lb = len(bits)
    if lb < n:
        for i in range(n-lb):
            bits = '0' + bits
    return bits

def num_to_bits(num):
    radix = 2
    bits = ''
    while num > 0:
        bits = str(num % radix) + bits
        num //= radix
    return bits

print(bin(10))
print(type(bin(10)))
print(9|10)

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))