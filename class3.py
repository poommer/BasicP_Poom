# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("ไม่กิน")



# score = int(input())

# if score >= 0:
#     if score <= 100:
#         if score >= 80:
#             print("A")
#         if score >= 70:
#             if score < 80:
#                 print("B")
#         if score >= 60:
#             if score < 70:
#                 print("C")
#         if score >= 50:
#             if score < 60:
#                 print("D")
#         if score < 50:
#             print("F")


# for i in range(1,10,2):
#     print(i)


# i = 0
# while i < 8:
#     print("Hello")
#     i = i + 1

# while True :
#     choice = int(input("กรอก 1 เพื่อบวก, กรอก 2 เพื่อออก: "))
    
#     if choice == 1:
#         num = int(input("จำนวนครั้งที่ต้องการบวก: "))
#         sumation = 0

#         for i in range(num):
#             num1 = int(input("กรอกเลข: "))
#             sumation = sumation + num1

#         print("ผลลัพธ์", sumation)

#     if choice == 2:
#         print("บาย")
#         break


while True:
    choice = int(input("กรอก 1 เพื่อสู้, กรอก 2 เพื่อออก: "))

    if choice == 1:
        monster = 100

        weapon1 = 50
        weapon2 = 20
        weapon3 = 100

        turn = int(input("จำครั้งที่ต้องการตี: "))

        for i in range(turn):
            print("รอบที่",i+1,"/", turn)
            select = int(input("เลือกอาวุธ\n 1.รถถัง\n 2.เรือดำน้ำ\n 3.พิซซ่า1112\n"))
            if select == 1:
                monster -= weapon1
            elif select == 2:
                monster -= weapon2
            elif select == 3:
                monster -= weapon3

            if monster < 0 :
                print("มอนเตอร์ HP ติดลบ (HP + 20)")
                monster = 20
            elif monster == 0 :
                print("มอนเตอร์ตายแล้ว!")
                break
            print("HP มอนเตอร์ = ", monster)

        if monster > 0 :
            print("มอนเตอร์ไม่ตาย คุณตายแล้ว")

    elif choice == 2:
        print("ออกจากเกมแล้ว")
        break

    else:
        print("ตัวเลือกไม่ถูกต้อง (เลือก 1 หรือ 2 เท่านั้น)")