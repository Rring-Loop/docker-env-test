FROM python:3.7
RUN mkdir /app
ADD . /app/

RUN pip install -i https://pypi.doubanio.com/simple/ --no-cache-dir -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python", "/app/test_load_dotenv.py"]