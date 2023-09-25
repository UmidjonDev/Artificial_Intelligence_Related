"""While Problem 1, 2: There is two distinctive line A and B(A>B). Write the aprehesible program that could find remnant line if polymath human beings attempt to fill up A line with miniscule B line"""
"""def remnant_and_division_finder():
    """"This is an manual fucntion that calculates remnant and divisions values of tho exceptional lines""""
    A_length=int(input("Write The overall lenght of A line : "))
    B_length=int(input("Type the measured length of B line : "))
    print(f"Divisional part is equal to : {int(A_length/B_length)}")
    print(f"Remnant part of A bluff line is indistinctive to : {A_length%B_length}")
#Calling ready-to-use function
remnant_and_division_finder()"""#Result is OK

"""While Problem 3 : There is two antitethic numbers a and b. Find their remnant part and division value without exploitting division or multiplication mathematical operators"""
"""While Problem 4 : Verify if plied number is the powered number of three"""#Could be found 
"""def division_without_operand(number1, number2) :
    elaborated_result=0
    while(number1>=0):
        number1-=number2
        elaborated_result+=1
    number1+=number2
    elaborated_result-=1
    return elaborated_result, number1


observational_number1=int(input("Write initial argument of division :"))
observational_number2=int(input("Write secondary argument of division : "))
print(division_without_operand(observational_number1, observational_number2))"""#Required answer to intriguing question is sought

"""While Problem 5 : There is the exclusive number which is equal to particular power of two. Find out the degree of this extraordinary number"""
"""def power_finder_of_exclusive_numbers(number, knumber):
    \"\"\"This is manual function which is assembled in order to find the power rate of demonstrated number according to the knumber\"\"\"
    seeking_power_rate=0
    while(number>1) :
        number/=knumber
        seeking_power_rate+=1
    if(number>0):
        seeking_power_rate-=1
    return f"Power rate of looking for number is equal to : {seeking_power_rate}"

number=int(input("Write down the number which is the powered digit of another unit : "))
knumber=int(input("Write down the \"another\" number : "))
print(power_finder_of_exclusive_numbers(number, knumber))"""#Answer to this little tough quest is outlandish

"""While Problem 6 : Look for the actual value of N! which is equal to N!=N*(N-2)*(N-4)*(N-6)*...2 or 1 according to the number which could be even or odd"""
"""def Factorial_Searching_Algorithm(Nnumber):
    result=1
    if(Nnumber%2==0) :
        while(Nnumber>=2):
            result*=Nnumber
            Nnumber-=2
    else:
        while(Nnumber>=1):
            result*=Nnumber
            Nnumber-=2
    return result

Nnumber=int(input("Write down the your imagined number : "))
print(f"N! of your daresayed(in another entailing) digit is equal to : {Factorial_Searching_Algorithm(Nnumber)}")"""#Portrayed answer to tough question is Magnificient

"""While Problem 7 : Look for the overall sum of A(1)=1, A(2)=2, A(k)=(A(k-2)+2A(k-1))/3 numerical series"""
A=[]
A[1]=1
A[2]=2
sum=3
k=3
n=int(input("It's my delight to recall the strict rule that provide the number which you would like to seek the sum value of given sequence : "))
while(k<=n):
    A[k]=(A[k-2]+2A[k-1])/3
    sum+=A[k]
if(n==2):
    print("The including-everything sum of digital sequence is")




