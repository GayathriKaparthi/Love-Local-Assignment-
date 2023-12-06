def count_total_no_of_ones(n):
    count=0
    for num in range(1,n+1):
        str1=str(num)
        count+=str1.count("1")
    return count
n=int(input())
print(count_total_no_of_ones(n))
