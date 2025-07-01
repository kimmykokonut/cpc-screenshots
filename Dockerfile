# Dockerfile, Image, Container

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:latest

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install requirements and dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt && \
  playwright install-deps && \
  playwright install

# Set the working directory
WORKDIR /src

# Copy necessary files
COPY ./src /src/

# Ensure the screenshots directory exists
RUN mkdir -p /screenshots

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
