#taking data from user input
def viewMenu ():
    print("===============MENU===============")
    print("1- Nasi Lemak Ayam........RM10")
    print("2- Nasi Lemak Telur.......RM5")
    print("3- Mee Goreng.............RM7")
    print("4- Milo Ais...............RM4")
    print("5- Teh Ais................RM3")
    print("n- enter n for No to stop");
    return input("\nEnter Menu number 1 to 5: ")

#calculate each menu price
def calculate_menuXprice(a,b):
    return a*b


choice = viewMenu ()
totalResult = 0
while True:       
        if choice == '1':#Nasi Lemak Ayam = price 10
            price = 10
            qtt = int(input("Enter quantity: "))
            result = calculate_menuXprice(price,qtt)
            totalResult = totalResult + result
            print("Total price for",qtt," Nasi Lemak Ayam is RM",result)
            
        elif choice == '2':#Nasi Lemak Telur = price 5
            price = 5
            qtt = int(input("Enter quantity: "))
            result = calculate_menuXprice(price,qtt)
            totalResult = totalResult + result
            print("Total price for",qtt," Nasi Lemak Telur is RM",result)

        elif choice == '3':#Mee Goreng = price 7
            price = 7
            qtt = int(input("Enter quantity: "))
            result = calculate_menuXprice(price,qtt)
            totalResult = totalResult + result
            print("Total price for",qtt," Mee Goreng is RM",result)
        
        elif choice == '4':#Milo Ais = price 4
            price = 4
            qtt = int(input("Enter quantity: "))
            result = calculate_menuXprice(price,qtt)
            totalResult = totalResult + result
            print("Total price for",qtt," Milo Ais is RM",result)

        elif choice == '5':#Teh Ais = price 3
            price = 3
            qtt = int(input("Enter quantity: "))
            result = calculate_menuXprice(price,qtt)
            totalResult = totalResult + result
            print("Total price for",qtt," Teh Ais is RM",result)
        elif choice != 'n' and int(choice) > 5:
             print("Invalid selection. Please choose 1, 2, 3, 4 or 5.")


        print("Total price RM : ",totalResult)
        
        choice = input("\nEnter Menu number 1 to 5:?")
        if choice.lower() == 'n':
            print("Thank you for visiting, your total bill is: RM ",totalResult)
            break