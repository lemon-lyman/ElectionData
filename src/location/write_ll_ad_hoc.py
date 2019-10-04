import pandas as pd
import time
import geopy
from geopy.geocoders import Nominatim


temp_start = 2545

class ll_nw:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="last_go111")
        self.error_list = []

    def get_ll(self, county, state):
        _location = self.geolocator.geocode(county + " county, " + state + " US")
        try:
            return (_location.latitude, _location.longitude)
        except AttributeError:
            self.error_list.append((county, state))
            return (10000, 10000)

cc = ll_nw()

df = pd.read_csv("../../data/countypres_2000-2016.csv", index_col=0)
df2016 = df.loc['2016']
trimmed_df2016 = df2016[['state_po', 'county']].dropna()
unique_df2016 = trimmed_df2016.drop_duplicates().copy()

latitudes = []
longitudes = []

loop_start = time.time()
total_try_loop_count = 0
try_loop_count = 0
for ii in range(temp_start, unique_df2016.shape[0]):
    row = unique_df2016.iloc[ii, :]
    total_try_loop_count = try_loop_count + total_try_loop_count
    try_loop_count = 0
    while True:
        try:
            ll = cc.get_ll(row['county'], row['state_po'])
            break
        except geopy.exc.GeocoderTimedOut:
            if try_loop_count > 10:
                print("try_loop_count > 10")
                time.sleep(10)
            time.sleep(1)
            print("try_loop_count", try_loop_count)
            try_loop_count = try_loop_count + 1
            continue

    latitudes.append(ll[0])
    longitudes.append(ll[1])
    print(ii)

print()
print("Loop time: ", time.time() - loop_start)
print("Total except_loops: ", total_try_loop_count)
print("Total location errors: ", len(cc.error_list))

# unique_df2016['latitude'] = latitudes
# unique_df2016['longitude'] = longitudes

# unique_df2016.to_csv('../../data/county_ll.csv')
