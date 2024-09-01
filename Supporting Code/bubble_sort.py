array = [4,1,3,9,7]

for i in range(0, len(array)):
    for j in range(0, len(array)-1-i):
        if(array[j] > array[j+1]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
        
for number in array:
    print(number)