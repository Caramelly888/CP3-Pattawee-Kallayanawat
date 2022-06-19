username = input("username : ")
password = input("password : ")
if username == "Pattawee" and password == "wgs84":
    print("Wellcome to Istored")
    print("-----List-----")
    print("1.Iphone", "Price = 35,000")
    print("2.IMac", "Price = 150,000")
    print("3.Airpods", "Price = 6,500")
    selected = int(input("Products : "))
    if selected == 1:
        amount = int(input("amount products : "))
        price = int(35000)
        total = int(price*amount)
        print("Price = ", total)
    elif selected == 2:
        amount = int(input("amount products : "))
        price = int(150000)
        total = int(price * amount)
        print("Price = ", total)
    elif selected == 3:
        amount = int(input("amount products : "))
        price = int(6500)
        total = int(price * amount)
        print("Price = ", total)







