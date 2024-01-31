FROM python:3.12

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r src/requirements.txt

CMD ["python", "src/main.py"]