# find the number of possible partition to arrange n elements in partition up to m number of elements



def n_partition(n, m):
    # base case: 
    # if n is negative, there's no element to continue
    # if m is 0, no partition will be allowed to have any element in it
    
    if n < 0 or m == 0:
        return 0
        
        
    # base case:
    # if n is 1 or 0 there's only one partition we can make
    # if m is 1, there's only one possible partition we can make
    if n < 2 or m == 1:
        return 1
    
    return n_partition(n - m, m) + n_partition(n, m - 1)
    
    
    

print(n_partition(9, 4))



# HOW THIS WORKS

# any n_partition(n, m) is formed by a combination of 2 parts:
    # the solution calculated with n_partition(n, m-1) and the solution calculated with n_partition(n - m, m)
    
    # suppose we start with n = 5 and m = 3
    
    # these are the partitions we can make
    # o o o | o o 
    # o o o | o | o
    # o o   | o o | o
    # o o   | o | o | o
    # o     | o | o | o | o
    
    # if we removed the solutions where the first partition has 3 elements, we are left with this
    
    # o o   | o o | o
    # o o   | o | o | o
    # o     | o | o | o | o
    
    # which is actually the solution for n_partition(5, 2)
    
    # so, n_partition(5, 3) can be written as
    
    # o o o | o o 
    # o o o | o | o
    # n_partition(5, 2)
    
    # to get the number of possible combinations from the top, we need to remove the first m elements from 
    # the current solution, so that we can calculate the difference with the bottom 
    
    # m = 3, so 3 elements are cut
    
    # x x x | o o               -->     o o
    # x x x | o | o             -->     o | o
    
    # this is a new set of solution, to be more specific n_partition(2, m), where m is still 3
    # if we keep going on with our functionand keeping in mind our base cases 
    # we can easilly calculate n_partition(n-m, m) and n_partition(n, m-1):
    
    # n_partition(5, 3) = n_partition(2, 3) + n_partition(5, 2)
        # n_partition(2, 3) = n_partition(-1, 3) + n_partition(2, 2)
        # n_partition(2, 3) = 0 + n_partition(0,2) + n_partition(2, 1)
        # n_partition(2, 3) = 0 + 1 + 1 = 2
        
        # n_partition(5, 2) = n_partition(3, 2) + n_partition(5, 1)
        # n_partition(5, 2) = n_partition(1, 2) + n_partition(3, 1) + 1
        # n_partition(5, 2) = 1 + 1 + 1 = 3
        
    # n_partition(5, 3) = 2 + 3 = 5