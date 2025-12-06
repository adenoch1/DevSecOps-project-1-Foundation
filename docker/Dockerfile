# =========================================================
# STAGE 1 — Build Dependencies
# =========================================================
FROM python:3.11-alpine AS builder
RUN pip install --upgrade pip

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade Alpine packages to get BusyBox security fixes (r20)
RUN apk update && apk upgrade && apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers

COPY app/requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


# =========================================================
# STAGE 2 — Runtime Image
# =========================================================
FROM python:3.11-alpine AS runtime
RUN pip install --upgrade pip

WORKDIR /app

# Patch Alpine to latest CVE fixes (BusyBox r20)
RUN apk update && apk upgrade

# Add non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Copy virtual env
COPY --from=builder /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY --chown=appuser:appgroup app /app

# Configurable App Env Vars
ENV APP_HOST=0.0.0.0
ENV APP_PORT=5000

# Expose port
EXPOSE 5000

# Use Gunicorn in production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "3", "--threads", "2"]
