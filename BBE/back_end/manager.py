from back_end import core
from back_end.core import console_cleaner as clean_screen
from back_end.core import wait_for_user_continue as wait_for_user


def admin_menu(data):
    clean_screen()
    selection_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "exit"]
    context = f"""
    Hello manager, what you would like to do?
    _Route related:_
    a1. add route
    a2. edit route
    a3. delete route
    a4. show routes
    a5. find route
    
    _Ride related:_
    b1. add ride
    b2. delete ride

    exit. exit the admin panel"""
    while True:
        print(context)
        selection = input("Please chose: ")
        if selection not in selection_list:
            clean_screen()
            print(f"Please select from the list... {selection} not in the list.")
            continue
        else:
            if selection == "a1":
                add_route(data)
                wait_for_user()
            if selection == "a2":
                edit_route(data)
                wait_for_user()
            if selection == "a3":
                delete_route(data)
                wait_for_user()
            if selection == "a4":
                show_routes(data)
                wait_for_user()
            if selection == "a5":
                find_route(data)
                wait_for_user()
            if selection == "b1":
                add_ride(data)
                wait_for_user()
            if selection == "exit":
                break


def show_routes(data):
    clean_screen()
    print(data.get_routes())


def find_route(data, line_number=None):
    finding = False
    while True:
        clean_screen()
        if line_number is None:
            finding = True
            line_number = input("Please insert desired line number: ")
        else:
            line_number = line_number
            break
        if line_number == "":
            print("Please insert data.")
            continue
        else:
            break
    if finding:
        print(data.get_route(line_number))
        return data.get_route(line_number)
    else:
        return data.get_route(line_number)


def add_route(data=None, editing=False, edit_stops=True, line_if_editing=None):
    stops_list = []
    line_number = ""
    if not editing:
        while True:
            clean_screen()
            line_number = input("Please insert line number: ")
            if line_number == "":
                print("Please insert data.")
                continue
            else:
                break
    while True:
        clean_screen()
        origin = input("Please insert start station: ")
        if origin == "":
            print("Please insert data.")
            continue
        else:
            break
    while True:
        clean_screen()
        destination = input("Please insert end station: ")
        if destination == "":
            print("Please insert data.")
            continue
        else:
            break

    station_order = 1

    if edit_stops:
        while True:
            clean_screen()
            stop = input(f"Please insert the {station_order} station name:(for finish insert 0)").strip().title()
            if stop is None or "":
                print("Please insert the station number...")
            if stop == "0":
                for s in stops_list:
                    print(s)
                print(f"{line_if_editing if editing else line_number}|{origin}->{destination} and stations above^")
                answer = input("Confirm? y/n").strip().lower()
                if answer == "y":
                    if not editing:
                        new_route = core.Route(line_number, origin, destination, stops_list)
                        data.add_route(new_route)
                        break
                    break
                if answer == "n":
                    return
            else:
                stops_list.append(stop)
                station_order += 1
                del stop
    if editing and edit_stops:
        return origin, destination, stops_list
    if editing:
        return origin, destination
    if edit_stops:
        return stops_list


def edit_route(data):
    while True:
        clean_screen()
        line_number = input("Please insert desired line number: ")
        if line_number == "":
            print("Please insert data.")
            continue
        else:
            pass
        print(data.get_route(line_number))
        answer = input("Are you sure you want to change this line? y/n").strip().lower()
        if answer == "y":
            sub_answer = input("""Please chose below:
            1. edit origin and destination
            2. edit all\n""")

            if sub_answer == "1":
                temp_data = add_route(data,
                                      editing=True,
                                      edit_stops=False,
                                      line_if_editing=line_number)
                if temp_data:
                    data.edit_route(l_number=line_number,
                                    origin=temp_data[0],
                                    destination=temp_data[1])
                break

            if sub_answer == "2":
                temp_data = add_route(data, editing=True,
                                      edit_stops=True,
                                      line_if_editing=line_number)
                if temp_data:
                    data.edit_route(l_number=line_number,
                                    origin=temp_data[0],
                                    destination=temp_data[1],
                                    stops_list=temp_data[2])
                break
            else:
                print("Please chose option from above.")
                continue
        if answer == "n":
            break


def delete_route(data):
    while True:
        clean_screen()
        line_number = input("Please insert desired line number: ")
        if line_number == "":
            print("Please insert data.")
            continue
        else:
            pass
        print(data.get_route(line_number))
        answer = input("Are you sure you want to delete this line? y/n").strip().lower()
        if answer == "y":
            data.delete_route(line_number)
            break
        if answer == "n":
            break


def add_ride(data):
    delays = []
    line_number = ""
    while True:
        clean_screen()
        line_number = input("Please insert line number: ")
        if line_number == "":
            print("Please insert data.")
            continue
        else:
            break
    while True:
        clean_screen()
        origin_time = input("Please insert start time HH:MM: ")
        if origin_time == "":
            print("Please insert data.")
            continue
        else:
            break
    while True:
        clean_screen()
        destination_destination = input("Please insert end time HH:MM: ")
        if destination_destination == "":
            print("Please insert data.")
            continue
        else:
            break
    while True:
        clean_screen()
        driver_name = input("Please insert full driver name: ")
        if driver_name == "":
            print("Please insert data.")
            continue
        else:
            break

    while True:
        clean_screen()
        print(f"{line_number}|{origin_time}->{destination_destination} Driver: {driver_name}")
        answer = input("Confirm? y/n").strip().lower()
        if answer == "y":
            new_ride = core.Ride(origin_time, destination_destination, driver_name, delays)
            find_route(data, line_number).add_ride(new_ride)
            break
        if answer == "n":
            return

def program(data):
    print(admin_menu(data))
