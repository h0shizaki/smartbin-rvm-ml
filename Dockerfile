FROM python:3.11.9

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0" ]