FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /segmentation-api
ADD ./requirements.txt /segmentation-api/requirements.txt
RUN pip install -r requirements.txt

COPY . /segmentation-api

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["run-keras-server.py"]