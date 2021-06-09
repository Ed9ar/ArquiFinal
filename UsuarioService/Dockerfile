FROM python:3.7

RUN mkdir /UsuarioService
WORKDIR /UsuarioService
ADD . /UsuarioService/
RUN pip install -r requirements.txt

CMD ["python", "/UsuarioService/app.py"]