FROM python:3.7

RUN mkdir /TwitterService
WORKDIR /TwitterService
ADD . /TwitterService/
RUN pip install -r requirements.txt

CMD ["python", "/TwitterService/app.py"]
