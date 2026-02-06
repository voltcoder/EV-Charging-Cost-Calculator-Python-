def calculate_charging_cost(battery_capacity, current_soc, target_soc, price_per_kwh):
    energy_needed = battery_capacity * (target_soc - current_soc) / 100
    cost = energy_needed * price_per_kwh
    return energy_needed, cost


try:
    battery_capacity = float(input("Enter battery capacity (kWh): "))
    current_soc = float(input("Enter current charge percentage: "))
    target_soc = float(input("Enter target charge percentage: "))
    price_per_kwh = float(input("Enter electricity price per kWh: "))

    if current_soc >= target_soc:
        print("Target charge must be higher than current charge.")
    else:
        energy, total_cost = calculate_charging_cost(
            battery_capacity, current_soc, target_soc, price_per_kwh
        )

        print(f"\nEnergy required: {energy:.2f} kWh")
        print(f"Estimated charging cost: ₹{total_cost:.2f}")

except ValueError:
    print("Please enter valid numeric values.")
