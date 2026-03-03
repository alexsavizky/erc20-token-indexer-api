# Stage 1: Build
FROM python:3.11-alpine as builder

WORKDIR /app

# Install system dependencies needed to COMPILE packages
# 'build-base' is Alpine's version of 'build-essential'
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    build-base

COPY requirements.txt .

# Install requirements to the user directory
RUN pip install --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final (The actual tiny image)
FROM python:3.11-alpine

WORKDIR /app

# Install ONLY the runtime library for Postgres (libpq) 
# This is needed for the app to talk to the DB at runtime
RUN apk add --no-cache libpq

# Copy the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure the app can find the installed packages
ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]