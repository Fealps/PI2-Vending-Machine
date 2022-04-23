FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /vendingmachine

WORKDIR /vendingmachine

COPY ./src /vendingmachine

COPY ./run_migrations.sh /run_migrations.sh

RUN chmod +x /run_migrations.sh

RUN pip install -r requirements.txt

EXPOSE 8000