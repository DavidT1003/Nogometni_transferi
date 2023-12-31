FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install pony
EXPOSE 5000
CMD python ./app.py