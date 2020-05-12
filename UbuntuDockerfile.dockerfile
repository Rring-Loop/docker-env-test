FROM ubuntu:16.04
MAINTAINER fnndsc "dev@babymri.org"

RUN mkdir /app
ADD . /app/

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python

RUN pip3 install -i https://pypi.doubanio.com/simple/ --no-cache-dir -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python3", "/app/test_load_dotenv.py"]