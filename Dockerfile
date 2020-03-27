FROM python:latest

WORKDIR /anton

#installing anton
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN rm requirements.txt

#copy anton
COPY . .
#run anton
CMD ["python", "anton.py"]