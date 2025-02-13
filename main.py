# Internet Shop

cart = {}
fruit_prices = {"apple": 1.5, "banana": 2.5, "lemon": 3.5}
bread_prices = {"white": 1.8, "wheat": 1.5, "rye": 2.0}
diary_prices = {"milk": 0.9, "eggs": 0.2, "cheese": 1.2}
soft_drink_prices = {"coca-cola": 1.5, "fanta": 1.4, "sprite": 1.3}
juice_prices = {"sochnaya dolina": 1.9, "bliss": 2.1}
shampoo_prices = {"clear men": 1.6, "head shoulders": 1.5, "nivea": 1.7}
deodorants_prices = {"axe": 1.9, "nivea": 2.0, "old spice": 2.1}
toothpaste_prices = {"colgate": 1.8, "sensodyne": 1.9, "crest": 2.0}
new_product_prices = {}
new_product_prices.update(fruit_prices)
new_product_prices.update(bread_prices)
new_product_prices.update(diary_prices)
new_product_prices.update(soft_drink_prices)
new_product_prices.update(juice_prices)
new_product_prices.update(shampoo_prices)
new_product_prices.update(deodorants_prices)
new_product_prices.update(toothpaste_prices)


def display_products():
    total_price = 0
    print('\nBasket:')
    print(" {:<10} {:<10} {:<10}".format("Product", "Amount", "Price"))
    print("-" * 35)

    if len(cart) == 0:
        print('Cart is empty')
        print("-" * 35)

    elif len(cart) != 0:
        for product, prices in cart.items():
            if "fruit_weight" in prices:
                amount = prices["fruit_weight"]
            elif 'bread_number' in prices:
                amount = prices['bread_number']
            elif 'diary_number' in prices:
                amount = prices['diary_number']
            elif 'soft_drink_number' in prices:
                amount = prices['soft_drink_number']
            elif 'soft_drink_number' in prices:
                amount = prices['soft_drink_number']
            elif 'juice_number' in prices:
                amount = prices['juice_number']
            elif 'shampoo_number' in prices:
                amount = prices['shampoo_number']
            elif 'deodorants_number' in prices:
                amount = prices['deodorants_number']
            elif 'toothpaste_number' in prices:
                amount = prices['toothpaste_number']
            elif 'new_product_number' in prices:
                amount = prices['new_product_number']
            else:
                amount = None

            unit_price = prices['price']
            total_price += unit_price

            print("{:<10} {:<10} ${:<10.2f}".format(product.capitalize(), amount, unit_price))
        print("-" * 35)
        print('{:<10} ${:.2f}'.format('Total price:', total_price))


