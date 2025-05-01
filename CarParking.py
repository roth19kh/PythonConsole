totalCharge ="";
totalRiel ="";
rate="";

vehicleType = input("Enter parking vehicle type (Moto,Car):")

while vehicleType.lower() not in ["moto","car"] :
    vehicleType = input("Enter parking vehicle type again(Moto,Car):")
hourDuration = float(input("Enter parking time (Hour): "))
if vehicleType.lower() in ["moto"]:
    if int(hourDuration) < 1:
        totalCharge = hourDuration * 0
        print("Free parking")
    elif int(hourDuration) < 3:
        rate = 0.15
        totalCharge = 0.15 * hourDuration
        TotalRiel = totalCharge * 4100
    else:
        oldTime = hourDuration - 3
        rate = 0.25
        totalCharge = (3 * 0.15) + (oldTime * 0.25)
        TotalRiel = totalCharge * 4100
else:
    if int(hourDuration) < 1:
        rate = 0.25
        totalCharge = hourDuration * 0.25
    elif int(hourDuration) < 3:
        oldTime = hourDuration - 1
        rate = 0.25
        totalCharge = (1 * 0.15) + (oldTime * 0.25)
        TotalRiel = totalCharge * 4100
    else:
        oldTime = hourDuration - 3
        rate = 0.50
        totalCharge = (3 * 0.25) + (oldTime * 0.50)
        TotalRiel = totalCharge * 4100
print("Total Charge: ", totalCharge , "$")
print("Rate: ",rate, "/h")
print(f"Total Riel: {TotalRiel:,.2f}៛")
print("Vehicle Type: ", vehicleType)
print("HourDuration: ", int(hourDuration))