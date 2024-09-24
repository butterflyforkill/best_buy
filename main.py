import sys
from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def display_menu():
    """
    Display the menu options for the program.

    Returns:
    None
    """
    print("********** Store Menu **********")
    print("Menu:\n1. List all products in store\n2."
          " Show total amount in store\n3."
          " Make an order\n4."
          " Quit\n")


def get_user_input():
    """
    Get user input for menu options and validate the input.

    Returns:
    int: User's choice for the menu option.
    """
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            if 1 <= user_input <= 4:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")


def list_all_products(store):
    """
    Display a list of all products in the store,
    along with their prices and quantities.

    Parameters:
    - store: The object representing the store
            from which the list of products is to be fetched.

    Returns:
    This function does not return any value.
    It simply prints the list of all products,
    their prices, and quantities in the store.
    """
    for i, product in enumerate(store.products, 1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")


def show_total_amount(store):
    """
    Display the total quantity of items in the store.

    Parameters:
    - store: The object representing
            the store from which the total quantity is to be fetched.

    Returns:
    This function does not return any value.
    It simply prints the total quantity of items in the store.
    """
    total_amount = store.get_total_quantity()
    print(f"Total of {total_amount} items in store\n")


def make_order(store):
    """
    Create an order by allowing the user
    to select products and quantities from the store.

    Parameters:
    - store: The object representing the store
            from which the products are to be ordered.

    Returns:
    This function does not return any value.
    It allows the user to build a shopping list
    by selecting products and quantities from the store,
    and then places an order based on the shopping list.
    """
    shopping_list = []
    while True:
        print("------")
        list_all_products(store)
        print("------")
        product_index = input("Which product # do you want? (Enter empty text to finish order): ")
        if not product_index:
            break
        try:
            product_index = int(product_index) - 1
            if 0 <= product_index < len(store.products):
                quantity = int(input("What amount do you want? "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                elif quantity > store.products[product_index].quantity:
                    print("Error: Insufficient quantity in store.")
                else:
                    shopping_list.append((store.products[product_index], quantity))
            else:
                print("Error: Invalid product number.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    try:
        if shopping_list:
            total_price = Store.order(shopping_list)
            print(f"Total price of the order: ${total_price}")
    except ValueError as e:
        print(f"Error: {e}")
        


def quit():
    """
    Function to exit the program.

    Prints "Exiting the program..." and exits the program.

    Returns:
    None
    """
    print("Exiting the program...")
    sys.exit()


def start(store):
    """
    Function to start the program and display the menu.

    Args:
    store: The store object containing product information.

    Returns:
    None
    """
    display_menu()

    while True:
        user_input = get_user_input()
        menu_functionality = {
            1: list_all_products,
            2: show_total_amount,
            3: make_order,
            4: quit
       }
        if user_input in menu_functionality:
            if user_input == 4:
                menu_functionality[user_input]()
            else:
                menu_functionality[user_input](store)
        else:
            print("You entered the wrong key")
        choice = input("\nPress Enter to continue\n")
        display_menu()
        if choice != '':
            break


def main():
    """
    Function to initialize the program by creating a store
    with a list of products and starting the main program loop.

    Creates a list of products, initializes a store object with the product list,
    and starts the main program loop using the start function.

    Returns:
    None
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
