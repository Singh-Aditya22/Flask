FROM python:3.9.13-slim-buster

WORKDIR /Users/adity/Desktop/Flask/docker

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]