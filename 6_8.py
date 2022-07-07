n = input("Введите город ")
country = {
    1: {
        "country": "Беларусь",
        "city": "Минск"
    },
    2: {
        "country": "Украина",
        "city": "Киев"
    }
}
for country in country.values():
    if n in country:
        print(country["country"])
