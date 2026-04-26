import os
import pickle
from typing import Optional, Tuple, List, Dict, Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

TMDB_BASE = "https://api.themoviedb.org/3"
TMDB_IMG_500 = "https://api.themoviedb.org/t/p/500"

if not TMDB_API_KEY:
    raise RuntimeError("TMDB Api key is missing. Put it in .env as TMDB_API_KEY=xxx")

