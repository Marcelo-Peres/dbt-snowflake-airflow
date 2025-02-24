FROM python:3.12-slim

WORKDIR /app
# Install system dependencies (git, other essentials)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
# Copia o diretório do código e o requirements.txt
COPY dbt/ /app/
COPY requirements.txt /app/
# Instala as dependências a partir do requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["bash"]
