ARG PYTHON_BASE=3.13.2

# Build stage, referencing the PYTHON_BASE variable
FROM python:$PYTHON_BASE AS BUILDER

# Install PDM
RUN pip install -U pdm

# Copy files into container for building