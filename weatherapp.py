weather = input("Enter a season (Summer, Winter, Spring, Autumn): ")

if weather == "Summer":
    print("Temperature: 35°C - 45°C")
    print("Weather: Sunny")
    print("Humidity: 20%")

elif weather == "Winter":
    print("Temperature: 10°C - 20°C")
    print("Weather: Cold")
    print("Humidity: 60%")

elif weather == "Spring":
    print("Temperature: 20°C - 30°C")
    print("Weather: Mild")
    print("Humidity: 40%")

elif weather == "Autumn":
    print("Temperature: 18°C - 28°C")
    print("Weather: Windy")
    print("Humidity: 50%")

else:
    print("Invalid season.")