#!/usr/bin/env python3

import sys 
import os
from argparse import ArgumentParser, ArgumentTypeError
import numpy as np

from config import *

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

	#agent.optimize_hyperparameters()
	agent.train()

if __name__ == "__main__":
	main(sys.argv)