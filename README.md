# Shortest Path Finder

This script designed to find the nearest location from a set of coordinates stored in a text file. Leveraging geocoding APIs, it retrieves the approximate location based on the user's IP address. The script then reads coordinates from a specified file and calculates the distance between the user's location and each coordinate. Finally, it generates a Google Maps URL for navigation to the nearest place.

To utilize Flask Location Finder, simply execute the script. It will automatically fetch the user's approximate location and compare it with coordinates stored in the provided text file. The script outputs the nearest place along with its coordinates and opens a Google Maps navigation link in the default web browser. Ensure that the text file containing coordinates is properly formatted and located in the specified path for accurate results.
