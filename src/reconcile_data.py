import pandas as pd


def create_formatted_data():

    county_ll_df = pd.read_csv('../data/county_ll.csv')
    election_data_df = pd.read_csv('../data/countypres_2000-2016.csv', index_col=[0, 2, 3]).loc[2016].dropna()
    formatted_data = []

    ii_count = 0
    print()
    print("Formatting Data")
    print("---------------")
    for ii in range(county_ll_df.shape[0]):

        state, county, latitude, longitude = county_ll_df.iloc[ii][['state_po',
                                                                   'county',
                                                                   'latitude',
                                                                   'longitude']]

        county_data = election_data_df.loc[state].loc[county]
        dem_votes = county_data.loc[county_data['party']=='democrat']['candidatevotes'].values.astype(int)[0]
        rep_votes = county_data.loc[county_data['party']=='republican']['candidatevotes'].values.astype(int)[0]

        if dem_votes>rep_votes:
            party = 'D'
        else:
            party = 'R'

        total_votes = county_data.iloc[0]['totalvotes']
        formatted_data.append((latitude, longitude, party, total_votes))

        if 100*ii/county_ll_df.shape[0] > ii_count:
            ii_count = ii_count + 10
            print("% " + str(ii_count))
    return formatted_data
