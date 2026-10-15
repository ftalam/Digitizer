import os
import asyncpg
import rasterio
import shapely
import geopandas 
from fastapi import FastAPI

app = FastAPI(title="Geospatial Digitizer API")
pool : asyncpg.Pool | None = None

@app.on_event("startup")
async def startup():
    global pool
    pool = await asyncpg.create_pool(os.environ["DATABASE_URL"])


@app.on_event("shutdown")
async def shutdown():
    await pool.close()

@app.get("/health")
async def health_check(): 
    postgis = await pool.fetchval("SELECT PostGIS_Version()")
    return {
        "postgis": postgis,
        "rasterio": rasterio.__version__,
        "rasterio_gdal": rasterio.__gdal_version__,
        "shapely": shapely.__version__,
        "geos": shapely.geos_version_string,
        "geopandas": geopandas.__version__,
    }
