FROM python:3.10

ENV PYTHONUNBUFFERED=1



COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
