#3. Accept any city from the user and display monuments of that city.
#City      Monuments
#Kathmandu Pashupati Nath
#Bhaktapur Bhaktapur Durbar Square
#Janakpur  Janaki Mandir

city = input("Enter city: ").lower()

if city == "kathmandu":
    print("Pashupati Nath")
elif city == "bhaktapur":
    print("Bhaktapur Durbar Square")
elif city == "janakpur":
    print("Janaki Mandir")
else:
    print("City not found")
