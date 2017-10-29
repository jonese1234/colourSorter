import random
from PIL import Image
import colorsys
import time

width = 30
height = 1
pixHeight = 30
totalList = []
glBaseInt = 0
glTotalInt = 0
compleatedRow = []
currentOne = 0


def hsv2rgb(h, s, v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h/360.0, s, v))

def makeRainbowNew():
    rainNum = 1
    rainbow = []

    while rainNum <= 360:
        rainbow.append(rainNum-1)
        rainNum += (360/width)
    global compleatedRow
    compleatedRow = rainbow.copy()
    rainBowList = []

    for x in range(0, pixHeight):
        rainBowList.append(rainbow.copy())

    #print(rainBowList)
    return rainBowList


def makeRandomRainbowNew():
    rainbow = makeRainbowNew()
    randomRainbow = []
    for x in rainbow:
        rlist = sorted(x, key=lambda x: random.random())
        randomRainbow.append(rlist)
    return randomRainbow

def quick_sort_iterative(list_, left, right):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left, right))

    # Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))

def quick_sort_recursive(list_, left, right):
    """
    Quick sort method (Recursive)
    """
    if right <= left:
        return
    else:
        #Get pivot
        piv = partition(list_, left, right)
        #Sort left side of pivot
        quick_sort_recursive(list_, left, piv-1)
        #Sort right side of pivot
        quick_sort_recursive(list_, piv+1, right)

def partition(list_, left, right):
    """
    Partition method
    """
    # Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right

    while 1:
        while i <= j and list_[i] <= piv:
            i += 1
        while j >= i and list_[j] >= piv:
            j -= 1
        if j <= i:
            break
        # Exchange items
        list_[i], list_[j] = list_[j], list_[i]
        # make Image
        makeImageList(list_.copy())
    # Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    # Make image
    makeImageList(list_.copy())
    return j

def makeImageList(list_):
    global glBaseInt, glTotalInt
    if glBaseInt == len(totalList):
        totalList.append([])
        for x in range(1, currentOne):
            totalList[glBaseInt].append(compleatedRow.copy())
        glTotalInt += 1
    totalList[glBaseInt].append(list_)
    glBaseInt += 1

def makeLargeImg(list, name):
    im = Image.new("RGB", (width, pixHeight))
    flatList = [item for sublist in list for item in sublist]
    flatRGBList = [hsv2rgb(x, 1, 1) for x in flatList]
    imgRBGList = [tuple(x) for x in flatRGBList]

    im.putdata(imgRBGList, scale=8.0)
    im.save(name + ".png", "PNG")

def imagePrint(list_):
    i = 1
    for x in list_:
        makeLargeImg(x, "record\\test8\\"+str(i))
        i += 1

def main():
    timeStart = time.clock()
    rndRainbow = makeRandomRainbowNew()
    #print(rndRainbow)


    for x in rndRainbow:
        global glBaseInt, currentOne
        glBaseInt = 0
        currentOne += 1
        quick_sort_recursive(x, 0, len(x)-1)
        for y in totalList:
            if len(y) < currentOne:
                    y.append(compleatedRow.copy())
    timemid = time.clock()
    print("Took this long to Sort: " + str(timemid-timeStart))

    imagePrint(totalList)

    #print(rndRainbow)
    timeEnd = time.clock()
    elapsed = timeEnd - timeStart

    print("It took Sort and print: " + str(elapsed))


main()
