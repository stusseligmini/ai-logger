
# Bruk slank Python image
FROM python:3.12-slim

# Sett arbeidsmappe
WORKDIR /app

# Installer avhengigheter
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopier hele prosjektet
COPY . .

# Sørg for at .env er tilgjengelig
ENV PYTHONUNBUFFERED=1

# Start applikasjonen
CMD ["python", "main.py"]
