FROM python:3.7

RUN mkdir /CsvService
WORKDIR /CsvService
ADD . /CsvService/
RUN pip install -r requirements.txt

EXPOSE 8001
CMD ["python", "/CsvService/app.py"]
