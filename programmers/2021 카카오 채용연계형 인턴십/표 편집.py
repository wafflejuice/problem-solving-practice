def solution(n, k, cmd):
    records = [[i-1, i+1] for i in range(n)]
    acc = 0
    
    del_history = [-1 for _ in range(n)]
    del_idx = -1

    for op in cmd:
        op_split = op.split()
        op_code = op_split[0]
        
        if op_code == "U":
            acc -= int(op_split[1])
            
        elif op_code == "D":
            acc += int(op_split[1])
            
        elif op_code == "C":
            if acc > 0:
                for i in range(acc):
                    k = records[k][1]
            elif acc < 0:
                for i in range(-acc):
                    k = records[k][0]
            acc = 0
            del_idx += 1
            del_history[del_idx] = k
            if records[k][1] == n:
                records[records[k][0]][1] = records[k][1]
                k = records[k][0]
            else:
                records[records[k][0]][1], records[records[k][1]][0] = records[k][1], records[k][0]
                k = records[k][1]
            
        else:
            if acc > 0:
                for i in range(acc):
                    k = records[k][1]
            elif acc < 0:
                for i in range(-acc):
                    k = records[k][0]
            acc = 0
            last_del_idx = del_history[del_idx]
            del_idx -= 1
            if records[last_del_idx][1] == n:
                records[records[last_del_idx][0]][1] = last_del_idx
            else:
                records[records[last_del_idx][0]][1] = last_del_idx
                records[records[last_del_idx][1]][0] = last_del_idx

    ans = ["O" for _ in range(n)]
    for di in range(del_idx+1):
        ans[del_history[di]] = "X"

    return ''.join(ans)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))            # "OOOOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))  # "OOXOXOOO"
