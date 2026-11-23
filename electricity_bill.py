
FIXED_CHARGE = 50.00
TAX_RATE = 0.05


def calculate_energy_charge(units):
    """Calculate electricity charges using slab-wise rates."""

    if units <= 100:
        energy_charge = units * 3

    elif units <= 200:
        energy_charge = (100 * 3) + ((units - 100) * 5)

    else:
        energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 8)

    return energy_charge


def generate_bill(name, units):
    """Calculate and display the complete electricity bill."""

    energy = calculate_energy_charge(units)
    fixed = FIXED_CHARGE

    tax = (energy + fixed) * TAX_RATE
    total_bill = energy + fixed + tax

    print("\n========== ELECTRICITY BILL ==========")
    print(f"Customer Name : {name}")
    print(f"Units Consumed: {units:g}")
    print("--------------------------------------")
    print(f"Energy Charge : Rs. {energy:.2f}")
    print(f"Fixed Charge  : Rs. {fixed:.2f}")
    print(f"Tax (5%)      : Rs. {tax:.2f}")
    print("--------------------------------------")
    print(f"Total Bill    : Rs. {total_bill:.2f}")
    print("======================================")


def main():
    print("===== ELECTRICITY BILL CALCULATOR =====")

    customer_name = input("Enter Customer Name: ").strip()

    try:
        units = float(input("Enter Electricity Units: "))

        if not customer_name:
            print("Invalid customer name. Please enter a name.")

        elif units < 0:
            print("Invalid units. Enter a non-negative number.")

        else:
            generate_bill(customer_name, units)

    except ValueError:
        print("Invalid units. Please enter a valid number.")


if __name__ == "__main__":
    main()
