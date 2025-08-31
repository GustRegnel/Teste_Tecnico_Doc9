from src.project.download_invoices import download_invoices_parallel
from src.project.fetch_invoice_data import extract_data
from src.project.write_csv import create_csv
import time
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def main() -> None:
    start_time = time.time()
    logging.info("Iniciando o processo de extração e download de faturas...")
    data = await extract_data()
    await download_invoices_parallel(data)
    create_csv(data)
    end_time = time.time()
    logging.info(f"Processo concluído em {end_time - start_time:.2f} segundos.")

if __name__ == "__main__":
    asyncio.run(main())