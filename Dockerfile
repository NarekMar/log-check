FROM python:3.12-slim
WORKDIR /app
COPY log_check.py sample.log ./
ENTRYPOINT ["python3", "log_check.py"]
CMD ["sample.log"]
