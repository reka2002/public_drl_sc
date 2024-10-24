# Run

### To run with default config dictionary:

python train.py --config default

### To run with specified config file:

python train.py --config="myfile.txt"

# Modifications from originial repo:
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

- In `train.py` change `` to `` to be able to run with config dictionary.
- Comment out `import `
