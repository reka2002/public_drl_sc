Article: [A deep reinforcement learning approach for chemical production scheduling](https://www.sciencedirect.com/science/article/pii/S0098135420301599#fn0002)

Original repo:  [A deep reinforcement learning approach for chemical production scheduling](https://www.sciencedirect.com/science/article/pii/S0098135420301599#fn0002)

# Run

### To run with default config dictionary:

python train.py --config default

python test.py --config default

### To run with specified config file:

python train.py --config="myfile.txt"

---

# Modifications from original repo
- Change the structure:
```
               /(root)
               |
-------------------------------
    |          |          |           
/config.py   /train.py   /ada    
                          |
          --------------------------------------------------------------------------------------
          |                |                |               |         |                |
     /Loggermixin.py     /logging.conf     /__init__.py    /agents    /environments   /scheduler
  
  ```

- Add venv and requirement.txt

## To run
- In `train.py` change `agent = set_up_sim(args)` to `agent = set_up_sim(args, config_dict = config)` to be able to run with config dictionary.
- Comment out `from .maintenance_models import * `
- Import `from ada.scheduler.heuristic_scheduler import *` in network scheduler
- To run SIMP_MPC:
    - Comment out `reduced_schedule = reduced_schedule[0,:]` in `tartan.py`
    - Add `transition_costs`
    - add k? 
- To run SMPC:
    - add K to order books?
- To run MPC RH (`deterministic_mip_rh.py`)
    - Add `transition_costs`
    - Add `MPCRH` to `create_agent()` in `op_agent.py`
- To run GOD (`god_mip.py`):
    - Add `transition_costs`
    - Add k?
- To run trained a2c:
    - create `test.py` to run trained network with the tartan environment
    - add `generate_schedule()` to the `a2c.py` code to generate schedule from trained network and add it to the `main()` function in `test.py`
    


###################################################################
# Not in original

## To plot results
Create `Results_plots` folder to store plot functions and schedule files.
- To plot MILP models:
    - create `save_schedule` to save the generated schedule and add it to the `train()` function in `mip_scheduler.py`
    - use the saved schedules in `plot gantt SIMP MPC.py`, `plot gantt main.py` and  `plot gantt forecast.py` 
- To plot a2c:
    - modify the `train()` function in `a2c.py` to store `epsiode_rewards`
    - create `log_epsiode_rewards()` function and use it in the `train()` function in `a2c.py` to save `epsiode_rewards` as a csv file
    - use the saved rewards in `plot training curve.py` 
    - create `save_schedule_RL` to save the generated schedule and add it to the `generate_schedule()` function in `a2c.py`
    - use the saved schedules in `plot gantt main.py` and  `plot gantt forecast.py` 



  

cd C:\Users\reka\Documents\GitHub\PUBLIC_DRL_SC