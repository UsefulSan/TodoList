FROM python

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

WORKDIR /django

COPY . .

RUN pip install -r requirements.txt