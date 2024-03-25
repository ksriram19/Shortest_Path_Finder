# compare_coordinates_with_navigation.py
from CurrentLocationFinder import get_approximate_location
from read_coordinates import read_coordinates
import webbrowser

def find_nearest_place(current_location, places_coordinates):
    if current_location is None or places_coordinates is None:
        return None

    min_distance = float('inf')
    nearest_place = None

    for place_coord in places_coordinates:
        lat, lon = place_coord
        distance = ((current_location[0] - lat)**2 + (current_location[1] - lon)**2)**0.5

        if distance < min_distance:
            min_distance = distance
            nearest_place = place_coord

    return nearest_place

def open_google_maps_navigation(current_location, destination_coordinates):
    if current_location is None or destination_coordinates is None:
        print("Error: Invalid coordinates.")
        return

    current_lat, current_lon = current_location
    destination_lat, destination_lon = destination_coordinates

    # Construct the Google Maps URL
    google_maps_url = f"https://www.google.com/maps/dir/{current_lat},{current_lon}/{destination_lat},{destination_lon}"

    # Open the URL in the default web browser
    webbrowser.open(google_maps_url)

if __name__ == "__main__":
    # Replace with the actual path of your text file containing the places' coordinates
    file_path = 'addresses.txt'
    
    # Fetch current location
    current_location = get_approximate_location()
    
    if current_location:
        print(f"Current GPS Location: {current_location}")

        # Read coordinates from file
        places_coordinates = read_coordinates(file_path)

        if places_coordinates:
            print(f"Coordinates from file: {places_coordinates}")

            # Find the nearest place
            nearest_place = find_nearest_place(current_location, places_coordinates)
        
            if nearest_place:   
                print(f"The nearest place is located at: {nearest_place}")

                # Open Google Maps navigation
                open_google_maps_navigation(current_location, nearest_place)
            else:
                print("No places found.")
        else:
            print("Could not read coordinates from file.")
    else:
        print("Error fetching current location.")
