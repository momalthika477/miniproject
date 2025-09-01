def name():
    print('***Malthika Janthong ID 6039010023***')

def BMI_calculator():
    
    Weight = float(input('Enter Student Weight : '))
    Height = float(input('Enter Student Height : '))
    Height1 = Height/100
    Height2 = Height1**2
    total = Weight/Height2

    print('*************************************')
    print(f"Weight : {Weight}")
    print(f"Weight : {Height}")
    print(f"BMI : {total}")

    
    if total < 18.5:
        print('>>You are underweight.<<')
    elif 25.0 <= total < 35.0:
        print('>>You are slightly overweight.<<')
    else: 
        print('>>You are severely obese<<')
    print('*************************************')

name()
BMI_calculator()
