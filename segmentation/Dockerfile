FROM python:3

WORKDIR /etc/segmentation

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "./segmentation_api.py" ]