import array
def binarysearch(arr,l,r,x):
    while l <=r:
        mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 2
    return -1

def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j+1]<arr[j]:
                temp =arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

def selectionsort(arr):
    for i in range(len(arr)-1):
        minpos = i
        for j in range(i,len(arr)):
            if arr[j]<arr[minpos]:
                minpos = j

        temp =arr[i]
        arr[i]=arr[minpos]
        arr[minpos]=temp

def deletion(arr):
    n=len(arr)
    for i in range(n-1):
        arr[i]=arr[i+1]
        n=n-1
    for i in range(n):
        print(arr[i])    

def search(arr,n,value):
    
    for i in range(len(arr)-1):
        if arr[i]==value:
            return i
    return -1    

def sorted(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n-1):
            if arr[i]<arr[j]:
                return arr[i]
            else:
                return arr[j] 
    print(arr)               


if __name__ =='__main__':
	arr = [2,3,6,6,5]
    sorted(arr)
    
	#result = search(arr)
    #if result != -1:
    

          
         
    #bubblesort(arr)
    #selectionsort(arr)
    #arr.insert(0,9)
    #print(arr)
    #x=int(input('Enter your number:'))
    #result = binarysearch(arr,0,len(arr)-1,x)


    

    




    

      
