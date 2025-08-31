import os
import csv
from src import config
from typing import List, Dict
import logging as logger
from datetime import datetime

def create_csv(data: List[Dict]) -> None:
    """
    Cria um arquivo CSV com os dados extraidos do site do desafio.
    """
    config.OUTPUT_INVOICES.mkdir(parents=True, exist_ok=True)
    file_name = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".csv"
    column_names = [key for key in data[0].keys() if key != 'duedate_dt']
    with open(os.path.join(config.OUTPUT_CSV, file_name), "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        for item in data:
            item_copy = item.copy()
            del item_copy['duedate_dt']
            writer.writerow(item_copy)
    logger.info(f"CSV criado: {file_name}")