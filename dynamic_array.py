def dynamicArray(n, queries):
    arr = []
    for i in range(0,n):
        arr.append([])
    lastAnswer = 0
    answers = []
    for query in queries:
        num,x,y = [int(v) for v in query]
        if num == 1:
            arr[(x ^ lastAnswer) % n].append(y)
        else:
            idx = (x ^ lastAnswer) % n
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    return answers

print(dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]))