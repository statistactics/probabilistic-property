import pandas as pd
import requests


# Get the collection of datasets from HDB website https://data.gov.sg/datasets?agencies=Housing+and+Development+Board+(HDB)&page=1&resultId=189 
collection_id = 189          
url = "https://api-production.data.gov.sg/v2/public/api/collections/{}/metadata".format(collection_id)
        
response = requests.get(url)

hdb_dataset_ids = response.json()["data"]["collectionMetadata"]["childDatasets"]


# Iterate through and append resulting dataframes into one for local export
output = []
for id in hdb_dataset_ids:
    temp_res = requests.get(f"https://api-open.data.gov.sg/v1/public/api/datasets/{id}/initiate-download").json()
    output.append(pd.read_csv(temp_res["data"]["url"]))

hdb_resale_df = pd.concat(output)

# Exporting dataframe to local .csv
hdb_resale_df.to_csv(r"/workspaces/probabilistic-property/data/raw/HDB_Resale_From_2000.csv", index = False)


