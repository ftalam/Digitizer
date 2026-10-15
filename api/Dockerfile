FROM python:3.12-slim-bookworm

# GDAL command-line tools (gdalinfo, gdalwarp, gdal_translate)
RUN apt-get update && apt-get install -y --no-install-recommends gdal-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app