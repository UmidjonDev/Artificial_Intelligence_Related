"""
Foundation Assignment 2: Berilgan matn ichidan raqamlarni toping va ularni yig'indisini chiqaring.
Masalan :
Input : "Men 2-iyul kuni 5 ta do'slarim bilan 6 ta boshqa mahallani bollari bilan futbol o'ynashga bordik."
Output : 13 
"""

"""
Foundation Assignment 2: Find numbers from give text and output the sum value of them.
For instance :
Input : "Men 2-iyul kuni 5 ta do'slarim bilan 6 ta boshqa mahallani bollari bilan futbol o'ynashga bordik."
Output : 13    - > 2+5+6
"""

inputString=input("Write some word or string : ")
emptyIntString=""
arrayInt=[]
sum=0
#Splitting Integer datas from String Data
for i in inputString:
    if i=='0':
        emptyIntString+='0'
    elif i=='1':
        emptyIntString+='1'
    elif i=='2':
        emptyIntString+='2'
    elif i=='3':
        emptyIntString+='3'
    elif i=='4':
        emptyIntString+='4'
    elif i=='5':
        emptyIntString+='5'
    elif i=='6':
        emptyIntString+='6'
    elif i=='7':
        emptyIntString+='7'
    elif i=='8':
        emptyIntString+='8'
    elif i=='9':
        emptyIntString+='9'
    else:
        if(emptyIntString==''):
            continue
        else:
            arrayInt+=[emptyIntString]
            emptyIntString=""
if(emptyIntString==''):
    pass
else:
    arrayInt+=[emptyIntString]
    emptyIntString=""
#Finding sum value of these integers
for a in arrayInt:
    sum+=int(a)
print(f"Sum value of numbers which are given in inputted String is :{sum}")