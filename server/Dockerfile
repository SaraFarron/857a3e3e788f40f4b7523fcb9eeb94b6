FROM python:3.9.5

WORKDIR /usr/src/server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY requirements.txt /usr/src/server/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/server/

ENTRYPOINT ["/usr/src/server/entrypoint.sh"]
