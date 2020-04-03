def left_rotation(a, k):
    alist = list(a)
    
    #print( alist[k:] )
    #print( alist[:k] )

    b = alist[k:]+alist[:k]
    return b

def right_rotation(a, k):
    alist = list(a)
    #print( alist[-k:] )
    #print( alist[:-k] )
    b = alist[-k:]+alist[:-k]
    return b
#...........................................
arr = [1, 2, 3, 4, 5, 6]
k = 3

#print("The left rotated Array is :")
#print( left_rotation(arr, k) )

print()

print("The Right rotated Array is : \n")
print( right_rotation(arr, k) )