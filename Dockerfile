FROM python:3.9.5



WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD ["python", "run.py"]
