from python:3.10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

# Install dig
RUN apt-get update && apt-get install -yq dnsutils telnet && apt-get clean && rm -rf /var/lib/apt/lists

WORKDIR /src
COPY . /src

CMD ["python", "main.py"]