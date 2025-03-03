def make_sandwich(*ingredients):
    """Prints a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("Enjoy your sandwich!\n")

# Calling the function with different numbers of ingredients
make_sandwich("Turkey", "Lettuce", "Tomato", "Mayo")
make_sandwich("Ham", "Cheese", "Mustard")
