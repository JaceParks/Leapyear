def again(verifiedyear):  

    #year = input("please enter a valid year: ") 

    #verifiedyear = int(year)

    d4i = verifiedyear / 4
    d100i = verifiedyear / 100
    d400i = verifiedyear / 400

    if d400i.is_integer():
        return True
    elif d100i.is_integer():
        return False
    elif d4i.is_integer():
        return True
    else:
        return True
again()

