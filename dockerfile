FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose no ports (since it's a Telegram bot)

# Command to run the bot
CMD ["python", "main.py"]
