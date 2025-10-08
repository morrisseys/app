FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Fetch AdminLTE assets into /app/static/adminlte
RUN apt-get update && apt-get install -y wget unzip &&     wget -qO /tmp/adminlte.zip https://github.com/colorlibhq/AdminLTE/archive/refs/heads/master.zip &&     unzip -q /tmp/adminlte.zip -d /tmp &&     mv /tmp/AdminLTE-master /app/static/adminlte &&     rm -rf /tmp/adminlte.zip /tmp/AdminLTE-master &&     apt-get purge -y wget unzip && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
COPY . .
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
