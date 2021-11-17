user_query_dict = {}

def queryUserSelections():
    websites = input("Select the websites you want to query \n"
                     "1. Property Guru\n"
                     "2. 99Co\n")
    mrt = input("Please input your desired MRT stations, separated by comma: ")
    bedrooms = input ("How many bedrooms are you looking for: ")
    bathrooms = input ("How many bathrooms do you desire: ")
    max_rent = input ("What is the MAXIMUM rent: ")
    min_rent = input ("What is your MINIMUM rent: ")

    mrt = mrt.split(",")
    bedrooms = bedrooms.split(",")
    bathrooms = bathrooms.split(",")
    user_query_dict['Websites'] = websites
    user_query_dict['MRT'] = mrt
    user_query_dict['Bedrooms'] = bedrooms
    user_query_dict['Bathrooms'] = bathrooms
    user_query_dict['Maximum Price'] = max_rent
    user_query_dict['Minimum Price'] = min_rent
    return user_query_dict
