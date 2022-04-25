def solution(numbers, hand):
    def dist(pos0, pos1):
        return abs(pos0[0]-pos1[0])+abs(pos0[1]-pos1[1])

    num_pos=dict()
    num_pos[0]=(1,0)
    for num in range(1, 10):
        num_pos[num]=((num-1)%3,(9-num)//3+1)

    left_thumb_pos = [0,0]
    right_thumb_pos=[2,0]

    order=[]
    for num in numbers:
        current_order=None

        if num in [1, 4, 7]:
            current_order = "L"
        elif num in [3, 6, 9]:
            current_order = "R"
        else:
            left_dist = dist(num_pos[num], left_thumb_pos)
            right_dist = dist(num_pos[num], right_thumb_pos)

            if left_dist==right_dist:
                if hand == "left":
                    current_order="L"
                else:
                    current_order="R"
            elif left_dist<right_dist:
                current_order="L"
            else:
                current_order="R"

        order.append(current_order)

        if current_order == "L":
            left_thumb_pos=num_pos[num]
        else:
            right_thumb_pos=num_pos[num]

    return ''.join(order)

inputs=[
    [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],   #"LRLLLRLLRRL"
    [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],	#"LRLLRRLLLRR"
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"],	    #"LLRLLRLLRL"
]

for input in inputs:
    print(solution(input[0], input[1]))
