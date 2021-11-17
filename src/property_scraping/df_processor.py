import pandas as pd
import constants

### Constants ###

df_columns = ['Website',
              'Name',
              'Address',
              'Rent',
              'Availability',
              'Bedrooms',
              'Bathrooms',
              'Total Area',
              'MRT Distance',
              'Property Type',
              'Built Year',
              'URL']


### Methods ###

def property_guru_processor(data):
    df = pd.DataFrame(columns=df_columns)
    listings = data[0]
    features = data[1]
    types = data[2]
    urls = data[3]
    print("Listings: ", listings)
    print("Features: ", features)
    print("Types: ", types)
    names = []
    names = list(map(lambda x: x.split('\n')[0], listings))
    addresses = list(map(lambda x: x.split('\n')[-1], listings))
    rents = list(map(lambda x: x.split('\n')[0], features[::3]))
    availabilities = list(map(lambda x: x.split('\n')[1], features[::3]))
    bedrooms = list(map(lambda x: x.split('\n')[0][0], features[1::3]))
    bathrooms = list(map(lambda x: x.split('\n')[0][-1], features[1::3]))
    total_areas = list(map(lambda x: x.split('\n')[1], features[1::3]))
    mrt_distances = list(map(lambda x: x.split('\n')[0], features[2::3]))
    property_types = list(map(lambda x: x.split('\n')[0], types))
    built_years = list(map(lambda x: x.split('\n')[-1], types))
    df['Name'] = names
    df['Address'] = addresses
    df['Rent'] = rents
    df['Availability'] = availabilities
    df['Bedrooms'] = bedrooms
    df['Bathrooms'] = bathrooms
    df['Total Area'] = total_areas
    df['MRT Distance'] = mrt_distances
    df['Property Type'] = property_types
    df['Built Year'] = built_years
    df['URL'] = urls
    df['Website'] = 'PropertyGuru'
    print(df)
    print("=" * 30)
    print("Done creating PropertyGuru dataframe")
    print("=" * 30)
    return df


def ninety_nine_co_processor():
    return


def merge_dfs(df_list):
    main_df = pd.DataFrame(columns=df_columns)
    for df in df_list:
        main_df = pd.concat([main_df, df], ignore_index=True)

    main_df.to_csv(constants.results_path, index=False)
    return main_df
