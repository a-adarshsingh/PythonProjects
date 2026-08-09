def food_delivery_app():
    # -------------------------------
    # Restaurant Menus
    # -------------------------------
    restaurants = {
        "Pizza Palace": {
            "Pizza": 250,
            "Burger": 150,
            "Garlic Bread": 120,
            "Cold Drink": 60
        },

        "Indian Kitchen": {
            "Biryani": 220,
            "Butter Paneer": 180,
            "Naan": 40,
            "Dal Makhani": 160
        },

        "Chinese Corner": {
            "Hakka Noodles": 140,
            "Manchurian": 160,
            "Fried Rice": 150,
            "Spring Roll": 100
        }
    }

    # -------------------------------
    # Display Restaurants
    # -------------------------------
    print("\n========== FOOD DELIVERY APP ==========")

    print("\nAvailable Restaurants:")
    for i, restaurant in enumerate(restaurants, 1):
        print(f"{i}. {restaurant}")

    choice = int(input("\nSelect restaurant: "))
    restaurant_name = list(restaurants.keys())[choice - 1]

    menu = restaurants[restaurant_name]

    # -------------------------------
    # Display Menu
    # -------------------------------
    print(f"\n========== {restaurant_name} ==========")

    items = list(menu.keys())

    for i, item in enumerate(items, 1):
        print(f"{i}. {item} - ₹{menu[item]}")

    # -------------------------------
    # Create Order
    # -------------------------------
    order = {}
    total = 0

    while True:
        item_choice = int(input("\nEnter item number (0 to finish): "))

        if item_choice == 0:
            break

        if 1 <= item_choice <= len(items):

            item = items[item_choice - 1]

            quantity = int(input(f"Enter quantity of {item}: "))

            order[item] = quantity

            total += menu[item] * quantity

            print(f"{quantity} x {item} added to cart.")

        else:
            print("Invalid item number.")

    # -------------------------------
    # Order Summary
    # -------------------------------
    print("\n========== ORDER SUMMARY ==========")

    if not order:
        print("Your cart is empty.")
        return

    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item} x {quantity} = ₹{price}")

    delivery_fee = 40
    grand_total = total + delivery_fee

    print("-----------------------------------")
    print(f"Food Total     : ₹{total}")
    print(f"Delivery Fee   : ₹{delivery_fee}")
    print(f"Grand Total    : ₹{grand_total}")

    # -------------------------------
    # Place Order
    # -------------------------------
    confirm = input("\nPlace order? (yes/no): ").lower()

    if confirm != "yes":
        print("Order cancelled.")
        return

    order_id = 1001

    print("\n✅ Order placed successfully!")
    print(f"Order ID: FD{order_id}")
    print(f"Restaurant: {restaurant_name}")
    print(f"Amount: ₹{grand_total}")

    # -------------------------------
    # Live Tracking
    # -------------------------------
    print("\n========== LIVE TRACKING ==========")

    tracking_status = [
        "Order Confirmed",
        "Restaurant is Preparing Your Food",
        "Food is Ready",
        "Delivery Partner Picked Up Your Order",
        "Out for Delivery",
        "Delivered"
    ]

    for status in tracking_status:
        print("📍", status)

    print("\n🎉 Your food has been delivered!")


# Run the application
food_delivery_app()