numberOfShoes = int(input("How many shoes? "))

if 0 < numberOfShoes < 10**3:
    listOfShoes = list(map(int, input("Enter shoe sizes: ").strip().split()))

    if len(listOfShoes) == numberOfShoes:
        print(listOfShoes)

        saleList = []
        customer = int(input("Enter customer count: "))

        for _ in range(customer):
            print("")
            saleSubList = list(map(int, input("Enter as: shoeSize price: ").strip().split()))
            saleList.append(saleSubList)

        earn = 0

        for sale in saleList:
            size = sale[0]
            price = sale[1]

            # shoe sizes allowed: 1 to 10
            if 0 < size <= 20:
                if size in listOfShoes:
                    earn += price
                    listOfShoes.remove(size)
                else:
                    price=0
                    earn+=price

        print(earn)
    else:
        print("❌ Shoe size count does not match!")
else:
    print("❌ Invalid number of shoes!")
