import os
from datetime import datetime
from pathlib import Path

URL_SITE = os.getenv("URL_SITE", "https://rpachallengeocr.azurewebsites.net")
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_CSV = BASE_DIR / "output" / "Results"
OUTPUT_INVOICES = BASE_DIR / "output" / "Invoices"
DATE_FORMAT = "%d-%m-%Y"
