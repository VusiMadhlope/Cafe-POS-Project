#Flow -> Featues 
#   Flow
# - Welcome -> Check Menu and choose preferred items -> Place Order -> Taken to payments section (cash or card) -> user iniates payment (successful or decline) ->
# - if successful: payment accepted and user gets reciept with details. Else: Declined Try again (loops till payment is accpeted) -> Goodbye message, End program. 
#   
#   Features
#   - Select items from menu. Dictionary functionality and show via popup
#   - Able to customize orders (extra toppings etc ect)
#   - Print receipt after payment:
#       Must show all items with price. Then subtotal, account for vat then final total
#   - Customer can pay in cash or card:
#        if money is enough payment will be "successful" else "declined, Try again"


import json
with open("menu.json", "r") as file:
    menu = json.load(file)

def Home_run_menu(menu):
    #parse the menu function into order function
    print("============================================================")
    print(" HOME RUN CAFE Menu ")
    print("============================================================")
    for code, (name, price) in menu.item():
        print(f"{code}: {name} - R{price}")

def order():
    #User will be prompted with menu and choose using item code. Will then add chosen items (Item code) in a list
    order_items = []
    while True:
        Home_run_menu(menu)
        choice = input("Please select from the menu shown or type done to complete order: ").upper()

        if choice == "DONE":
            break
        elif choice in menu:
            order_items.append(choice)
            print(f"Your order has been successfully added: {menu[choice][0]} ")
        else:
            print("Invalid item code. Please Try Again. \nThank You.")
            
    return order_items

def payment(total):
    #payment functionality for the cafe
    vat = 0.15
    subtotal = 0
    total = 0
    
    print("============================================================")
    print(" HOME RUN CAFE PAYMENT SECTION ")
    user = print("Select your payment option below \n1: Cash \n2: Card \n3: Tap Payment \n4: Scan to pay")
    print("")

    #calculatin subtotal
    for item in order:
        if item in menu:
            name, price = menu[item]
            subtotal += price
        else:
            print(f"Item {item} does not exist in the menu.")

    #adding in the VAT calculation
    vat = subtotal * vat
    total  = subtotal + vat

    print(f"Subtotal: R{subtotal:.2f}")
    print(f"Vat: R{vat:.2f}")
    print(f"Total: R{total:.2f}")

    #Payment method 
    while True:
        try: 
            print("Select your payment option below \n1: Cash \n2: Card \n3: Tap Payment \n4: Scan to pay")
            print("")
            user ("Enter your payment option: ")

            if user.isdigit():
                user = int(user)
                if user in [1,2,3,4]:
                    method = ["Cash", "Card", "Tap Payment", "Scan to pay"][user - 1]
                    print(f" {method} has been selected.")

                    while True:
                        user_amount = input(f"Enter your amount: ")
                        if user_amount.isdigit():
                            user_paid = int(user_amount)
                            if user_paid >= total:
                                change = user_paid - total
                                print("Payment Successful")
                                if change > 0:
                                    print(f"Change is: R{change:.2f}")
                                return total
                            else:
                                print("Payment has been declined Try again")
                        else:
                            print("Invalid Amount. Enter a valid amount")
                else:
                    print("Invalid Payment option. Please select from options above")
            else:
                print("Enter numbers only please")
        
        except ValueError:
            print("Invalid input. Please Try Again.")


def receipt(order_items, menu,subtotal, total, vat):
    print("============================================================")
    print(" HOME RUN CAFE RECEIPT ")
    print("============================================================")
    
    for item_code in order_items:
        if item_code in menu:
            name, price = menu[item_code]
            print(f"{name: <25} R{price:.2f}")
        else:
            print(f"item {item_code} does not exist in the menu.")
    
    print("============================================================")
    print(f"Subtotal:                                   R{subtotal:.2f}")
    print(f"vat:                                        R{vat:.2f}")
    print(f"total:                                      R{total:.2f}")
    print("============================================================")
    print("Thank you for choosing HOME RUN CAFE. See you soon!!! ;)")
    



def main():
    def switch(choices):
        match choices:
            case 1:
                return order()
            case 2:
                return payment()
            case 3:
                return receipt()
            case 4:
                print("Thank You for dining at Home Run Cafe. See you soon!!!")
                exit()
            case _:
                print("Invalid Option. Only choose from above options please.")
    
    try:
        while True:
            print("")
            print("=====================================")
            print("WELCOME TO HOME RUN CAFE")
            print("***  See Below   ***")
            print("\n 1. Drinks Menu" \
            "\n 2. Your Order"
            "\n 3. Payments Sections"
            "\n 4. Your Receipt"
            "\n 5. Exit Program")
            print("")
            print("=====================================")

            user = input("Choose your option: ")
            if user.isdigit():
                user = int(user)
                switch(user)
            
            else:
                print("invalid option!!!")
    except KeyboardInterrupt:
        print("\nGame Interrupted. Exiting game.")


main()