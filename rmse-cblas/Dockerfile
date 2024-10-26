FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    cmake \
    libgtest-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir build numpy pybind11


WORKDIR /app


COPY . .

RUN bash setup.sh && \
    make rmse_cblas && \
    make linalg


RUN python3 -m build


RUN pip install dist/*.whl


CMD ["python3", "scripts/perf.py"]

