# https://www.geeksforgeeks.org/understanding-python-pickling-example/

import pickle
from ada.scheduler.mip_scheduler import *

mypath = "agent_MPC_with_6prods2.pkl"
#mypath= "C:\\Users\Reka\Documents\GitHub\public_drl_sc\agent_MPC_with_6prods2.pkl"
with open(mypath, 'rb') as f:
    data = pickle.load(f)

