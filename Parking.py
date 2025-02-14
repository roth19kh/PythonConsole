print("Parking")

vehicleType = input("Enter type of vehicle: ")
parkingTime = float(input("Enter parking time (Hour): "))

if vehicleType == "Moto" or vehicleType == "moto":
    parkingPrice = 0.5 * parkingTime
    print("Vehicle type: " + vehicleType)
    print("Parking Rate is 0.5$/1h")
    print("Parking Charge($): " + str(parkingPrice) + "$")
    priceKhmer = parkingPrice * 4000
    print("Parking Charge(៛): " + str(priceKhmer) +"៛")
elif vehicleType ==  "Car" or vehicleType == "car":
    parkingPrice = 1 * parkingTime
    print("Vehicle type: " + vehicleType)
    print("Parking Rate is 1$/1h")
    print("Parking Charge($): " + str(parkingPrice) + "$")
    priceKhmer = parkingPrice * 4000
    print("Parking Charge(៛): " + str(priceKhmer) +"៛")
elif vehicleType ==  "truck" or vehicleType == "Truck":
    parkingPrice = 2 * parkingTime
    print("Vehicle type: " + vehicleType)
    print("Parking Rate is 2$/1h")
    print("Parking Charge($): " + str(parkingPrice) + "$")
    priceKhmer = parkingPrice * 4000
    print("Parking Charge(៛): " + str(priceKhmer) +"៛")
elif vehicleType ==  "Bus" or vehicleType == "Bus":
    parkingPrice = 3 *parkingTime
    print("Vehicle type: " + vehicleType)
    print("Parking Rate is 3$/1h")
    print("Parking Charge($): " + str(parkingPrice) +"$")
    priceKhmer = parkingPrice * 4000
    print("Parking Charge(៛): " + str(priceKhmer) +"៛")
else:
    print("Invalid vehicle type")