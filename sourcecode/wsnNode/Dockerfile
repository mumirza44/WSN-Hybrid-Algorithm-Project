# Dockerfile
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 21-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
#"""Dockerfile - Create WSN node docker image """
# ---

FROM python:3.7.16-slim-bullseye

#WORKDIR /../../sourcecode

RUN pip install paho-mqtt

COPY . .

CMD [ "python","-u","./temperatureSimulator.py" ]