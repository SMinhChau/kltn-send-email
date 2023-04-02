FROM python:3.10.6

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt
COPY . .

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5005", "main:app" ]