celsius = float(input("Suhu (C): "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
status = "Panas" if celsius > 30 else "Normal"

print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin: {kelvin:.2f}")
print(f"Status: {status}")