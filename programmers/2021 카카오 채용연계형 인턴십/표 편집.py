def solution(n, k, cmd):
    active_records = [i for i in range(n)]
    active_idx = k
    acc = 0
    
    del_history = [None for _ in range(200000)]
    del_idx = -1

    for op in cmd:
        op_split = op.split()
        op_code = op_split[0]
        
        if op_code == "U":
            acc -= int(op_split[1])
            
        elif op_code == "D":
            acc += int(op_split[1])
            
        elif op_code == "C":
            active_idx += acc
            acc = 0
            del_idx += 1
            del_history[del_idx] = (active_records[active_idx], active_idx)
            if active_idx == len(active_records)-1:
                active_records.pop(-1)
                active_idx -= 1
            else:
                active_records.pop(active_idx)
            
        else:
            active_idx += acc
            acc = 0
            last_del_val, last_del_idx = del_history[del_idx]
            del_idx -= 1
            if last_del_idx <= active_idx:
                active_idx += 1
            active_records.insert(last_del_idx, last_del_val)

    ans = ["O" for _ in range(n)]
    for di in range(del_idx+1):
        ans[del_history[di][0]] = "X"

    return ''.join(ans)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))            # "OOOOXOOO"
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))  # "OOXOXOOO"
