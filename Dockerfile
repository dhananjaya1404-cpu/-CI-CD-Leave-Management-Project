# ── Stage 1: Build ────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Stage 2: Run ──────────────────────────────────
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages cleanly
COPY --from=builder /install /usr/local

# Copy app source
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

CMD ["python", "app.py"]