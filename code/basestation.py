#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 23-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""Basestation data collection api Server"""
# ---


#Define FLASK APP
app = Flask(__name__)




@app.route("/basestation", methods = ['POST']) # URL: http://localhost:500/output  [POST]
def basestation():

    request_data = request.get_json() # Get the JSON response in the variable 
    clusterHost= request_data["clusterHost"] # Extract the ClusterHost(Cluster IP) from request_data in a variable.
    lockerNum= request_data["lockerID"]      # Extract the lockerNum from request_data in a variable.
    
    obj = IOBoard(clusterHost,lockerNum) # Create Object IOBoard class
    x = obj.output() # Call the output
    
    del obj # Delete Object

    return x # Return the output


# Run the Flask app on the system IP Address and Port = 500
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=500, debug=True)
