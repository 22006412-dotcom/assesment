def split_bill(total_amount: float, people: int, tip: float) -> float:
    """
    Calculates how much each person should pay.

    :param total_amount: The base bill amount
    :param people: Number of people splitting the bill
    :param tip: Tip amount to add (0 if none)
    :return: Amount each person pays
    """

    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")

    if tip > 0:
        total_amount += tip

    return total_amount / people


def collect_names(num_people: int) -> list:
    """Collects names using a loop."""
    names = []
    for i in range(num_people):
        name = input(f"Enter name for person {i + 1}: ")
        names.append(name)
    return names


# ---- Main Program ----
try:
    num_people = int(input("Enter number of people: "))
    names = collect_names(num_people)

    bill = float(input("Enter total bill amount: "))
    tip = float(input("Enter tip amount (0 if none): "))

    amount_each = split_bill(bill, num_people, tip)

    print("\nBill Split Result:")
    for name in names:
        print(f"{name} pays: ${round(amount_each, 2)}")

except ValueError as error:
    print("Input error:", error)
