FROM python:3.7

RUN mkdir /CsvService
WORKDIR /CsvService
ADD . /CsvService/
RUN pip install -r requirements.txt

CMD ["python", "/CsvService/app.py"]
