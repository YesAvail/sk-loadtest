FROM python:slim-bullseye
COPY /requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
COPY /. .
EXPOSE 8089
CMD ["locust", "-f", "locustfiles/api.py", "--master"]
