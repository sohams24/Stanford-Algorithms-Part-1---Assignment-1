import math

def countSplitInv(intlist, leftfirst, leftlast, rightfirst, rightlast):
    '''
    This method counts the number of split inversions in the 2 sorted halves of the list
    Input : list, first index of left half, last index of left half, first index of right half, last index of right half
    Output : number of split inversions
    '''

    index = leftfirst
    sortedList = []
    invCount = 0

    while leftfirst <= leftlast and rightfirst <= rightlast:
        #while more elements in the left and right halves
        if intlist[leftfirst] <= intlist[rightfirst]:
            # if the first unchecked element in left half is less than the first unchecked element in right half
            sortedList.append(intlist[leftfirst])
            leftfirst += 1
        # if the first unchecked element in right half is less than the first unchecked element in left half
        else:
            sortedList.append(intlist[rightfirst])
            rightfirst += 1
            # whenever this condition is true, we increment the inversions count with the number of unchecked elements remaining in the left half
            invCount += leftlast - leftfirst + 1

    while leftfirst <= leftlast:
        #while more elements in the left half
        sortedList.append(intlist[leftfirst])
        leftfirst += 1

    while rightfirst <= rightlast:
        #while more elements in the rigt half
        sortedList.append(intlist[rightfirst])
        rightfirst += 1

    #copying the sorted sub-list in the original list
    for num in sortedList:
        intlist[index] = num
        index += 1

    return invCount



def sortAndCount(intlist, first, last):

    '''
    this function sorts and counts the number of inversions in a list
    input: list, length, index of first, index of center, index of last
    output: number of inversions
    '''

    totalInv = 0
    #terminating condition
    if last > first:
        middle = math.floor((first + last)/2)   #get middle index
        left = sortAndCount(intlist, first, middle)     #number of inversions in left half
        right = sortAndCount(intlist, middle+1, last)   #number of inversions in right half
        split = countSplitInv(intlist, first, middle, middle+1, last)   #number of split inversions
        totalInv = left + right + split     #adding all three inversions count

    return totalInv


fo = open('IntegerArray.txt','r')
intlist=[]
for line in fo.readlines():
    intlist.append(int(line))
length = len(intlist)
print("The total number of inversions are {}".format(sortAndCount(intlist, 0, length-1)))


