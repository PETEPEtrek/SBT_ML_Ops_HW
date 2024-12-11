FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir build


WORKDIR /app


COPY . .


RUN python3 -m build


RUN pip install dist/*.whl


CMD ["python3", "-m", "scripts/perf.py"]

