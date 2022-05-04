#Q2: Temperature of a city in Fahrenheit degrees is input through the keyboard.
#Write a program to convert this temperature into Centigrade degrees. 
#formula : (32°F − 32) × 5/9 = 0°C

fahrtemperature = float(input("Enter the city temperture in Fahrenheit degree : "))
centigradedegrees = (fahrtemperature - 32) * 5/9
print("Centigrade Degrees is : ",centigradedegrees)
