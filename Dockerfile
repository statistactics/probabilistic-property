ARG PYTHON_BASE=3.12-slim

# Build stage, referencing the PYTHON_BASE variable
FROM python:$PYTHON_BASE AS builder

# Initialize working directory within container
WORKDIR /project

# Install PDM
RUN pip install -U pdm

# Copy files into container for building
COPY ./pyproject.toml ./pdm.lock /project/ 

# Check the sequence of the installation step for layer caching
RUN pdm update
RUN pdm install --prod --no-editable



