#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 21-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""Orchestrator.py - Orchestrator to manage which algorithm to choose. Event Driven or Time Driven """
# ---

import time
import requests
from datetime import datetime

class WsnHybrid:
    """WSN Project Class"""

    def __init__(self,wsn_mode,threshold_temp,threshold_start_counter,threshold_stop_counter,timedriven_interval):
        
        self.wsn_mode = wsn_mode
        self.threshold_temp = threshold_temp
        self.threshold_start_counter = threshold_start_counter
        self.threshold_stop_counter = threshold_stop_counter
        self.timedriven_interval = timedriven_interval
    


    def orchestrator(self,current_temp):
        """Orchestrator to manage which algorithm to choose. Event Driven or Time Driven"""
        
        print("Current Temperature:",current_temp)
        
        print("Reading Counter file")
        f = open("counter.txt", "r")
        mode_counter = int((f.read()))

        print("Reading mode Counter from file",mode_counter)

        if self.wsn_mode == "event-driven":
            print("Event Driven Mode")
            
            if current_temp >= self.threshold_temp:
                mode_counter = mode_counter + 1
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                print("Counter",mode_counter)
                self.data_reporting(current_temp,"Event Reporting: Temperature Above 50") # Start Reporting Event data by calling the data_reporting function
                
            else:
                mode_counter = 0
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                print("Counter",mode_counter)
            
            if mode_counter >= self.threshold_start_counter:
                print("**************************************")
                print("Message: Switching Mode to Time Driven")
                print("**************************************")
                self.wsn_mode = "time-driven" # Call time driven function
                return self.wsn_mode
            else:
                print("Message: Below Threshold mode still set to Event Driven")
                pass

        elif self.wsn_mode == "time-driven":
            print("Time Driven Mode")
            
            self.data_reporting(current_temp,"Time Driven Reporting: Every "+str(self.timedriven_interval)+" Seconds") # Start Reporting data every x seconds calling the data_reporting function
            
            time.sleep(self.timedriven_interval)
    
            if current_temp < self.threshold_temp:
                mode_counter = mode_counter + 1
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                
            else:
                mode_counter = 0
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                print("Counter",mode_counter)

            if mode_counter >= self.threshold_stop_counter:
                print("***************************************")
                print("Message: Switching Mode to Event Driven")
                print("***************************************")
                self.wsn_mode = "event-driven" # Call event driven function
                return self.wsn_mode
            else:
                print("Message: Above Threshold, Mode still set to Time Driven")
                pass

        else:
            pass
            

        time.sleep(2)
        return mode_counter

    def update_counter(self,mode_counter):
        """Function to update the counter file"""

        f = open("counter.txt", "w")
        f.write(str(mode_counter))
        f.close()

        return None

    def update_sleep_counter(self,sleep_counter):
        """Function to update the sleep counter file"""
        f = open("counter.txt", "w")
        f.write(str(sleep_counter))
        f.close()

        return None

        f = open("counter.txt", "w")
        f.write(str(sleep_counter))
        f.close()

        return None

    def data_reporting(self,tempdata,description):
        """Send event data over HTTP Post to the Basestation REST API server"""
        
        date_time = str(datetime.now()) # Create Timestamp
        data = {
            "temperature" : tempdata,
            "timestamp": date_time,      
            "mode": self.wsn_mode,
            "description": description
             }

        print(data)

        requests.post("http://0.0.0.0:5070/basestation",json=data)

        

