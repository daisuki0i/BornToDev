# index
text = "Hello"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[1] + "llo")

print()

# ตัดตัวอักษร
print(text[0:4]) # หมายถึง เอาตั้งแต่ inddex ตัวที่ 0 จนถึงก่อนหน้าตัวที่ 4

print()

# ตรวจสอบ String return true , false
text = "Tsuki so coooooool"
print("Tsuki" in text)
print("eiei" in text)

print()

# การจัดรูปแบบ String และ การแสดงผล

# 1
name = "Tsuki"
weight = str(53) + "kg"
weightInt = 53
print("Hello " + name + "! and weight " + weight)

print()

# 2-string formatting
print("Hello %s ! and weight %s" % (name , weight))
print("Hello %s ! and weight %d kg" % (name , weightInt))
