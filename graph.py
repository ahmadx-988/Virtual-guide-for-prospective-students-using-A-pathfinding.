# graph.py

# Campus road connections
# Format:
# "Building": [(Connected Building, Distance)]

campus_graph = {

    "Main Gate": [
        ("Administration Block", 2),
        ("Cafeteria", 6)
    ],

    "Administration Block": [
        ("Main Gate", 2),
        ("Central Library", 3)
    ],

    "Central Library": [
        ("Administration Block", 3),
        ("AI Department", 2)
    ],

    "AI Department": [
        ("Central Library", 2),
        ("Cafeteria", 4),
        ("Playground", 5)
    ],

    "Cafeteria": [
        ("Main Gate", 6),
        ("AI Department", 4),
        ("Boys Hostel", 3)
    ],

    "Boys Hostel": [
        ("Cafeteria", 3),
        ("Playground", 2)
    ],

    "Playground": [
        ("AI Department", 5),
        ("Boys Hostel", 2)
    ]
}


def get_neighbors(location):
    """
    Returns connected locations
    """
    return campus_graph.get(location, [])


def show_graph():

    for place, connections in campus_graph.items():
        print(place)

        for destination, distance in connections:
            print("  ->", destination, "Distance:", distance)


if __name__ == "__main__":
    show_graph()