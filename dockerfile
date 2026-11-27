# Base Python image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Start application
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]
