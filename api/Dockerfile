FROM python:3.10-slim
WORKDIR /organizer
COPY ./requirements.txt /organizer/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /organizer/requirements.txt
COPY . /organizer
ENTRYPOINT ["python"]
CMD ["server.py"]
