time limit : 4 hours

### 1. N진수 게임
- (2회차) 20분

number radix 변환
```
def num_to_radix(num, radix):
    radix_table = '0123456789ABCDEF'
    if num == 0:
        return '0'
    
    num_by_radix = ''
    while num > 0:
        num_by_radix = radix_table[num % radix] + num_by_radix
        num //= radix
    return num_by_radix
```

### 2. 압축
- 31분
```
ord('a') # 97
chr(97) # 'a'
```

### 3. 파일명 정렬
- (2회차) 1시간 20분

merge sort에서 left[li] == right[ri]일 때, left[li]만 merged_list에 추가한다.
right[ri]까지 추가해버리면 un-stable해진다!!!
```
...
if left[li] == right[ri]:
    merged_list.append(left[li])
    li += 1
...
```

merge sort template
```
def merge_sort(l):
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    
    li, ri = 0, 0
    merged_list = []
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            merged_list.append(left[li])
            li += 1
        elif left[li] > right[ri]:
            merged_list.append(right[ri])
            ri += 1
        else:
            merged_list.append(left[li])
            li += 1
    
    if li < len(left):
        merged_list += left[li:]
    elif ri < len(right):
        merged_list += right[ri:]
    
    return merged_list
```

python의 sorted()는 stable sort한 값을 return한다. 또한 어떤 값을 기준으로 삼을 것인지도 지정 가능한다. lambda function과 조합하면 좋다.
```
split_file_names = sorted(split_file_names, key=lambda split_file_name: int(split_file_name[1]))
```
### 4. 방금그곡
- (2회차) 39분

### 5. 자동완성
- 1시간 27분

tree 및 trie 공부 필요