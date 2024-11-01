# Run

### To run with default config dictionary:

python train.py --config default

### To run with specified config file:

python train.py --config="myfile.txt"

---

# Modifications from originial repo
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

- In `train.py` change `agent = set_up_sim(args)` to `agent = set_up_sim(args, config_dict = config)` to be able to run with config dictionary.
- Comment out `from .maintenance_models import * `
- Import `from ada.scheduler.heuristic_scheduler import *` in network scheudler
