FROM python:3.7
RUN mkdir /app
ADD . /app/

WORKDIR /app
ENTRYPOINT ["python", "test_env.py"]