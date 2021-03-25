# import os 
# import pickle
# import requests
# import zipfile
# import io
# import json 
# dirname = os.path.dirname(__file__)
# available_models = os.listdir(dirname)
# available_models = [model for model in available_models if ".pickle" in model and "data" in model]
# model_names = [
#                'training_data_WEST.pickle', 'training_data_NORTH.pickle', 
#                'training_data_CENTRL.pickle', 'training_data_MILLWD.pickle', 
#                'training_data_MHK VL.pickle', 'training_data_h24.pickle', 
#                'training_data_LONGIL.pickle', 'training_data_DUNWOD.pickle', 
#                'training_data_CAPITL.pickle', 'training_data_GENESE.pickle',
#                'training_data_HUD VL.pickle', 'training_data_N.Y.C..pickle', 
               
#             ]
# import json


# url = "http://35.229.113.99/api/models/training_data?key=orenda1234"
# response = requests.get(url)
# with zipfile.ZipFile(io.BytesIO(response.content)) as zfile:
#     f_names = sorted(zfile.namelist())
#     for f in f_names:
#         name = f.split('/')[-1] # get <training_data_%region.pickle>
#         if name in model_names:
#             server_dic = pickle.load(zfile.open(f))
#             file_dir = os.path.join('./src/ml/models/saved_data', name)
#             with open(file_dir, 'rb') as f:
#                 existing_dic = pickle.load(f)
#             for key in server_dic.keys():
#                 existing_dic[key] = server_dic[key]
#             with open(file_dir, 'wb') as f:
#                 pickle.dump(existing_dic, f)