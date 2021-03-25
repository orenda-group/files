# 
import os 
import pickle
import requests
import zipfile
import io
model_names = [
               'training_data_WEST.pickle', 'training_data_NORTH.pickle', 
               'training_data_CENTRL.pickle', 'training_data_MILLWD.pickle', 
               'training_data_MHK VL.pickle', 'training_data_h24.pickle', 
               'training_data_LONGIL.pickle', 'training_data_DUNWOD.pickle', 
               'training_data_CAPITL.pickle', 'training_data_GENESE.pickle',
               'training_data_HUD VL.pickle', 'training_data_N.Y.C..pickle', 
               
            ]

def transfer_pickle_files():
    url = 'https://github.com/orenda-group/files/blob/master/training_data.zip?raw=true'
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zfile:
        f_names = sorted(zfile.namelist())
        for f in f_names:
            name = f.split('/')[-1]  # get <training_data_%region.pickle>
            if name in model_names:
                file_store_dic = pickle.load(zfile.open(f))
                keys = list(file_store_dic.keys())
                print(keys[0][0], keys[-1][0])