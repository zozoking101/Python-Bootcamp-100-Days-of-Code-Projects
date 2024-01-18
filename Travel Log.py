capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Italy",
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuggart",]
    
}
travel_log = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
    },
    {
        "Country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuggart"], 
        "total_visits": 15,
    }
]
print(travel_log[1])   


travel_log = [
    {
        "country": "France",
        "vsits": 12,
        "cities": ["Paris", "Lille", "Dijon"], 
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Harmburg", "Stuggart"],
    }
]

def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Ukraine"])
print(travel_log)