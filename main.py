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

def show_keys(url='github',display='first-all'):
    if url == 'github':
        url = 'https://github.com/orenda-group/files/blob/master/training_data.zip?raw=true'
    else: 
        url = 'http://35.229.113.99/api/models/training_data?key=orenda1234'
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zfile:
        f_names = sorted(zfile.namelist())
        max_data, min_data = 0,10000 
        num_points = {}
        for f in f_names:
            name = f.split('/')[-1]  # get <training_data_%region.pickle>
            if name in model_names:
                file_store_dic = pickle.load(zfile.open(f))
                keys = list(file_store_dic.keys())
                print(name)
                if (len(keys) < min_data) & (name != "training_data_h24.pickle"):
                    min_data = len(keys)
                    min_list = keys
                if (len(keys) > max_data) and (name != "training_data_h24.pickle"):
                    max_data = len(keys) 
                    max_list = keys
                num_points[name] = len(keys)
                if display == 'first-last':
                    print(keys[0][0], keys[-1][0])
                elif display == 'first-all':
                    print(*keys, sep='\n')
    for point in max_list:
        if point not in min_list:
            print('PROBLEM HERE',point)
    for key in num_points.keys():
        print('number of points:', num_points[key])



if __name__ == "__main__":
    show_keys(url='notgit')