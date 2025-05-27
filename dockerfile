FROM python:3.11-slim

# Install dependencies
WORKDIR /MY-APP

COPY requirements.txt requirements.txt
# Install system dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8000
EXPOSE 8501
# Run the application
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run ui.py --server.port 8501 --server.address 0.0.0.0"]

