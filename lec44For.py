# For : วนซ้ำแบบมีจำนวนรอบที่แน่นอน

# print(list(range(10)))

# for i in range(5):
#     print("Yoooo")
#     print("Tsuki")

# โปรแกรมเครื่องคิดเลข (บวกอย่างเดียว)
# inputRound = int(input("Please Enter Number : "))
# total = 0
# for x in range(inputRound):
#     inputRound = int(input("x" + str(x + 1) + ":")) 
#     total = total + inputRound
# print(f"total {total}")

# x = int(input())
# y = int(input())
# for i in range(5):
#     print(x + y * i, end=" ")

# สร้างสูตรคูณ
# print("2 x 1 = 2")
# print("2 x 2 = 4")
# print("2 x 3 = 6")
# print("2 x 4 = 8")
# print("2 x 5 = 10")
# print("2 x 6 = 12")
# print("2 x 7 = 14")
# print("2 x 8 = 16")
# print("2 x 9 = 18")
# print("2 x 10 = 20")
# print("2 x 11 = 22")
# print("2 x 12 = 24")

# x = 1
# y = 2 * x
# print("2 x", x, "=", y)
# x = x + 1 # ทำด้านขวาก่อน ตอนนี้ x = 1 ดังนั้น x = 1 + 1 = 2
# y = 2 * x
# print("2 x", x, "=", y)
# x = x + 1 
# y = 2 * x
# print("2 x", x, "=", y)

# # แม่2
# for x in range(12):
#     # x = x + 1 # ให้เริ่มที่ 1
#     # y = 2 * x
#     print("2 x", x + 1, "=", 2 * (x + 1)) # ย่อจากบรรทัดที่ 46, 47

# print()

# # แม่3
# for x in range(12):
#     print(f"3 x {x + 1} = {3 * (x + 1)}") 
# # x + 1 ตรงนี้หมายถึง ให้ x เริ่มที่ 1 (ถ้าเป็น x เฉยๆจะเริ่มที่ 0) และการวนในแต่ละเริ่ม x ก็จะเพิ่มที่ละ 1

# print()

# # แม่4
# for x in range(12):
#     print(f"4 x {x + 1} = {4 * (x + 1)}")

# print()

# # แม่5
# for x in range(12):
#     print(f"5 x {x + 1} = {5 * (x + 1)}")

# print()

# # แม่6
# for x in range(12):
#     print(f"6 x {x + 1} = {6 * (x + 1)}")

# print()

# # แม่7
# for x in range(12):
#     print(f"7 x {x + 1} = {7 * (x + 1)}")

# print()

# # แม่8
# for x in range(12):
#     print(f"8 x {x + 1} = {8 * (x + 1)}")

# print()

# # แม่9
# for x in range(12):
#     print (f"9 x {x + 1} = {9 * (x + 1)}")

# print()

# # แม่10
# for x in range(12):
#     print (f"10 x {x + 1} = {10 * (x + 1)}")

# print()

# # แม่11
# for x in range(12):
#     print (f"11 x {x + 1} = {11 * (x + 1)}")

# print()

# # แม่12
# for x in range(12):
#     print (f"12 x {x + 1} = {12 * (x + 1)}")

# print()

# # loopซ้อน
# for x in range(11):
#     for y in range(12):
#         print(f"{x + 2} x {y + 1} = {(x + 2) * (y + 1)}")

# loopนี้ by เด็กชายพชร
for x in range(2, 13):
    for y in range(1, 13):
        print(f"{x} x {y} = {x * y}")



