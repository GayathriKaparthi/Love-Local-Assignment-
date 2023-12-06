# repeated number in array which is more than n/3 times

from collections import Counter

def find_elements(arr):
    n=len(arr)
    k=n//3
    counts=Counter(arr)
    result=[]
    for num,counts in counts.items():
        if counts>k:
            result.append(num)
    return result
arr=list(map(int,input().strip().split()))
print(find_elements(arr))





