test2tab = ['ac','bv','fb','er','yd','xi','nc','oj','pt','lu','de','wt','kc','ls','h','gg','oh','ux']


testtab = [1,35,8,78,45,65,21,35,52,95,85,7,77,9,3,57,8,2,1]

# Etape1:
testtab.sort()

# Etape2
print(testtab)
# [1 , 1, 2, 3, 7, 8, 8, 9, 21, 35, 35, 45, 52, 57, 65, 77, 78, 85, 95]

# Comment fonctionne la methode de rechcerche 

# Etape search  1
                                            # search 13
#  1   2  3  4  5  6  7  8   9  10  11  12  13  14  15  16  17  18   19
#                                   low            mid              high


# Etape search  2
                                # search 13
#  1   2  3  4  5  6  7  8   9  10  11   12  13  14  15  16  17  18   19
#                                   low mid high


# Etape search  3
                                        # search 13
#  1   2  3  4  5  6  7  8   9  10  11   12  13  14  15  16  17  18   19
#                                           low mid high



# Etape search  4
                                    # search 13
#  1   2  3  4  5  6  7  8   9  10  11   12  13  14  15  16  17  18   19
#                                       low mid high


test2tab.sort()
# ['ac', 'bv', 'de', 'er', 'fb', 'gg', 'h', 'kc', 'ls', 'lu', 'nc', 'oh', 'oj', 'pt', 'ux', 'wt', 'xi', 'yd']
#                                                       low                      mid                  high
print(test2tab)

# avant 
# apres 
# plus 
# plus2




def binarySearch(arr, val):
    if len(arr)==0 or (len(arr)== 1 and  arr[0]!= val):
        return False
    mid = arr[len(arr)//2]
    if val== mid:return True 
    if val< mid:return binarySearch(arr[:len(arr)//2],val)
    if val> mid:return binarySearch(arr[len(arr)//2+1:],val)
        
# testtab = [1,35,8,78,45,65,21,35,52,95,85,7,77,9,3,57,8,2,1]
print(binarySearch(testtab,65))#true
print(binarySearch(testtab,77))#true
print(binarySearch(testtab,0))#false
print(binarySearch(testtab,1))#true
print(binarySearch(testtab,21))#true
print(binarySearch(testtab,95))#true
print(binarySearch(testtab,45))#true