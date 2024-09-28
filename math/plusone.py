digits=[9,9,9,9]

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i]<9:
            digits[i] +=1
            return digits
        digits[i]=0
    new=[0]*(len(digits)+1)
    new[0]=1
    return new

print(plusOne(digits))

# here our simple approach is like:
# if there is any number less than 9 then there is no problem we can directly add +1 to last index number
# but it may happen like all numbers [9,9,9,9,9,9] is such case all the numbers will be updated and also the
# size of digits array will change to tackle this we can replace all the 9's by 0 
# but now the size of total number after adding 1 has increased, 
# so create new array of len(digits)+1 and initialize it by 0 and change 1st index's number to 1 