import sys
import os, re
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(parent_dir,'FastBATLLNN','HyperplaneRegionEnum'))
import numpy as np
import pickle
import itertools

import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.optim as  optim
import torch.nn as nn
import pdb
with open('results_combined.p','rb') as fp:
        database = pickle.load(fp)
# pdb.set_trace()
def extract_info(data_list):
    extracted_info = []
    # pdb.set_trace()
    for item in data_list:
        d = item.get('d',None)
        N = item.get('N',None)
        bd = item.get('bd',None)
        m = item.get('m',None)
      
        supLevelTime = item['sysInfo']['charm']['supLevelTime']
        regionTime = item['allRegs']['stats']['regionTime']
        time = supLevelTime - regionTime
        extracted_info.append({'d': d, 'N': N,'bd':bd,'m':m,
                               'supLevelTime': supLevelTime, 'regionTime':regionTime,
                               'time': time})
        print(f"d: {d}, N: {N},bd:{bd},m:{m},time: {time}")
    return extracted_info
# Call the function and store the result
info = extract_info(database)
# pdb.set_trace()
with open('results_extracted_time.p','wb') as file:
    pickle.dump(info,file)