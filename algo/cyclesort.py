
def cyclesort(lst):
    for i in range(len(lst)):
        if i != lst[i]:
            n = i
            while 1: 
                tmp = lst[int(n)]
                if n != i:
                    lst[int(n)] = last_value
                    from main import makeImageList
                    makeImageList(lst.copy())
                else:
                    lst[int(n)] = None
                    from main import makeImageList
                    makeImageList(lst.copy())
                last_value = tmp
                n = last_value
                if n == i:
                    lst[int(n)] = last_value
                    from main import makeImageList
                    makeImageList(lst.copy())
                    break


