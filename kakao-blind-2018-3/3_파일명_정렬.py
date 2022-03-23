import re

def solution(files):
    splitted_file_names = []
    for file_name in files:
        splitted_file_names.append(do_split_file_name(file_name))

    sorted_split_file_names = sort_file_names_builtin(splitted_file_names)
    answer = prettify_split_file_names(sorted_split_file_names)
    
    return answer

def prettify_split_file_names(split_file_names):
    file_names = []
    for sfn in split_file_names:
        file_names.append(sfn[0]+sfn[1]+sfn[2])
    return file_names

def sort_file_names(split_files_names):
    return merge_sort(split_files_names)

def sort_file_names_builtin(split_file_names):
    split_file_names = sorted(split_file_names, key=lambda split_file_name: int(split_file_name[1]))
    split_file_names = sorted(split_file_names, key=lambda split_file_name: split_file_name[0].lower())
    return split_file_names

def merge_sort(l):
    if len(l) <= 1:
        return l
    
    mid = len(l)//2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    
    li, ri = 0, 0
    merged_list = []
    while li < len(left) and ri < len(right):
        if compare_func(left[li], right[ri]) < 0:
            merged_list.append(left[li])
            li += 1
        elif compare_func(left[li], right[ri]) > 0:
            merged_list.append(right[ri])
            ri += 1
        else:
            merged_list.append(left[li])
            li += 1
            # merged_list.append(right[ri])
            # ri += 1
    
    if li < len(left):
        merged_list += left[li:]
    elif ri < len(right):
        merged_list += right[ri:]
    
    return merged_list

def compare_func(a, b):
    if a[0].lower() < b[0].lower():
        return -1
    elif a[0].lower() > b[0].lower():
        return 1
    
    return int(a[1]) - int(b[1])

def do_split_file_name(file_name):
    p = re.compile('([^0-9]+)([0-9]+)([a-zA-Z0-9 .-]*)')
    m = p.match(file_name)
    
    head = m.group(1)
    number = m.group(2)
    tail = m.group(3)
    
    return [head, number, tail]

sample_inputs = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
]

for s in sample_inputs:
    print(solution(s))
    
# custom_inputs = [
#     ["B00000 Superfortress", "---010bar020.zip", "---5-A-10 Thunderbolt II", "F-14 Tomcat"],
#     ['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT']
# ]
#
# for c in custom_inputs:
#     print(solution(c))
    
# 2회차 : 1시간 20분