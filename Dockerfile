FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt
COPY main.py .

CMD [ "python3", "main.py" ]