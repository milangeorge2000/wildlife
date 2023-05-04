import geocoder

def get_current_location():
    location = geocoder.ip('me')
    return location.latlng

latitude, longitude = get_current_location()
print(f"Latitude: {latitude}, Longitude: {longitude}")
