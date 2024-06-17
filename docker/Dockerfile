FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Define environment variable
ENV NAME Conduit

# Run main.py when the container launches
CMD ["python", "main.py"]
