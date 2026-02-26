
import pandas as pd
import numpy as np
import haversine as hs
from haversine import Unit

inputPostCode = "B10 0AB"

# import uk postcodes
colNames = ["Nation", "PostCode", "City", "Country", "CountryAbreviation", "County", "Unnamed1", "District", "Unnamed2", "Lat", "Long", "Id"]
dType= {"Unnamed1": str, "District":str, "Lat":float, "Long":float}
uk_postcodes_df = pd.read_csv("GB_full.txt", delimiter="\t", names=colNames, dtype=dType)

# import nhs locations
Nhs_df = uk_postcodes_df.sample(20) # replace this with nhs locations database

# select input postcode row in uk postcode df
inputPostcode_df = uk_postcodes_df.loc[uk_postcodes_df.PostCode == inputPostCode]

# calculate harversine distance from input postcode to all nhs locations
loc1=(inputPostcode_df.Lat.to_numpy()[0], inputPostcode_df.Long.to_numpy()[0])
loc2 = Nhs_df[["Lat", "Long"]].to_numpy()

distances=hs.haversine_vector(loc1,loc2,unit=Unit.KILOMETERS, comb=True)
Nhs_df["Distance2InputPostCode"] = distances

# sort by distance
Nhs_df = Nhs_df.sort_values("Distance2InputPostCode")

print(Nhs_df)













# a = df.PostCode == inputPostCode
# i = [i for i, x in enumerate(a) if x]

# lat = np.array(df.Lat)[i]
# long = np.array(df.Long)[i]


# print(f"Lat: {lat}, Long: {long}")
# print()
# print()