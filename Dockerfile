FROM python:3.8.6-buster

COPY frontend /frontend 
COPY markdown_predictions /markdown_predictions
COPY requirements.txt /requirements.txt
COPY markdown_model.joblib /markdown_model.joblib

RUN mkdir $USER/.streamlit
RUN apt-get update 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run frontend/sales_predictor.py  --server.port 8080