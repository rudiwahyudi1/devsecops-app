# Base image (ringan & aman)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Security: non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Copy dependency file dulu (biar cache efisien)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Ubah ownership
RUN chown -R appuser:appgroup /app

# Pakai non-root user
USER appuser

# Expose port FastAPI
EXPOSE 8000

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
