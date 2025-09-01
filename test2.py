# def name():
#     print('***Malthika Janthong ID 6039010023***')

# def calculator():
#     total = float(input('Enter Student Total Score: '))
#     print(f"Total Score: {total}")  
#     score = float()
#     while total < 50 :
#         print(score)
#     total = float(input('Enter Student Total Score: '))
#     print(f"Total Score: {total}")

# name()
# calculator()

# 1.1 ฟังก์ชันแสดงชื่อ - นามสกุล และรหัสนักเรียน
def display_student_info():
    print('***Malthika Janthong ID 6039010023***')

# 1.2 ฟังก์ชันตรวจสอบคะแนนของนักเรียน
def check_student_score():
    total_score = 0
    
    while True:
        score = float(input('Enter Student  Score: '))
        
        if score > 50:
            total_score += score
            print(f"Score: {score}")
        else:
            print('*************************************')
            break

# 1.3 เรียกใช้ฟังก์ชันทั้งสอง
display_student_info()
check_student_score()
