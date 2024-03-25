# read_coordinates.py
def read_coordinates(file_path):
    coordinates = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                lat, lon = map(float, line.strip().split(','))
                coordinates.append((lat, lon))
        return coordinates

    except Exception as e:
        print(f"An error occurred while reading coordinates: {e}")
        return None

if __name__ == "__main__":
    file_path = 'addresses.txt'  # Change this to the path of your text file
    places_coordinates = read_coordinates(file_path)

    if places_coordinates:
        print(f"Coordinates from file: {places_coordinates}")
    else:
        print("Could not read coordinates from file.")
