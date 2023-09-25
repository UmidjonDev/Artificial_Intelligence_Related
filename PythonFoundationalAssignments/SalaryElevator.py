"""
Foundation 4 assignment : Create an object called Employee and Enterprise-employee class which get inheritance from Employee class. Employee class should have 
surname, position, salary attributes where Enterprise_employee class should have excess rating attribute. Ok, according to the rating value, change the salary value of employee.
Index for changing salary value : 
    rating >= 65 and rating < 75  -> Elevate the value by 20%;
    rating>=75 and rating<90   -> Elevate the value by 40%;
    obj.rating>=90 and obj.rating<=100  -> Elevate the value by 60%;
"""

"""
Foundation 4 assignment : Employee class va Enterprise_Employee classini yarating. Ikkinchi class birinchi classdan inheritance olishi kerak. Employee classi eng avvalo
suname("Familiya"), postion("Kasbi"), salary("Oylik maosh") kabi attributlarni qabul qilib olishi kerak. Enterprise_employee classi esa rating("Baho") attributini ham qabul qilishi kerak.
Sizning vazifangiz berilgan rating qiymatiga ko'ra, ishchining maoshini oshirish.
    rating >= 65 and rating < 75  -> 20% ga oshiring ;
    rating>=75 and rating<90   -> 40% ga oshiring;
    obj.rating>=90 and obj.rating<=100  -> 60% ga oshiring;
"""

#Object Creation
def salaryCounter(obj):
    if obj.rating>=60 and obj.rating<75:
        obj.salary*=1.2
    elif obj.rating>=75 and obj.rating<90:
        obj.salary*=1.4
    elif obj.rating>=90 and obj.rating<=100:
        obj.salary*=1.6
    elif obj.rating>100 or obj.rating<0:
         print("Give appropriate number for rating")
         obj.salary=0
    else:
        obj.salary=obj.salary
    return obj.salary
for i in range(5):
    objectName=input(f"Please enter the surname of {i+1} Employee :")
    objectPosition=input("Please enter the position of Employee :")
    objectSalary=input("Please enter the salary of employee : ")
    objectRating=input("Please enter the rating of employee(Rating should be in 0-100 scale) : ")
    class Employee:
        surname=objectName
        position=objectPosition
        salary=int(objectSalary)
    class Enterprise_employee(Employee):
        rating=int(objectRating) #Rating should be in scale 0-100

    employee=Enterprise_employee()
    employee.salary=salaryCounter(employee)
    print(f"Employee {i+1} surname : {employee.surname}")
    print(f"Employee position : {employee.position}")
    print(f"Employee rating : {employee.rating}")
    print(f"Employee new salary : {employee.salary}")