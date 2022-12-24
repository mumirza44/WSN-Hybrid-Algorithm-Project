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

class WsnHybrid:
    """WSN Project Class"""

    def __init__(self,wsn_mode,threshold_temp,threshold_start_counter,threshold_stop_counter):
        
        self.wsn_mode = wsn_mode
        self.threshold_temp = threshold_temp
        self.threshold_start_counter = threshold_start_counter
        self.threshold_stop_counter = threshold_stop_counter
    


    def orchestrator(self,current_temp):
        """Orchestrator to manage which algorithm to choose. Event Driven or Time Driven"""
        
        print("Current Temperature:",current_temp)
        
        print("Reading Counter file")
        f = open("/home/mustafa/wsn/WSN-Hybrid-Algorithm-Project/counter.txt", "r")
        mode_counter = int((f.read()))

        print("Reading mode Counter from file",mode_counter)

        if self.wsn_mode == "event-driven":    
            print("Event Driven Mode")

            if current_temp >= self.threshold_temp:
                mode_counter = mode_counter + 1
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                print("Counter",mode_counter)
            else:
                mode_counter = 0
                self.update_counter(mode_counter) # Update the counter file by calling the update counter function
                print("Counter",mode_counter)
            
            if mode_counter >= self.threshold_start_counter:
                print("**************************************")
                print("Message: Switching Mode to Time Driven")
                print("**************************************")
                self.wsn_mode = "time-driven" # Call time driven function
            else:
                print("Message: Below Threshold mode still set to Event Driven")
                pass

        elif self.wsn_mode == "time-driven":
            print("Time Driven Mode")

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
            else:
                print("Message: Above Threshold, Mode still set to Time Driven")
                pass

        else:
            pass
            

        time.sleep(2)
        return mode_counter

    def update_counter(self,mode_counter):
        """Function to update the counter file"""

        f = open("/home/mustafa/wsn/WSN-Hybrid-Algorithm-Project/counter.txt", "w")
        f.write(str(mode_counter))
        f.close()

        return None

        

