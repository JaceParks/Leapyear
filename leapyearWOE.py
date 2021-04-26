def again():  

    year = input("please enter a valid year: ") 

    verifiedyear = int(year)

    d4i = verifiedyear / 4
    d100i = verifiedyear / 100
    d400i = verifiedyear / 400

    if d400i.is_integer():
        print(str(verifiedyear) + " is a valid leap year!")
    elif d100i.is_integer():
        print(str(verifiedyear) + " is not a valid leap year")
    elif d4i.is_integer():
        print(str(verifiedyear) + " is a valid leap year!")                                                                                     
    else:
        print(str(verifiedyear) + " is not a valid leap year")
    again()

again()

