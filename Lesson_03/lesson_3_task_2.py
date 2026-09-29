from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 5", "+79220000001"),
    Smartphone("Samsung", "Galaxy S21", "+79220000002"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79320000003"),
    Smartphone("Realmi", "№8", "+79190000004"),
    Smartphone("Honor", "Magic 6", "+79120000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")