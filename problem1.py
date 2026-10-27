class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self, distance):
        return self.capacity * distance * 2.15

class Bus(Vehicle):
    def fare(self, distance):
        total_fare = super().fare(distance)
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge

# Get the bus details
bus_name = input("Enter Bus Name: ")
capacity = int(input("Enter Capacity: "))
distance = int(input("Enter Distance: "))

# Create a Bus object and calculate the fare
bus = Bus(bus_name, capacity)
total_fare = bus.fare(distance)

# Display the bus details and total fare
print("\nBus Details:")
print(f"Bus Name: {bus_name}")
print(f"Total Seat: {capacity}")
print(f"Traveled Distance: {distance}")
print(f"Total Fare: {total_fare:.2f}")