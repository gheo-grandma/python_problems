def intToBin(n):
    
    # base case: when we reach 2 // 2 = 1 it means we reached the last number of the list
    # since the largest number usually is included in the series, we need to append a 1 to the left
    
    if n // 2 == 0 or n // 2 == 1:
        return '1'
        
    # in order to avoid any sum between the numbers, the binary 
    # conversion works converting any 0 or 1 to string
    
    return (intToBin(n // 2) + f'{n % 2}')



print(intToBin(18))



# HOW IT WORKS

# binary numbers can be calculated by integer division recursively, 
# and the remainder is the binary value ( 0 / 1 )

# example for n = 17
# 17 // 2 = 8       17 % 2 = 1      binary = 1
# 8 // 2 = 4        8 % 2 = 0       binary = 01
# 4 // 2 = 2        4 % 2 = 0       binary = 001
# 2 // 2 = 1    ->  end of the function, so append a 1 to the left      binary = 1001