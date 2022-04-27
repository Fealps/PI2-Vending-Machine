FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /vendingmachine

COPY ./ /vendingmachine

COPY ./run_migrations.sh /run_migrations.sh

RUN chmod +x /run_migrations.sh

WORKDIR /vendingmachine/src/

RUN pip install -r requirements.txt

EXPOSE 8000