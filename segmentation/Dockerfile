FROM python:3

WORKDIR /etc/segmentation

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install git+https://www.github.com/keras-team/keras-contrib.git

EXPOSE 5000