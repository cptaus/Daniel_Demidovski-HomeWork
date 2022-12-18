import pickle
from os import path

import back_end
from back_end import core, manager, client

if __name__ == "__main__":

    # CHECK IF DATA PICKLE FILE IS PRESENT OR NOT
    # IF NOT CREATE NEW ONE WITH THE NULL DATA
    if not path.exists('bus_company_data.pickle'):
        bus_company_data = back_end.core.BestBusCompany()
    else:
        with open('bus_company_data.pickle', 'rb') as file:
            bus_company_data = pickle.load(file)

    # HERE GOES ALL THE INTERACTIONS
    client.main_program(bus_company_data)
    print("PROGRAM ENDED")

    # BEFORE EXITING MAKE SURE TO STERILIZE AND SAVE DATA INTO PICKLE FILE
    with open('bus_company_data.pickle', 'wb') as file:
        pickle.dump(bus_company_data, file)
