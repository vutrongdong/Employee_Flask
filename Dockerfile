FROM python:3.7.1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install flask-bootstrap
CMD ["python", "app.py"]

