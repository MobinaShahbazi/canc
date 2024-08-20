FROM --platform=linux/amd64 pdr.hexatech.ir/python:3.10-slim

WORKDIR /matching-service

COPY ./requirements.txt /matching-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /matching-service/requirements.txt

COPY ./app /matching-service/app
COPY ./alembic /matching-service/alembic

COPY ./alembic.ini /matching-service/alembic.ini

# for alembic
#CMD ["bash", "-c", "alembic upgrade head"]
#RUN alembic revision --autogenerate -m "migrate database"
#CMD ["bash", "-c", "alembic upgrade head"]

EXPOSE 42421

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "42421"]
