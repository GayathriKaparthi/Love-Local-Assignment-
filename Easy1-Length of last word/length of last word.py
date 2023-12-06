def length(str):
    list1=list(str.split(" "))
    return len(list1[-1])
str=input()
print("Length of last word is:",length(str))