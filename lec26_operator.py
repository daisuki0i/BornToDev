'''
ตัวดำเนินการทางคณิต -> 2 more variable
ลำดับกาารทำ
1.( )
2.** ยกกำลัง
3.+x, -x, ~x
4.*, /, //, %
5.+, -
'''
x = 10
y = 5
# z = 10 + 5
z = x + y
print(z)

money = 200
incomeDay = 100
costDay = 166
result = 200 + 100 * 30 - 166 * 30 #โปรแกรมจะใส่วงเล็บให้เอง
print(result) #-1780

resultTwo = money + (incomeDay * 30) - (costDay * 30) #บอกแล้วโปรแกรมใส่วงเล็บให้เอง!
print(resultTwo) #-1780

'''
ตัวดำเนินการทางตรรกะ -> มีค่า True , False
'''
x = True
y = False
z = True and False
print(z)

a = 10
b = 15
c = a > b
print(c)

#โปรแกรมเข้าร้านเหล้า อายุต้องมากกว่า 18 ครับผม
age = 56
print("สวัสดีครับ คุณอายุเกินกว่าที่จะเข้าร้านเราได้ไหม")
print(age > 18)

'''
การใช้งาน assignment operator (เครื่องหมาย = )
'''
a = 10
b = 5
c = a - b
b = 15
print(b) #15 เพราะ python สั่งงานเป็นบรรทัด บรรทัดที่ 47 b จะเก็บค่า 5 แต่ลงมาบรรทัดที่ 49 b จะมีค่า 15

a = 10
b =  a + 20
c = a + b
a += 3
print(b)

a = 10
a = a + 15
a += 3
print(a)

money = 1000
money = money - 390
money -= 20
print(money)