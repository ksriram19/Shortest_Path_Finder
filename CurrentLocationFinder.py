import geocoder

def get_approximate_location():
    try:
        # Using OpenCage Geocoding API
        location = geocoder.ip('me')

        if location.ok:
            return location.latlng
        else:
            print(f"Error: {location.status}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    approximate_location = get_approximate_location()

    if approximate_location:
        print(f"Approximate Location: {approximate_location}")
    else:
        print("Could not fetch approximate location.")
