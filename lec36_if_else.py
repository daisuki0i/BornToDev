'''
HW

ตัวอย่าง
 ตัดสินใจว่าเที่ยงนี้จะกินอะไรดี?
    ถ้ามีเงินมากกว่า 100 บาท จะไปกิน KFC 🍗
    ถ้ามากกว่า 50 บาท ไปกินตามสั่งหน้าปากซอยดีกว่า 🍛
    ถ้ามีเงินไม่ถึง 20 บาท ว่าจะไปกินมาม่า 🍜
    ถ้าไม่มีเงินเลย ไปบอกแม่ดีกว่า 👱‍♀

ตอบ
ตัดสินใจ about เอนไก่
    ถ้าเราติ่งเอนไฮเพน(เงื่อนไข) 
    เราจะไปคอน
    แต่ ถ้าเราไม่ติ่งเอนไฮเพน(เงื่อนไข)
    เราจะไปคอนวงอื่น
'''

money = 100
if money > 300:
    print("GO TO KFCCCCC")
else:
    print("SO SAD T_T")

print()

# username ถูกต้อง
usernameInput = input("Username : ")
passwordInput= input("Password : ")
if usernameInput == "worachisa":
    print("DONE")
else:
    print("ERROR")

print()

# ถูกทั้งusername and password
usernameInput = input("Username : ")
passwordInput= input("Password : ")
if usernameInput == "worachisa" and passwordInput == "12345678":
    print("DONE")
else:
    print("ERROR")

print()

# username ถูกต้องแต่ password ไม่ถูก
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if passwordInput == "12345678":
    print("DONE")
else:
    print("ERROR")

print()

'''
if เงื่อนไข : ถ้าเงื่อนไขเป็นจริงจะทำงานในส่วนของif
else : ถ้า if ไม่เป็นจริง เงื่อนไขจะม่ทำต่อใน else
elif : จะทำงานก็ต่อเมื่อเงื่อนไขด้านบนเป็นเท็จ
'''

if False:
    print("First Condition")
elif True:
    print("Second Condition")
elif False:
    print("Third Condition")
else:
    print("Else Section")

print()

money = int(input())
if money > 300:
    print("Good")
elif True:
    print("Saddd")
else:
    print("error")

print()

'''
ตัวอย่างการตัดสินใจหลากหลายเงื่อนไข

ถ้าคะแนน
    มากกว่าหรือเท่ากับ 80 จะได้เกรด A
    มากกว่าหรือเท่ากับ 75 จะได้เกรด B+
    มากกว่าหรือเท่ากับ 70 จะได้เกรด B
    มากกว่าหรือเท่ากับ 65 จะได้เกรด C+
    มากกว่าหรือเท่ากับ 60 จะได้เกรด C
    มากกว่าหรือเท่ากับ 55 จะได้เกรด D+
    มากกว่าหรือเท่ากับ 50 จะได้เกรด D
    น้อยกว่า         50 จะได้เกรด F
'''

score = int(input("Add Score(100) : "))
if score >= 80:
    print("A")
elif score >= 75:
    print("B+")
elif score >= 70:
    print("B")
elif score >= 65:
    print("C+")
elif score >= 60:
    print("C")
elif score >= 55:
    print("D+")
elif score >= 50:
    print("D")
else:
    print("F")

print()


# การใช้งานเงื่อนไขซ้อนเงื่อนไข (Nested Condition)

if True:
    print("Hello Welocome!")
    if True:
        print("Yo! Ms.A")
        if True:
            print("so good")



# ถูกทั้งusername and password
usernameInput = input("Username : ")
passwordInput= input("Password : ")
if usernameInput == "worachisa" and passwordInput == "12345678":
    print("DONE")


    print("----- iShop -----")
    print("1.Vat Calculator")
    print("2. Price Calculator")

    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("price : "))
        vat = 7
        result = price + (price * vat/100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Pricel : "))
        price2 = int(input("First Product Pricel : "))
        print(price1 + price2)
else:
    print("ERROR")