destinations = [
    "Paris, France",
    "Shanghai, China",
    "Los Angeles, USA",
    "São Paulo, Brazil",
    "Cairo, Egypt"
]

test_traveller = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    # if destination in destinations:
        destination_index = destinations.index(destination)
        return destination_index

def get_traveler_location(traveler):
        traveler_destination = traveler[1]
        traveler_destination_index = get_destination_index(traveler_destination)
        return traveler_destination_index

print(get_traveler_location(test_traveller))