#Task 1: Formatting Flight Itineraries
#Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the 
# input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
#"Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"

def format_itinerary():
    itinerary_list = []
    num_itineraries = int(input("How many itineraries would you like to enter?: "))
    for i in range(num_itineraries):
        traverler_name = input(f"Enter traverlers name for itinerary {i+1}: ")
        origin = input(f"Enter the origin for itinerary {i+1}: ")
        destination = input(f"Enter the destination for itinerary {i+1}: ")
        itinerary_list.append((traverler_name, origin, destination))
    formatted_string = ""
    for i, itinerary in enumerate(itinerary_list, start=1):
        formatted_string += f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}\n"
    return formatted_string.strip()
formatted_output = format_itinerary()
print(formatted_output)