while True:
    print('\nWelcome to the Internet Shop!')
    user = input('\nIf you would like to shop in here please press "1"\n'
                 'If you would like to leave please press "0"\n'
                 '::: ')
    if user == '1':
        while True:
            menu = input('\nType in:\n'
                         '"Products" to see products in the cart,\n'
                         '"Add" to add the product to the cart\n'
                         '"Change" to change the product in the cart\n'
                         '"Delete" to delete the product in the cart\n'
                         '::: ').lower()
            if menu == 'products':
                display_products()
            elif menu == 'add':
                while True:
                    category = input('\nPlease type in a category of product you would like to order\n'
                                     'Categories: "Food", "Drinks", "Self-Care" or "0" to leave\n'
                                     '::: ')
                    category = category.lower()
                    if category == 'food':
                        while True:
                            food = input('\nChoose food type:\n'
                                         '"Fruits", "Bread", "Diary"\n'
                                         'or press "0" to go back\n'
                                         '::: ')
                            food = food.lower()
                            if food == 'fruits':
                                fruits = input('\nChoose type of fruit:\n '
                                               '"Apple", "Banana" or "Lemon"\n'
                                               '::: ')
                                fruits = fruits.lower()
                                if fruits in fruit_prices:
                                    fruit_weight = float(input('\nType in the weight (kg): '))
                                    if fruit_weight > 0:
                                        fruit_price = fruit_weight * fruit_prices[fruits]
                                        if fruits in cart:
                                            old_fruit_weight = cart[fruits]['fruit_weight']
                                            old_fruit_price = cart[fruits]['price']
                                            new_fruit_weight = old_fruit_weight + fruit_weight
                                            new_fruit_price = old_fruit_price + fruit_price

                                            cart[fruits] = {"fruit_weight": new_fruit_weight, "price": new_fruit_price}
                                        else:
                                            cart[fruits] = {"fruit_weight": fruit_weight, "price": fruit_price}
                                        print(f'\n{fruit_weight}kg of "{fruits.capitalize()}" added to the list.\n '
                                              f'Total price for "{fruits.capitalize()}": ${fruit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                        break
                                else:
                                    print("\nInvalid fruit selection.\n")
                                    break
                            #bread
                            elif food == 'bread':
                                bread = input('\nChoose type of bread:\n'
                                              '"White", "Wheat", "Rye"\n'
                                              '::: ')
                                bread = bread.lower()
                                if bread in bread_prices:
                                    bread_number = float(
                                        input(f'\nHow many of "{bread.capitalize()}" you would like to buy?\n'
                                              '::: '))
                                    if bread_number > 0:
                                        bread_unit_price = bread_number * bread_prices[bread]
                                        if bread in cart:
                                            old_bread_number = cart[bread]['bread_number']
                                            old_bread_price = cart[bread]['price']
                                            new_bread_number = old_bread_number + bread_number
                                            new_bread_price = old_bread_price + bread_unit_price

                                            cart[bread] = {"bread_number": new_bread_number, "price": new_bread_price}
                                        else:
                                            cart[bread] = {'bread_number': bread_number, "price": bread_unit_price}
                                        print(
                                            f'\n"{bread_number}" units of "{bread.capitalize()}" added to the basket\n'
                                            f'Total price for "{bread.capitalize()}": ${bread_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            #diary
                            elif food == 'diary':
                                diary = input('\nPlease choose diary: "Milk", "Eggs", "Cheese"\n'
                                              '::: ')
                                diary = diary.lower()
                                if diary in diary_prices:
                                    diary_number = float(
                                        input(f'\nHow many of "{diary.capitalize()}" you would like to buy?\n'
                                              f'::: '))
                                    if diary_number > 0:
                                        diary_unit_price = diary_number * diary_prices[diary]
                                        if diary in cart:
                                            old_diary_number = cart[diary]['diary_number']
                                            old_diary_price = cart[diary]['price']
                                            new_diary_number = old_diary_number + diary_number
                                            new_diary_price = old_diary_price + diary_unit_price

                                            cart[diary] = {"diary_number": new_diary_number, "price": new_diary_price}
                                        else:
                                            cart[diary] = {'diary_number': diary_number, "price": diary_unit_price}
                                        print(
                                            f'\n"{diary_number}" units of "{diary.capitalize()}" added to the basket\n'
                                            f'Total price for "{diary.capitalize()}": ${diary_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                        break
                                else:
                                    print("\nInvalid diary selection.\n")
                                    break
                            elif food == '0':
                                print('\nGoing back')
                                break
                            else:
                                print('\nError invalid symbol\n')
                                break
                    #drinks
                    elif category == 'drinks':
                        while True:
                            drinks = input('\nChoose drink type:\n'
                                           '"Soft drink" or"Juice"\n'
                                           'or press "0" to go back\n'
                                           '::: ')
                            drinks = drinks.lower()
                            if drinks == 'soft drink':
                                soft_drink = input('\nChoose soft drink to purchase: "Coca-Cola", "Fanta", "Sprite"\n'
                                                   '::: ')
                                soft_drink = soft_drink.lower()
                                if soft_drink in soft_drink_prices:
                                    soft_drink_number = float(
                                        input(f'\nHow many liters of {soft_drink.capitalize()} do you want to buy?\n'
                                              '::: '))
                                    if soft_drink_number > 0:
                                        soft_drink_unit_price = soft_drink_number * soft_drink_prices[soft_drink]
                                        if soft_drink in cart:
                                            old_soft_drink_number = cart[soft_drink]['price']
                                            old_soft_drink_price = cart[soft_drink]['soft_drink_number']
                                            new_soft_drink_number = old_soft_drink_number + soft_drink_number
                                            new_soft_drink_price = old_soft_drink_price + soft_drink_unit_price
                                            cart[soft_drink] = {"soft_drink_number": new_soft_drink_number,
                                                                "price": new_soft_drink_price}
                                        else:
                                            cart[soft_drink] = {'soft_drink_number': soft_drink_number,
                                                                'price': soft_drink_unit_price}
                                        print(
                                            f'\n"{soft_drink_number}" units of "{soft_drink.capitalize()}" added to the basket\n'
                                            f'Total price for "{soft_drink.capitalize()}": ${soft_drink_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            #juice
                            elif drinks == 'juice':
                                juice = input('\nChoose type of juice: "Sochnaya Dolina" or "Bliss"\n'
                                              '::: ')
                                juice = juice.lower()
                                if juice in juice_prices:
                                    juice_number = float(
                                        input(f'\nHow many liters of {juice.capitalize()} do you want to buy?\n'
                                              '::: '))
                                    if juice_number > 0:
                                        juice_unit_price = juice_number * juice_prices[juice]
                                        if juice in cart:
                                            old_juice_number = cart[juice]['juice_number']
                                            old_juice_price = cart[juice]['price']
                                            new_juice_number = old_juice_number + juice_number
                                            new_juice_price = old_juice_price + juice_unit_price

                                            cart[juice] = {'juice_number': new_juice_number, 'price': new_juice_price}
                                        else:
                                            cart[juice] = {'juice_number': juice_number, 'price': juice_unit_price}
                                        print(
                                            f'\n"{juice_number}" units of "{juice.capitalize()}" added to the basket\n'
                                            f'Total price for "{juice.capitalize()}": ${juice_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            elif drinks == '0':
                                print('\nGoing back')
                                break
                            else:
                                print('\nError invalid symbol\n')
                    #self-care
                    elif category == 'self-care':
                        while True:
                            self_care = input('\nChoose item type:\n'
                                              '"Shampoo", "Deodorants", "Toothpaste"\n'
                                              'or press "0" to go back\n'
                                              '::: ')
                            self_care = self_care.lower()
                            if self_care == 'shampoo':
                                shampoo = input('\nChoose type of shampoo: "Clear Men", "Head Shoulders", "Nivea"\n'
                                                '::: ')
                                shampoo = shampoo.lower()
                                if shampoo in shampoo_prices:
                                    shampoo_number = float(
                                        input(f'\nHow many of "{shampoo.capitalize()}" shampoo you want to buy?\n'
                                              '::: '))
                                    if shampoo_number > 0:
                                        shampoo_unit_price = shampoo_number * shampoo_prices[shampoo]
                                        if shampoo in cart:
                                            old_shampoo_number = cart[shampoo]['shampoo_number']
                                            old_shampoo_unit_price = cart[shampoo]['price']
                                            new_shampoo_number = old_shampoo_number + shampoo_number
                                            new_shampoo_unit_price = old_shampoo_unit_price + shampoo_unit_price
                                            cart[shampoo] = {'shampoo_number': new_shampoo_number,
                                                             'price': new_shampoo_unit_price}
                                        else:
                                            cart[shampoo] = {'shampoo_number': shampoo_number,
                                                             'price': shampoo_unit_price}
                                        print(
                                            f'\n"{shampoo_number}" units of "{shampoo.capitalize()}" added to the basket\n'
                                            f'Total price for "{shampoo.capitalize()}": ${shampoo_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            elif self_care == 'deodorants':
                                deodorants = input('\nPlease choose deodorant: "Axe", "Nivea", "Old Spice"\n'
                                                   '::: ')
                                deodorants = deodorants.lower()
                                if deodorants in deodorants_prices:
                                    deodorants_number = float(
                                        input(f'\nHow many of "{deodorants.capitalize()}" deodorant you want to buy?\n'
                                              '::: '))
                                    if deodorants_number > 0:
                                        deodorants_unit_price = deodorants_number * deodorants_prices[deodorants]
                                        if deodorants in cart:
                                            old_deodorants_number = cart[deodorants]['deodorants_number']
                                            old_deodorants_unit_price = cart[deodorants]['price']
                                            new_deodorants_number = old_deodorants_number + deodorants_number
                                            new_deodorants_unit_price = old_deodorants_unit_price + deodorants_unit_price

                                            cart[deodorants] = {'deodorants_number': new_deodorants_number,
                                                                'price': new_deodorants_unit_price}
                                        else:
                                            cart[deodorants] = {'deodorants_number': deodorants_number,
                                                                'price': deodorants_unit_price}
                                        print(
                                            f'\n"{deodorants_number}" units of "{deodorants.capitalize()}" added to the basket\n'
                                            f'Total price for "{deodorants.capitalize()}": ${deodorants_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            elif self_care == 'toothpaste':
                                toothpaste = input('\nChoose toothpaste type: "Colgate", "Sensodyne", "Crest"\n'
                                                   '::: ')
                                toothpaste = toothpaste.lower()
                                if toothpaste in toothpaste_prices:
                                    toothpaste_number = float(
                                        input(f'\nHow many of "{toothpaste.capitalize()}" deodorant you want to buy?\n'
                                              '::: '))
                                    if toothpaste_number > 0:
                                        toothpaste_unit_price = toothpaste_number * toothpaste_prices[toothpaste]
                                        if toothpaste in cart:
                                            old_toothpaste_number = cart[toothpaste]['toothpaste_number']
                                            old_toothpaste_unit_price = cart[toothpaste]['price']
                                            new_toothpaste_number = old_toothpaste_number + toothpaste_number
                                            new_toothpaste_unit_price = old_toothpaste_unit_price + toothpaste_unit_price

                                            cart[toothpaste] = {'toothpaste_number': new_toothpaste_number,
                                                                'price': new_toothpaste_unit_price}
                                        else:
                                            cart[toothpaste] = {'toothpaste_number': toothpaste_number,
                                                                'price': toothpaste_unit_price}
                                        print(
                                            f'\n"{toothpaste_number}" units of "{toothpaste.capitalize()}" added to the basket\n'
                                            f'Total price for "{toothpaste.capitalize()}": ${toothpaste_unit_price:.2f}')
                                        display_products()
                                    else:
                                        print("\nInvalid weight. Please enter a positive value.\n")
                                else:
                                    print("\nInvalid fruit selection.\n")
                            elif self_care == '0':
                                print('\nGoing back')
                                break
                            else:
                                print('\nError invalid symbol\n')
                                break
                    #0
                    elif category == '0':
                        print('\nExit\n')
                        break
                    else:
                        print('\nError invalid symbol\n')
            elif menu == 'change':
                display_products()
                if len(cart) == 0:
                    print('Nothing to change')
                    break
                elif len(cart) != 0:
                    product_change = input('\nType in a product to change: ').lower()
                    if product_change in cart:
                        cart.pop(product_change)
                        new_product = input('\nType in a new product: ').lower()
                        if new_product in new_product_prices:
                            new_product_number = float(input('\nType in amount: '))
                            if new_product_number > 0:
                                new_product_price = new_product_number * new_product_prices[new_product]
                                cart[new_product] = {'new_product_number': new_product_number,
                                                     'price': new_product_price}
                                print(f'"{product_change}" is replaced by "{new_product} in the cart"')
                                display_products()
                            else:
                                print('\n Error invalid number')
                                break
                        else:
                            print('\nInvalid product name')
                            break
                    elif product_change not in cart.items():
                        print('\nError invalid product name!')
                    else:
                        break
                else:
                    print('\nError invalid symbols!')
                    break
            elif menu == 'delete':
                remove = input('\nType in:\n'
                               '"Clear" to clear the cart\n'
                               '"Delete" to delete the product\n'
                               '"0" to go back\n'
                               '::: ').lower()
                if remove == 'clear':
                    cart.clear()
                    display_products()
                    print('\nCart is cleared!')
                elif remove == 'delete':
                    display_products()
                    if len(cart) == 0:
                        print('Nothing to delete')
                        break
                    elif len(cart) != 0:
                        product_delete = input('\nType in a product to delete: ').lower()
                        if product_delete in cart:
                            cart.pop(product_delete)
                            display_products()
                            print(f'\n"{product_delete.capitalize()}" is successfully deleted from the cart!')
                        else:
                            print('\nError invalid product name!')
                    else:
                        print('\nError invalid symbol!')
                        break
                elif remove == '0':
                    print('\nGoing back')
                    break
                else:
                    print('\nError invalid symbol!')
                    break
            else:
                print('Error unknown symbol')
                break
    elif user == '0':
        print('\nExit\n')
        break
    else:
        print('\nError unknown symbol')
