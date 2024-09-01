def threeConsecutiveOdds(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    impar = 0

    for num in arr:
        if num % 2:
            impar += 1
        else:
            impar = 0

        if impar == 3:
            return True
        
    return False

print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))