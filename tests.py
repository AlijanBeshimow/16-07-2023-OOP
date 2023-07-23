from functions import add, view, load_items, update_service_date, history_service_display
from classes import Car, ElectricCar
import random
from files import load_items


def create_cars(num: int = 0):
    for _ in range(num):
        owner = random.choice(
            ['avi', 'tal', 'gal', 'alex', 'dani', 'shai', 'mike', 'haim', 'rafi', 'guy'])
        name = random.choice(
            ['mazda', 'toyota', 'bmw', 'audi', 'hyundai', 'tesla', 'opel', 'honda', 'kia', 'suzuki'])
        license = random.randrange(60000000, 80000000)
        year = random.randrange(2010, 2024)
        visit_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        service_date = f"{random.randrange(1,31)}-{random.randrange(1,12)}-{random.randrange(2020,2023)}"
        address = random.choice(
            ['telaviv', 'haifa', 'batyam', 'holon', 'ramle', 'lod', 'beersheva'])
        add(Car(name=name, year=year, color=random.choice(
            ['red', 'blue', 'gold', 'silver', 'green']), license=license, owner=owner, visit_date=visit_date, service_date=service_date, address=address))
    view()


# Targil 1
def find_name_year():
    car_name = input("Car name: ")
    car_year = int(input("Car year: "))
    cars = load_items()
    for car in cars:
        if car.name == car_name and car.year == car_year:
            print("FInd:", car.name.capitalize(), car.year, car.owner)


# Targil 2
def find_license():
    license = int(input("Enter license number: "))
    cars = load_items()
    for car in cars:
        if car.license == license:
            print(car)


# Targil 3-4
def get_year(date):
    return int(date[-4:])


def check_visit_date():
    cars = load_items()
    for car in cars:
        if get_year(car.service_date) == 2022:
            print(car.name, car.service_date)


# Targil 5
def check_haifa():
    cars = load_items()
    for car in cars:
        if car.address == 'haifa':
            print(car.owner, car.address)


# Targil 6 - Bonus
def sort_cars_by_year():
    cars = load_items()
    sorted_cars = sorted(cars, key=lambda car: car.year, reverse=True)
    return sorted_cars


# sorted_colors = sort_cars_by_year()
# for car in sorted_colors:
#     print(car)


# Targil 7 Bonus
def sort_cars_by_color():
    cars = load_items()
    sorted_colors = sorted(cars, key=lambda car: car.color, reverse=True)
    return sorted_colors


# sorted_colors = sort_cars_by_color()
# for car in sorted_colors:
#     print(car)


# def get_license():
#     cars = load_items()
#     return cars[random.randint(5, 20)].license


# l = get_license()
# update_service_date(license=l, date="10-99-99")

# history_service_display(license=l)

# view()

# cars = load_items()
# cars.sort(key=lambda c: int(c.year), reverse=True)
# for car in cars:
#     print(car)

# ec = ElectricCar()
# print(ec.battery)
# ec.battery = "90%"
# print(ec.battery)
view()
