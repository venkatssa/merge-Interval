
## merge interval
def mergeinterval(interval):
    interval.sort()
    temp_list = []
    temp_list.append(interval[0])
    for i in interval[1:]:
        if temp_list[-1][0] <= i[0] <= temp_list[-1][-1]:
            temp_list[-1][-1] = max(temp_list[-1][-1], i[-1])
        else:
            temp_list.append(i)

    for i in range(len(temp_list)):
        print(temp_list[i], end=' ')
    
arr = [[6,8], [1,9], [2,4], [4,7]]
mergeinterval(arr)
