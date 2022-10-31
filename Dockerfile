FROM python:3.8
RUN apt-get clean -y && apt-get update -y
RUN apt-get install bash
RUN pip install --upgrade pip 
EXPOSE 5000
COPY . /app
RUN pip install -r /app/requirements.txt
RUN pip install -e /app/src
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

