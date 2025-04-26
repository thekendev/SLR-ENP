# Use official Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirement and install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your app files
COPY . .

# Only expose Streamlit port (now 7860 for Hugging Face)
EXPOSE 7860

# Run Streamlit directly
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]