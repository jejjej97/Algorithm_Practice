# 정렬
# list = [8,5,6,2,4]
# list = [5,15,12,66,2,6,5,9]
list = [2,6,10,61,21,63,66,85,125,13,514,122,55,12,67,278,32,425,16,28,84,99,3,1]

# 삽입 정렬
def Insert_Sort() :
    print("Insert_Sort\n",)
    회전수 = 0
    num = 1
    for i in range(len(list)-1):
        회전수 += 1
        print(회전수,"회전 시작")
        a = list[num]
        num += 1
        for i in range(num):
            if list[i] > a:
                list.insert(i, a)
                list.pop(num)
                break
        print(회전수,"회전 결과:",list,"\n")

# 선택 정렬
def Select_Sort() :
    print("Select_Sort\n")
    회전수 = 0
    for i in range(len(list)-1):
        회전수 += 1
        print(회전수, "회전 시작")
        num = 1 + i
        for ii in range(len(list)-1-i):
            a = list[i]
            if list[i] > list[num]:
                list[i] = list[num]
                list[num] = a
                num+=1
                print(">>",list)
            else:
                num+=1
        print(회전수,"회전 결과:",list,"\n")

# 버블 정렬
def Bubble_Sort() :
    print("Bubble_Sort\n")
    회전수 = 0
    for i in range(len(list) - 1):
        회전수 += 1
        print(회전수, "회전 시작")
        num = 1
        for ii in range(len(list) - 1 - i):
            a = list[ii]
            if list[ii] > list[num]:
                list[ii] = list[num]
                list[num] = a
                num += 1
                print(">>", list)
            else:
                num += 1
        print(회전수, "회전 결과:", list, "\n")

if __name__ == "__main__":
    print("초기 상태:", list, "\n")
    # Insert_Sort()
    # Select_Sort()
    Bubble_Sort()