def solution(record):
    id_nickname=dict()
    txs=[]
    for tx in record:
        words=tx.split()
        if words[0] == "Enter":
            id_nickname[words[1]]=words[2]
            txs.append(("Enter", words[1]))
        elif words[0] == "Leave":
            txs.append(("Leave", words[1]))
        else:
            id_nickname[words[1]]=words[2]
    
    result=[]
    for tx in txs:
        nickname=id_nickname[tx[1]]
        if tx[0] == "Enter":
            result.append(nickname+"님이 들어왔습니다.")
        else:
            result.append(nickname+"님이 나갔습니다.")
    
    return result