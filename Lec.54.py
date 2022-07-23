def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done")
        return showMenu()
    else:
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1 :
        inputPrice = int(input("Input Your Price : "))
        return  vatCalculator(inputPrice)
    if userSelected == 2 :
        return  pricecalculate()

    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def pricecalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
print(login())
print(showMenu())
print(menuSelect())
print(pricecalculate())

