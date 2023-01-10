usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "worachisa" and passwordInput == "12345":
    print("DONE")


    print("----- moodandmoon Welcome ! -----")
    print()
    print(">> Product List")


    apple = 12
    watermelon = 45
    longan = 35
    grape  = 92 
    print(f"Apple {apple} THB")
    print(f"Watermelon {watermelon} THB")
    print(f"Longan {longan} THB")
    print(f"Grape {grape} THB")

    print()

    userSelected = input("Selected Product : ")
    productAmount = int(input("Amount : "))
    total = 0

    print()

    if userSelected == "Apple":
        total = productAmount * apple
        print(f"{total} THB")
    elif userSelected == "Watermelon":
        total= productAmount * watermelon
        print(f"{total} THB")
    elif userSelected == "Longan":
        total = productAmount * longan
        print(f"{total} THB")
    elif userSelected == "Grape":
        total = productAmount * grape
        print(f"{total} THB")
    else:
        print("Product not found")

else:
    print("ERROR")


'''
ใน python ไม่นิยมใช้ sum เพราะในโปรแกรมมีฟังก์ชันนี้อยู่

ตัวอย่าง
numbers = [1,2,3,4,5,1,4,5]
print(sum(numbers))
'''


    