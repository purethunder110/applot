FROM ubuntu:latest

# install staging changes

RUN apt-get update && apt-get install -y \
    git \
    redis \
    python3 \
    python3-pip \
    python3.12-venv


#main django file directory
WORKDIR /app

# creating a virtual env. PEP 668 prevents to install pip inside docker
RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# installing packages
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]