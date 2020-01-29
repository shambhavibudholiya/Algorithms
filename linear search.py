def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            print(i)
    return -1
list = [1,2,3,4,5,6,7,8,9,0]
n = 7
search(list,n)