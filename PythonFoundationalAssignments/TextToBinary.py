"""Assignment-1-Najot Ta'lim Foundation : nol va bir bilan yozilgan textni binary formaga o'tkazing.
Masalan : "nol bir nol bir nol bir ikki nol nol " -> "01010100"
Agar sonlar soni 8 tadan kam bo'lsa xatolik berilsin. 
"""

"""Assignment-1-Najot Ta'lim Foundation : Convert the text which contain zero(nol in uzbek) and one(bir in uzbek) to binary form.
Masalan : "zero one zero one zero one two zero zero " -> "01010100"
Portray error if there aren't at least eight one and zeros. 
"""
"""Warning : This algorithm contained ready-to-use function named split() which is common algorithm of string forms. As well as it is created for 
Uzbek language condition. """
emptyString=""
data=input("Plase write some sentences with 'nol' and 'bir' : ")
splittedText=data.split(" ")
#Getting binary data in forms of String
for i in splittedText:
    if i.lower()=='nol':
        emptyString+="0"
    elif i.lower()=='bir':
        emptyString+="1"
    else: 
        continue
#Concluding if it is acceptable to output result using len() operator

if(len(emptyString)>=8):
    print(f"Our binary data is : {emptyString}")
else:
    print("Your providen data is not lenghty enough, please write at least 8 words which contain 'nol' or 'bir' ")