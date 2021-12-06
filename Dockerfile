FROM python:alpine3.7
ADD square.py /square.py
RUN pip install Flask
ENTRYPOINT ["python3", "square.py"]
