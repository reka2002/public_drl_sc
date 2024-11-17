import sys
from config import *
from ada.agents.rl_algos.a2c import a2c
from ada.environments.tartan import productionFacility

def main(argv):
    args = parse_cl_args(argv)

    # original:
    #agent = set_up_sim(args)

    # use default:
    agent = set_up_sim(args, config_dict = config)

    # use default path
    # default_path = "C:\Users\Reka\Documents\GitHub\public_drl_sc\config.txt"  
    #agent = set_up_sim(args, default_path=default_path)
    # TODO: Train agent and log results

    agent.generate_schedule()

if __name__ == "__main__":
	main(sys.argv)