FROM python:3.8.2-alpine3.11

WORKDIR /anton

#installing anton
COPY requirements.txt ./
RUN pip install --default-timeout=100 -r requirements.txt
RUN rm requirements.txt

COPY . .
CMD ["python", "anton.py"]