def solution(places):
    def is_place_legit(place):
        for yi in range(5):
            for xi in range(5):
                if place[yi][xi]=="P":
                    surrounding_positions=[
                        (yi, xi + 1),
                        (yi, xi - 1),
                        (yi + 1, xi),
                        (yi - 1, xi),
                        (yi, xi + 2),
                        (yi, xi - 2),
                        (yi + 1, xi + 1),
                        (yi + 1, xi - 1),
                        (yi - 1, xi + 1),
                        (yi - 1, xi - 1),
                        (yi + 2, xi),
                        (yi - 2, xi)
                    ]
                    surrounding_positions=list(filter(lambda pos:0<=pos[0]<5 and 0<=pos[1]<5, surrounding_positions))

                    for position in surrounding_positions:
                        if place[position[0]][position[1]] == "P":
                            if abs(position[0]-yi)+abs(position[1]-xi)==1:
                                return 0
                            else:
                                if position[0]==yi:
                                    if xi+2==position[1]:
                                        if place[yi][xi+1]!="X":
                                            return 0
                                    if xi-2==position[1]:
                                        if place[yi][xi-1]!="X":
                                            return 0
                                elif position[1]==xi:
                                    if yi+2==position[0]:
                                        if place[yi+1][xi]!="X":
                                            return 0
                                    if yi-2==position[0]:
                                        if place[yi-1][xi]!="X":
                                            return 0
                                else:
                                    if place[yi][position[1]]!="X":
                                        return 0
                                    if place[position[0]][xi]!="X":
                                        return 0
        return 1

    answer = []
    for place in places:
        answer.append(is_place_legit(place))

    return answer

input=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(input)) # [1, 0, 1, 1, 1]

# 36 minutes
# 36분이나 걸릴 문제였나...?