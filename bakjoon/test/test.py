

import random

def make_colors(whole_color):
    color_list = []
    for i in range(4):
        color_list.append(random.choice(whole_color))
    return color_list
    
    
def select_color(whole_color):
    selected_colors = []
    print(''''(r)ed', '(b)lack', '(g)reen', '(y)ellow', '(o)range', '(p)urple', '(w)hite' 중에 선택하세요''')
    while len(selected_colors) < 4:
        SC = input().lower()
        if SC in whole_color:
            selected_colors.append(SC)
            print(selected_colors)
        else:
            print(''''잘못 입력하셨습니다.
                  (r)ed', '(b)lack', '(g)reen', '(y)ellow', '(o)range', '(p)urple', '(w)hite' 중에 선택하세요''')
    return selected_colors
        

def check_ans(color_list, selected_colors):
    again = True
    
    CL = color_list
    selected_colors2 = selected_colors
     
    CC_count = 0
    CI_count = 0
    right_index = []
    right_color = []
    
    if selected_colors == CL:
        again = False
    for z in range(0,4):
        if selected_colors[z] == color_list[z]:     #자꾸 color_list에서 답변과 일치한 항목이 사라지는데 무슨 문제?
            CC_count += 1                           
            right_index.append(z)
            right_color.append(selected_colors[z])
    
    for r in right_color:
        selected_colors2.remove(r)
        CL.remove(r)
    
        
    for x in range(0, 4-len(right_index)):
        if CL[x] in selected_colors2:
            selected_colors2.remove(CL[x])
            CI_count += 1
    
    print(f"Correct color in the correct place : {CC_count}")
    print(f"Correct color but in the wrong place : {CI_count}")
    
    
    return again
    
def main():
    whole_color = ['r', 'b', 'o', 'y', 'p', 'g', 'w']
    color_list = make_colors(whole_color)
    print(color_list)
    try_count = 0
    
    again = True
    while again:
        
        try_count +=1
        selected_colors = select_color(whole_color)
        again = check_ans(color_list, selected_colors)
        print(color_list, "왜?")
    
    print("축하합니다! 정답을 맞추셨습니다.")
    print(f"{try_count}번만에 맞추셨습니다!")
        
        
    
main()