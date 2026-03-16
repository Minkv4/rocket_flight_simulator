# Minks Python Rocket Physics Simulator.
#Base code.
SPACE_ALTITUDE = 100000
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
def run_simulation():
#Planet choice menu code.
    print("\nChoose a planet:")
    print("1. Mercury")
    print("2. Venus")
    print("3. Earth")
    print("4.The Moon")
    print("5. Mars")
    print("6. Jupiter")
    print("7. Saturn")
    print("8. Uranus")
    print("9. Neptune")
    planet_choice = input("Select planet (1-9): ")
    if planet_choice == "1":
        planet_name = "Mercury"
        gravity = 3.7
        drag_coefficient = 0
    elif planet_choice == "2":
        planet_name = "Venus"
        gravity = 8.87
        drag_coefficient = 0.0004
    elif planet_choice == "3":
        planet_name = "Earth"
        gravity = 9.81
        drag_coefficient = 0.0002
    elif planet_choice == "4":
        planet_name = "Moon"
        gravity = 1.62
        drag_coefficient = 0
    elif planet_choice == "5":
        planet_name = "Mars"
        gravity = 3.71
        drag_coefficient = 0.00005
    elif planet_choice == "6":
        planet_name = "Jupiter"
        gravity = 24.79
        drag_coefficient = 0.0006
    elif planet_choice == "7":
        planet_name = "Saturn"
        gravity = 10.44
        drag_coefficient = 0.0003
    elif planet_choice == "8":
        planet_name = "Uranus"
        gravity = 8.69
        drag_coefficient = 0.0002
    elif planet_choice == "9":
        planet_name = "Neptune"
        gravity = 11.15
        drag_coefficient = 0.00025
    else:
        print("Invalid planet")
        return
    print(f"\nLaunching from {planet_name}")
    print(f"Gravity: {gravity} m/s²")
    print(f"Atmospheric drag factor: {drag_coefficient}")

# Rocket choice menu code
    print("\nChoose a rocket:")
    print("1. Space Launch System (SLS)")
    print("2. Falcon 9")
    print("3. Saturn V")
    print("4. SpaceX Starship")
    print("5. Custom Rocket")
    rocket_choice = input("Select option (1-5): ")
    if rocket_choice == "1":
        rocket_mass = 600000
        fuel_mass = 2000000
        thrust_power = 39000000
        fuel_burn_rate = 12000
    elif rocket_choice == "2":
        rocket_mass = 549000
        fuel_mass = 395000
        thrust_power = 7600000
        fuel_burn_rate = 2500
    elif rocket_choice == "3":
        rocket_mass = 670000
        fuel_mass = 2300000
        thrust_power = 34000000
        fuel_burn_rate = 13000
    elif rocket_choice == "4":
        rocket_mass = 1200000
        fuel_mass = 3600000
        thrust_power = 74000000
        fuel_burn_rate = 18000
    elif rocket_choice == "5":
        rocket_mass = get_float("Enter the rocket mass in kg: ")
        fuel_mass = get_float("Enter the fuel mass in kg: ")
        fuel_burn_rate = get_float("Enter the fuel burn rate (kg/s): ")
        thrust_power = get_float("Enter the thrust power (N): ")
    else:
        print("Invalid choice")
        return
    total_mass = rocket_mass + fuel_mass
    print(f"\nRocket mass: {rocket_mass} kg")
    print(f"Fuel mass: {fuel_mass} kg")
    print(f"Total mass: {total_mass} kg")
    print(f"Thrust: {thrust_power} N")
    velocity = 0
    altitude = 0
    acceleration = thrust_power / total_mass
    drag = drag_coefficient * velocity * abs(velocity)
    net_acceleration = acceleration - gravity - drag
    print(f"Acceleration: {acceleration:.2f} m/s²")
    print(f"Net acceleration: {net_acceleration:.2f} m/s²")
    if net_acceleration <= 0:
        print("Rocket does not have enough acceleration to lift off")
        return
    print("Rocket is ready to lift off")
    burn_time = get_int("Enter burn time in seconds: ")

#INFORMATION for the simulation.
    max_altitude = 0
    max_velocity = 0
    time = 0
    reached_space = False

#Lanuch countdown timer code.
    import time as t
    print("\nLaunch sequence starting...")
    for i in range(5, 0, -1):
        print(i)
        t.sleep(1)
    print("LIFTOFF 🚀")

# Powered flight code.
    for second in range(burn_time):
        fuel_mass -= fuel_burn_rate
        if fuel_mass <= 0:
            print("Fuel depleted!")
            break
        total_mass = rocket_mass + fuel_mass
        acceleration = thrust_power / total_mass
        drag = drag_coefficient * velocity * abs(velocity)
        net_acceleration = acceleration - gravity - drag
        velocity += net_acceleration
        altitude += velocity
        time += 1
        if velocity > max_velocity:
            max_velocity = velocity

        if altitude > max_altitude:
            max_altitude = altitude
        print(
            f"Time: {time}s | Velocity: {velocity:.2f} m/s | Altitude: {altitude:.2f} m | Fuel: {fuel_mass:.2f} kg")
        bar_length = min(int(altitude / 10000), 50)
        print(f"Altitude: {altitude:.0f} m | {'#' * bar_length}")
        if altitude >= SPACE_ALTITUDE and not reached_space:
            print("Rocket has reached space! 🚀")
            reached_space = True

# Coasting phase code.
    print("Rocket is now coasting...")
    while altitude > 0:
        time += 1
        drag = drag_coefficient * velocity * abs(velocity)
        velocity += -gravity - (drag * (1 if velocity >= 0 else -1))
        altitude += velocity
        if velocity > max_velocity:
            max_velocity = velocity

        if altitude > max_altitude:
            max_altitude = altitude

        if altitude < 0:
            altitude = 0
#Landing checking code.
            if velocity < -20:
                print("Rocket crashed! 💥")
            else:
                print("Rocket landed safely! 🛬")
#Coasting phase code.
        print(
            f"Time: {time}s | Velocity: {velocity:.2f} m/s | Altitude: {altitude:.2f} m")
        if altitude >= SPACE_ALTITUDE and not reached_space:
            print("Rocket has reached space! 🚀")
            reached_space = True

# Mission results code.
    print("\nMission complete")
    print(f"Maximum altitude reached: {max_altitude:.2f} meters")
    print(f"Maximum velocity reached: {max_velocity:.2f} m/s")
    print(f"Total flight time: {time} seconds")
    if max_altitude >= SPACE_ALTITUDE:
        print("Mission Result: SUCCESS 🚀")
    elif max_altitude >= 50000:
        print("Mission Result: Suborbital Flight")
    else:
        print("Mission Result: Failed Launch")

# Main menu code.
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


