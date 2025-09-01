def Salary_calculator():
    bonus1 = salary*15/100
    total=salary+bonus1
    print(f"Earnings with Bonus : {total}")
    print('*************************************')



while True:
    id = int(input('Enter Employee ID : '))
    if id == 0:
        break  
    else:
        name = (input('Enter Employee Full name : '))
        salary = float(input('Enter Employee Salary : '))

        Salary_calculator()
