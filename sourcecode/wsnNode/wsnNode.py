#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 23-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""WSN Node file calls the methods from the wsnHybrid Library"""
# ---

import random
import json
from wsnHybrid import WsnHybrid
import requests
import os
import sys


# wsnHybrid Library variables
wsn_xmode = "event-driven" # Starting mode
mode_counter = 0           # Mode Counter Variable

# Environment Variables
threshold_xtemp = int(os.environ["threshold_temp"])            # Threshold Temperature
threshold_start = int(os.environ["threshold_start"])           # Starting Time driven mode Counter Threshold
threshold_stop = int(os.environ["threshold_stop"])             # Starting Time driven mode Counter Threshold
timedriven_interval = int(os.environ["timedriven_interval"])   # Time Driven Data Reporting interval
temp_range_start = int(os.environ["temp_start"])               # Temperature range start
temp_range_stop = int(os.environ["temp_stop"])                 # Temperature range stop

node_id = os.environ["node_id"]                                # ID of WSN Node

print("WSN NODE ID: ",node_id)

# Create wsn library object
wsn_lib = WsnHybrid(wsn_xmode,threshold_xtemp,threshold_start,threshold_stop,timedriven_interval,node_id)
wsn_mode = wsn_lib.orchestrator(30) # Call the orchestrator function in the wsn lib


while True:

        msg = random.randint(temp_range_start, temp_range_stop)
        
        print("Temp Received:",msg)
        
        wsn_mode = wsn_lib.orchestrator(msg)
        print("in wsn node file mode is:",wsn_mode)
