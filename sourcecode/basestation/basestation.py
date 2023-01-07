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

import json
from flask import make_response
from flask import Flask, render_template, request

#Define FLASK APP
app = Flask(__name__)


open('/output/basestation_output.json', 'w').close() # RESET Output file
    


@app.route("/basestation", methods = ['POST']) # URL: http://localhost:5070/basestation  [POST]
def basestation():
    """Basestation to receive response from nodes"""

    request_data = request.get_json() # Get the JSON response in the variable 
    print(json.dumps(request_data,indent=2))
    
    with open("/output/basestation_output.json", "a") as basestation_output:
        json.dump(request_data, basestation_output, indent=3)
        basestation_output.write('\n\n')

    return request_data # Return the output


# Run the Flask app on the system IP Address and Port = 5070
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5070, debug=True)
