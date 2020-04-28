FROM python:3

WORKDIR /etc/segmentation

COPY mock-requirements.txt ./
RUN pip install --no-cache-dir -r mock-requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "./mock-segmentation-api.py" ]