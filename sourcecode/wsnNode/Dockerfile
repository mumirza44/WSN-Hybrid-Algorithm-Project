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

RUN pip install flask
RUN pip install requests

COPY . .

CMD [ "python","-u","./wsnNode.py" ]