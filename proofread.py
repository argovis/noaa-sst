# usage: python proofread.py
# expects data/sst.wkmean.1990-present.nc
import xarray, random, time, math
from pymongo import MongoClient

def tidylon(longitude):
    # map longitude on [0,360] to [-180,180], required for mongo indexing
    if longitude <= 180.0:
        return longitude;
    else:
        return longitude-360.0;

# db connection
client = MongoClient('mongodb://database/argo')
db = client.argo

# data files
upstream = xarray.open_dataset('data/sst.wkmean.1990-present.nc', decode_times=False)

# metadata record
metadata = list(db.noaaOIsstMeta.find({"_id":"noaa-oi-sst-v2"}))[0]

while True:

        latidx = math.floor(180*random.random())
        lonidx = math.floor(360*random.random())
        timeidx = math.floor(1727*random.random())
        data = list(db.noaaOIsst.find({"_id": str(tidylon(upstream['lon'][lonidx].to_dict()['data'])) + "_" + str(upstream['lat'][latidx].to_dict()['data'])}))[0]
        if data['data'][0][timeidx] != round(upstream['sst'][timeidx, latidx, lonidx].to_dict()['data'], 2):
                print(latidx, lonidx, timeidx, data['data'][0][timeidx], upstream['sst'][timeidx, latidx, lonidx].to_dict()['data'])
        else:
                print('ok')

        time.sleep(60)