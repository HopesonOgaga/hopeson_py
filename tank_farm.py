import math
def calculate_tank_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
def main():
    num_tanks = int(input("Enter the number of tanks in the farm: "))

    total_volume = 0
    for i in range(1, num_tanks + 1):
        print(f"\nTank {i} dimensions:")
        radius = float(input("Enter the radius (in meters): "))
        height = float(input("Enter the height (in meters): "))

        tank_volume = calculate_tank_volume(radius, height)
        total_volume += tank_volume

    print("\nTotal volume needed to fill the tank farm: %.2f cubic meters" % total_volume)
if __name__ == "__main__":
    main()
# m.22/hnd/csc/11503