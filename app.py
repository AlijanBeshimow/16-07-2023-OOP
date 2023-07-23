from functions import add, update_service_date, view, delete
from classes import Car
from files import load_items

while True:
    option = input("""
1. Add New Car
2. Check Status by license number
3. Check Status by owner name
4. Update Service Date
5. Update Visit Date
                            Choice: """)
    print()
    if option == "1":
        name = input("car name: ")
        year = input("year: ")
        license = input("license: ")
        owner = input("owner: ")
        color = input("color: ")
        visit_date = input("visit date: ")
        service_date = input("service date: ")
        add(Car(name=name, year=year, license=license, owner=owner,
            color=color, visit_date=visit_date, service_date=service_date))

    if option == "2":
        license = input("enter license number: ")
        cars = load_items()
        for car in cars:
            if car.license == int(license):
                print(car)

    if option == 'q':
        break

    if option == 'v':
        view()

    if option == "4":
        license = input("License: ")
        date = input("Date: ")
        update_service_date(license=license, date=date)

    if option == "d":
        name = input("name: ")
        delete(name=name)
