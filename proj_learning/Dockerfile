FROM python:3.8

RUN mkdir /app
COPY . /app/myFuncs
WORKDIR /app/myFuncs

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]