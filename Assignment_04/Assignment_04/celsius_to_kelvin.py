while True:
    celsius = raw_input("Celsius: ")

    try:
        celsius = float(celsius)
        kelvin = celsius + 273.15

        if kelvin > 0:
            break

        print "Invalid input"

    except ValueError:
        print "Invalid input"

print("Celsius to Kelvin: " + str(celsius) + " > " + str(kelvin) )

