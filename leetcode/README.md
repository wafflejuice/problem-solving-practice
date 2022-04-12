### 13. Roman to Integer
Leanrt "zip" usage
```
pair_dict = {i:j for i,j in zip(list1, list2)}
```
Roman to Integer는 문자열을 순회하며 i-1, i번째 원소의 대소비교로 쉽게 구현 가능

### 289. Game of Life
y, x 좌표로 표현되는 board에서 boundary check는 아래와 같이 간편하게 할 수 있다.  
즉, 각 위치마다 복잡한 if문으로 valid한지 따지지 않아도 된다.
```
for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]:
        if dy==0 and dx==0:
            continue
        ...
```
valid 여부만 따진다면, 다음과 같이 간편하게 구현할 수도 있다.
```
def is_valid(board, yi, xi):
    if (yi<0 or yi>=len(board) or xi<0 or xi>=len(board[0]):
        return False
    return True
```
