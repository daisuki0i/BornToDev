# def sayHello(name):
#     print("Hello", name)
# def hello():
#     return 10
# sayHello("tsuki")
# print(hello())

# คำนวณตัวเลขทางคณิต
def vatCalculast(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result

price = int(input("price : "))
print(vatCalculast(price))

# 2
def vatCalculast(totalPrice):
    return totalPrice + (totalPrice * 7 / 100)
print(vatCalculast(100))
    
'''
แก้เป็นฟังก์ชัน
ควรมี
- login
- show menu
- select menu
'''

def logIn():
    usernameInput = input("Username : ")
    passwordInput= input("Password : ")
    if usernameInput == "worachisa" and passwordInput == "12345678":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1.Vat Calculator")
    print("2. Price Calculator")

def selectMenu():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + ( totalPrice * vat / 100)
    return result

def priceCalculate():
    price1 = int(input("First Product Pricel : "))
    price2 = int(input("First Product Pricel : "))
    return vatCalculast(price1 + price2)

print(logIn)
print(showMenu)
print(selectMenu)









# usernameInput = input("Username : ")
# passwordInput= input("Password : ")
# if usernameInput == "worachisa" and passwordInput == "12345678":
#     print("DONE")


#     print("----- iShop -----")
#     print("1.Vat Calculator")
#     print("2. Price Calculator")

#     userSelected = int(input(">>"))
#     if userSelected == 1:
#         price = int(input("price : "))
#         vat = 7
#         result = price + (price * vat/100)
#         print(result)
#     elif userSelected == 2:
#         price1 = int(input("First Product Pricel : "))
#         price2 = int(input("First Product Pricel : "))
#         print(price1 + price2)
# else:
#     print("ERROR")