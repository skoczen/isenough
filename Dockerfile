# FROM python:3.10.9-slim
FROM python:2.7-slim
MAINTAINER Steven Skoczen <skoczen@gmail.com>

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran


# Set up reqs
ADD requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 8000

# Run the bot.py script
WORKDIR project
CMD ["python", "manage.py", ""]
