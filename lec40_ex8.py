usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "worachisa" and passwordInput == "12345":
    print("DONE")


    print("----- moodandmoon Welcome ! -----")
    print("- Product List -")

    apple = 12
    watermelon = 45
    longan = 35
    grape  = 92
    print("Apple" , apple , "THB")
    print("Watermelon" , watermelon , "THB")
    print("Longan" , longan , "THB")
    print("Grape" , grape , "THB")

    userSelected = input("Selected Product : ")
    productAmount = int(input("Amount : "))
    sum = 0

    if userSelected == "Apple":
        sum = productAmount*apple
        print(sum , "THB")
    elif userSelected == "Watermelon":
        sum = productAmount*watermelon
        print(sum , "THB")
    elif userSelected == "Longan":
        sum = productAmount*longan
        print(sum , "THB")
    elif userSelected == "Grape":
        sum = productAmount*grape
        print(sum , "THB")
    else:
        print("Product not found")

else:
    print("ERROR")


    