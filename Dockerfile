FROM python:3.9-slim

WORKDIR /app
COPY calc.py .
COPY test_calc.py .
CMD ["python3","calc.py"]
