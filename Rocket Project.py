# Minks Python Rocket Physics Simulator.
#Base code.
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")
#Information code.
def run_simulation():
    rocket_mass = get_float("Enter the rocket mass in kg: ")
    if rocket_mass <= 0:
        print("Rocket mass must be greater than 0")
        return
    fuel_mass = get_float("Enter the fuel mass in kg: ")
    if fuel_mass <= 0:
        print("Fuel mass must be greater than 0")
        return
    fuel_burn_rate = get_float("Enter the fuel burn rate (kg per second): ")
    if fuel_burn_rate <= 0:
        print("Fuel burn rate must be greater than 0")
        return
    total_mass = rocket_mass + fuel_mass
    print(f"Total mass: {total_mass:.2f} kg")
    thrust_power = get_float("Enter the thrust power (N): ")
    if thrust_power <= 0:
        print("Thrust must be greater than 0")
        return
    acceleration = thrust_power / total_mass
    gravity = 9.81
    net_acceleration = acceleration - gravity
    print(f"Acceleration: {acceleration:.2f} m/s²")
    print(f"Net acceleration: {net_acceleration:.2f} m/s²")
    if net_acceleration <= 0:
        print("Rocket does not have enough acceleration to lift off")
        return
    else:
        print("Rocket is ready to lift off")
    burn_time = get_int("Enter the burn time in seconds: ")
    if burn_time <= 0:
        print("Burn time must be greater than 0")
        return
#INFORMATION used in the code.
    velocity = 0
    altitude = 0
    max_altitude = 0
    max_velocity = 0
    time = 0
    reached_space = False
# Powered flight
    for second in range(burn_time):
        fuel_mass -= fuel_burn_rate
        if fuel_mass <= 0:
            print("Fuel depleted!")
            break
        total_mass = rocket_mass + fuel_mass
        acceleration = thrust_power / total_mass
        net_acceleration = acceleration - gravity
        velocity += net_acceleration
        altitude += velocity
        time += 1
        if velocity > max_velocity:
            max_velocity = velocity

        if altitude > max_altitude:
            max_altitude = altitude
        print(f"Time: {time}s | Velocity: {velocity:.2f} m/s | Altitude: {altitude:.2f} m | Fuel: {fuel_mass:.2f} kg")
        if altitude >= 100000 and not reached_space:
            print("Rocket has reached space!")
            reached_space = True
# Coasting phase
    print("Rocket is now coasting...")
    while altitude > 0:
        time += 1
        velocity -= gravity
        altitude += velocity
        if velocity > max_velocity:
            max_velocity = velocity

        if altitude > max_altitude:
            max_altitude = altitude

        if altitude < 0:
            altitude = 0
        print(f"Time: {time}s | Velocity: {velocity:.2f} m/s | Altitude: {altitude:.2f} m")
#Mission information code.
    print("\nMission complete")
    print(f"Maximum altitude reached: {max_altitude:.2f} meters")
    print(f"Maximum velocity reached: {max_velocity:.2f} m/s")
    print(f"Total flight time: {time} seconds")
# Main menu
while True:
    print("\n===== ROCKET SIMULATOR =====")
    print("1 Start Simulation")
    print("2 Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        while True:
            run_simulation()
            replay = input("\nRun another simulation? (y/n): ").lower()
            if replay == "y":
                continue
            elif replay == "n":
                break
            else:
                print("Please enter y or n.")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1 or 2.")