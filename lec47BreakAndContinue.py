'''
ฺBreak : คำสั่งให้มีการ ออกจากloop
Continue : คำสั่งให้มีการ ข้ามคำสั่งต่อไปใน loop for ของรอบนั้น
'''

# ฺBreak
for x in range(11):
    for y in range(12):
        print(f"{x + 2} x {y + 1} = {(x + 2) * (y + 1)}")
    break

print()

# Continue
for val in "Hello": 
# ความหมายคือ เราจะนำString แต่ละตัวอักษร(Hello) มาใส่ใน val
    if val == "l":
        continue # มันจะข้ามรอบการทำงาน ในที่นี้คือข้าม l 
    print(val)
print("end")
