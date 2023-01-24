'''
คอนเซป
    ถ้าเรายังไม่ ………………
    เราจะทำ ……….. ซ้ำไปเรื่อยๆ

ตอบ
    ถ้ากิยังไม่หายง่วง
    กิก็จะนอนไปเรื่อยๆ (เย่)
'''

# While : การทำงานวนซ้ำไปเรื่อยๆ ก็ต่อเมื่อเงื่อนไขเป็นจริง จะหยุดก็ต่อเมื่อเงื่อนไขเป็นเท็จ

# เกมทายเลข
correctNumber = 17
userGuess = 0

while userGuess != correctNumber:
    userGuess = int(input("Please Guess a Number : "))
    
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif userGuess == correctNumber: # == คือการเปรียบเทียบขวาซ้ายว่ามีค่าเท่ากันไหม ถ้าเท่าค่าก้จะเป็นจริง
        print("Correct !!")
