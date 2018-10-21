FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install -r requestment && apt-get clean all

EXPOSE 8889

CMD ["python","saturday.py"]