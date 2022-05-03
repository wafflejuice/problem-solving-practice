PILLAR = 0
RIDGEPLATE = 1

def is_valid(n, mat, y, x, structure_type):
    can_place = False
    
    # 기둥
    if structure_type == 0:
        # 바닥 위에 있다.
        can_place |= y == 0
        # 보의 한쪽 끝 부분 위에 있다.
        can_place |= (x - 1 >= 0 and mat[y][x - 1][RIDGEPLATE] == True) or (mat[y][x][RIDGEPLATE] == True)
        # 다른 기둥 위에 있다.
        can_place |= y - 1 >= 0 and mat[y - 1][x][PILLAR]
    # 보
    else:
        # 한쪽 끝 부분이 기둥 위에 있다.
        can_place |= (y - 1 >= 0 and mat[y - 1][x][PILLAR]) or (y - 1 >= 0 and x + 1 <= n and mat[y - 1][x + 1][PILLAR])
        # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있다.
        can_place |= x - 1 >= 0 and mat[y][x - 1][RIDGEPLATE] and x + 1 <= n and mat[y][x + 1][RIDGEPLATE]
    
    return can_place

def solution(n, build_frame):
    mat = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    result = []
    
    for frame in build_frame:
        y, x = frame[1], frame[0]
        structure_type = frame[2]
        op = frame[3]

        # remove
        if op == 0:
            mat[y][x][structure_type] = False

            recheck_list = [[y, x], [y, x+1], [y, x-1], [y+1, x], [y+1, x-1]]
            recheck_list = list(filter(lambda pos:0<=pos[0]<=n and 0<=pos[1]<=n, recheck_list))

            can_remove = True
            for pos in recheck_list:
                if mat[pos[0]][pos[1]][PILLAR]:
                    can_remove &= is_valid(n, mat, pos[0], pos[1], PILLAR)
                if mat[pos[0]][pos[1]][RIDGEPLATE]:
                    can_remove &= is_valid(n, mat, pos[0], pos[1], RIDGEPLATE)
                
            if can_remove:
                result.remove([x, y, structure_type])
            else:
                mat[y][x][structure_type] = True
        # place
        else:
            if is_valid(n, mat, y, x, structure_type):
                mat[y][x][structure_type] = True
                result.append([x, y, structure_type])
        
    return sorted(result)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])) # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])) # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

# 58분 소요