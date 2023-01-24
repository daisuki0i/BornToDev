a = "worachisa"
b = "boonlert"
print(a+b)
print(a,b)

# แปลงประเภทขอมูล
a = "10"
b = 5
c = int(a)+b # ใส่ type ข้างหน้าตัวที่ต้องการเปลี่ยน
print(c)

x = input()
print(x)
print(type(x))

name = input("first name : ")
lastName = input("last name : ")
print("Hello" , name , lastName)

# HW
numOne = int(input("first number : "))
numTwo = int(input("second number : "))
sum = numOne + numTwo
print(sum)

# คำนวณภาษี
price = 10000
vat = 7
result = price+(price*vat/100)
print(result)

# HW
price = int(input("price : "))
vat = 7
result = price + (price * vat/100)
print(result)