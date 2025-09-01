import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("ลบเสร็จสิ้น")
else:
    print("The file does not exist")






# f = open("myfile.txt", "x")
# f.write("“Content of file from x mode!")
# f = open("myfile.txt", "r")
# print(f.read())
# f.close()



# f = open("demofile2.txt", "w")
# f.write("มีเนื้อหาใหม่ที่น่าสนใจกว่านี้!!")
# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()





# f = open("demofile2.txt","a",encoding="utf-8")
# f.write("เพิ่มข้อมูลที่คุณสนใจ!")
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()


# f = open("demotext.txt","r",encoding="utf-8")
# print(f.readline())




# f = open("demotext.txt","r")
# print(f.read(5))


# f = open("demotext.txt","r")
# print(f.read())


