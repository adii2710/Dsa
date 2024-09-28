roman="LVIII"

def R2I(roman):
    prev=0  
    data={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    num=0

    for char in roman:
        curr=data[char]
        if prev<curr:
            num += curr -2*prev
        else:
            num +=curr

        prev=curr
    return num

print(R2I(roman))