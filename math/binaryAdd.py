a = "1"
b = "11"

########################################################### using carry approach ####################################################
an=len(a)
bn=len(b)
mi=min(an, bn)
ma=max(an, bn)

#here set the length of both the string equal i.e a='01' and b='11'
if mi==an:
    a ='0'*abs(an-bn)+a
else:
    b ='0'*abs(an-bn)+b

ma_arr=['0']*ma
c=0
res=0

for i in range(-1, -ma-1, -1):
    if a[i]=='1' and b[i] == '1': #check only whether a[i] and b[i] == 1 ##there will be two cases either carry will be there or carry will be generated
        if c==1:                    # if already carry present from prev calculations so 1+1+1= 1 and c=1
            ma_arr[i]='1'
        else:
            ma_arr[i]='0'           #else it would happen that no carry from previous calculations so the carry will be generated here!!
            c=1
    else:                           #else simply perform math opr 
        res=int(a[i])+int(b[i])
        if c==1 and res==1:
            ma_arr[i]='0'
        else:
            ma_arr[i] = str(res+c)      #here whether carry present or not add it to result
            c=0

#finally checking whether carry still present or not if yes then insert the carry i.e '1' in starting and return string
if c==0:
    final=''.join(ma_arr)
    
else:
    ma_arr=['1']+ma_arr[0:]
    final=''.join(ma_arr)


################################### using int and bin function approach ##############################################################
# x=int(a, 2)
# y=int(b, 2)
# z=x+y

# bi=bin(z)[2:]
# print(bi)