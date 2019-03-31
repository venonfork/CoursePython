from random import randint
from time import time
# create array 
def create_array(size= 10, max = 20):
    return [randint(0,max)for _ in range(size)]

def quicksort(b):
    if len(b)<=1: return b
    smaller, equal, larger = [],[],[]
    # return smaller, equal, larger
    pivot = b[randint(0,len(b)-1)]
    # return f'voila {pivot}' 
    for x in b:
        if x <pivot: 
            smaller.append(x)
        elif x == pivot: 
            equal.append(x)
        else: 
            larger.append(x)
    return quicksort(smaller)+equal+quicksort(larger)


    # def merge_sort(b):
    #     if len(b)<=1: return a
    #     left, right = merge_sort(b[:len(b)/2]),merge_sort(b[:len(b)/2:])
    #     return merge(left, right)


n=[10,100,1000,10000,100000]
times = {'quick': []}
samples = 5


for size in n:
    tot_time = 0.0
    for v in range(samples):
        b = create_array(size, size)
        t0 = time()
        s = quicksort(b)
        t1= time()
        tot_time+=(t1-t0)
    times['quick'].append(tot_time/float(samples))

print("n\t Quicksort \t Autres")
print(40*"--")
for i, size in enumerate(n):
    print(f"{size}\t{times['quick'][i])%0.5f}")

# b = create_array()
# print(b)
# print(quicksort(b))
