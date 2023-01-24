'''
def การประกาศ Function ตามด้วยชื่อฟังก์ชัน(ชื่อต้องสื่อความหมายว่าฟังก์ชันทำงานอะไร)
'''
# def sayHello():
#     print("Hello")
# # sayHello() # เรียกใช้ฟังก์ชัน
#     sayMyName()

# def sayMyName():
#     print("Hello Tsuki")
# sayMyName()
# sayHello()

'''
การรับค่าใน Function ใส่ใน parameter
'''
# 1
def addNumber(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
addNumber(100, 20)

print()

# 2
def plusNumber(x, y):
    print(x + y)

def minusNumber(x, y):
    print(x - y)

def multiplyNumber(x, y):
    print(x * y)

def divideNumber(x, y):
    print(x / y)

plusNumber(200, 789)
minusNumber(890, 76)
minusNumber(12, 2)
divideNumber(200, 2)