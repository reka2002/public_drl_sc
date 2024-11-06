# heuristic_planner - Implements planning heuristics for baseline comparisons
# Christian Hubbs
# 16.06.2018

import numpy as np 
from ada.scheduler.schedule_utils import *
from ada.environments.env_utils import get_current_state
from copy import copy

def build_heuristic_schedule(facility, schedule=None):
	#scheduler = heuristic_scheulder()
	schedule = build_schedule(facility, heuristic_scheduler, schedule)

	return schedule

def heuristic_scheduler(facility, schedule, *args, **kwargs):
    # Get current state
    # s = facility.get_current_state()[-facility.n_products:]
    s = get_current_state(facility, schedule=schedule, day=int(copy(facility.sim_time)))[-facility.n_products:]
    # Get minimum inventory entries
    mins = np.where(s==np.min(s))[0]
    # If multiple minimum values, sample from available actions
    if mins.size > 1:
        # Add one to match action
        action = np.random.choice(np.array(facility.action_list)[mins])
    else:
        # action = np.array(facility.action_list)[np.argmin(facility.get_current_state())]
        action = np.array(facility.action_list)[np.argmin(get_current_state(facility, schedule=schedule, day=int(copy(facility.sim_time))))]
        
    return int(action)