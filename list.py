class Fare_Calcu:
    def __init__(self, bus_name, passenger_name, distance):
        self.bus_name = bus_name
        self.passenger_name = passenger_name
        self.distance = distance
        self.fare = self.distance * 2.15

    def display_info(self):
        print(f"Bus Name: {self.bus_name}")
        print(f"Passenger Name: {self.passenger_name}")
        print(f"Traveled Distance: {self.distance:.1f} km")
        print(f"Fare is: {self.fare:.2f} Taka\n")

# Get the number of passengers
num_passengers = int(input("How many passengers: "))

# Create N number of objects (passenger) and calculate the fare for each passenger
for i in range(num_passengers):
    bus_name = input("Enter bus Name: ")
    passenger_name = input("Enter passenger Name: ")
    distance = float(input("Distance: "))
    passenger = Fare_Calcu(bus_name, passenger_name, distance)
    passenger.display_info()