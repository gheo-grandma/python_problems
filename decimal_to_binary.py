def intToBin(n):
    
    # base case: the number is either odd or even
    # this condition checks if the last number is a 0 or a 1
    if n // 2 == 0 or n // 2 == 1:
        return '1'
        
    # in order to avoid any sum between the numbers, the binary 
    # conversion works converting any 0 or 1 to string
    
    return (intToBin(n // 2) + f'{n % 2}')



print(intToBin(17))



# HOW IT WORKS

# hhh