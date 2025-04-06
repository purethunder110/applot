FROM ubuntu:latest

# install staging changes

RUN apt-get update && apt-get install -y \
    git \
    redis \
    python3.12 \
    python-pip


#main django deployement
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]