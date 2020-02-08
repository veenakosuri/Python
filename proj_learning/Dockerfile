FROM python:3.8

RUN mkdir /app
RUN mkdir /app/myFuncs
COPY . /app/myFuncs
WORKDIR /app/myFuncs

RUN pip install -r requirements.txt
RUN pip install pytest

CMD [ "python", "./main.py" ]