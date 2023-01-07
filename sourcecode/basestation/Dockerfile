# Dockerfile
#----------------------------------------------------------------------------
# Company: WSN Research
# Created By  : Mohammed Mustafa Mirza
# Created Date: 21-Dec-2022
# version ='0.1'
# ---------------------------------------------------------------------------
#"""Dockerfile - Create WSN Temperature Simulator docker image """
# ---

FROM python:3.7.16-slim-bullseye

#WORKDIR /../../sourcecode
#RUN mkdir app
RUN pip install flask
#WORKDIR /app
COPY . .

CMD [ "python","-u","./basestation.py" ]