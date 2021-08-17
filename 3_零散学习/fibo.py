print('--------outer_test_1--------')
print(__name__)
if __name__ == '__main__':
    print('if __name__ is main print')


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


if __name__ == '__main__':
    print("hello")
