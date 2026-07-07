# campus.py

campus_data = {

    "Main Gate": {
        "info": "Main entrance of University of Haripur campus.",
        "type": "Entrance"
    },

    "Administration Block": {
        "info": "Office area for university administration, admissions and records.",
        "type": "Office"
    },

    "Central Library": {
        "info": "University library containing books, research material and study areas.",
        "type": "Library"
    },

    "AI Department": {
        "info": "Department for Artificial Intelligence and Computer Science students.",
        "type": "Department"
    },

    "Cafeteria": {
        "info": "Food and relaxation area for students.",
        "type": "Food Area"
    },

    "Boys Hostel": {
        "info": "Residential facility for male students.",
        "type": "Hostel"
    },

    "Playground": {
        "info": "Sports and recreational area of the university.",
        "type": "Sports"
    }
}


def get_buildings():
    return list(campus_data.keys())


def get_building_info(name):
    if name in campus_data:
        return campus_data[name]["info"]
    return "Information not available."