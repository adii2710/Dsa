######################################## CORRECT APPROACH ##########################################################
arr1=[1, 10, 100]
arr2=[1000]

arr_prefixes=set()
longest_prefix=0
for num in arr1:
    while num not in arr_prefixes and num>0:
        arr_prefixes.add(num)
        num =num//10
for num in arr2:
    while num not in arr_prefixes and num>0:
        num =num//10
    if num>0:
        longest_prefix=max(longest_prefix, len(str(num)))

#################################### TIME LIMIT EXCEED APPROACH ###################################################
def check(num1, num2, max_len):
    n1, n2=len(num1), len(num2)
    min_len=min(n1, n2)
    for i in range(min_len):
        if num1[i]==num2[i]:
            max_len = max(i+1, max_len)

        if num1[i]!=num2[i]:
            return max_len
        
    return max_len

max_len=0
n1=len(arr1)
n2=len(arr2)
for i in range(n1):
    num1=str(arr1[i])
    for j in range(n2):
        num2=str(arr2[j])
        max_len=check(num1, num2, max_len)