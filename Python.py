from __future__ import (absolute_import, division, print_function)
import os
import json

import matplotlib as mpl
import matplotlib.pyplot as plt

from shapely.geometry import Point, Polygon, MultiPolygon
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import *
from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras

data_path = "./data"
