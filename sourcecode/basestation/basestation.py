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


from flask import make_response
from flask import Flask, render_template, request
import json

#Define FLASK APP
app = Flask(__name__)




@app.route("/basestation", methods = ['POST']) # URL: http://localhost:5070/basestation  [POST]
def basestation():
    """Basestation to receive response from nodes"""

    request_data = request.get_json() # Get the JSON response in the variable 
    print(json.dumps(request_data,indent=2))
    
    return request_data # Return the output


# Run the Flask app on the system IP Address and Port = 5070
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5070, debug=True)
