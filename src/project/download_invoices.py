import aiohttp
import asyncio
import os
from src import config
from typing import List, Dict
import logging as logger

async def download_single_invoice(session: aiohttp.ClientSession, invoice_data: dict) -> str:
        """
        Realiza o download de uma única fatura e salva em disco.
        """
        try:
            url_path = config.URL_SITE.rstrip('/') + invoice_data["invoice"]
            file_name = os.path.basename(invoice_data["invoice"])
            file_path = config.OUTPUT_INVOICES / file_name

            async with session.get(url_path, timeout=30) as response:
                if response.status != 200:
                    raise Exception(f"Status {response.status}")
                content = await response.read()

            with open(file_path, "wb") as f:
                f.write(content)
            logger.info(f"Fatura salva: {file_name}")
            return file_name
        except Exception as e:
            logger.error(f"Falha ao baixar {invoice_data.get('invoice', 'desconhecido')}: {e}")
            return None


async def download_invoices_parallel(data: List[Dict]):
    """
    Faz download de todas as faturas em paralelo.
    """
    config.OUTPUT_INVOICES.mkdir(parents=True, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = [download_single_invoice(session, invoice) for invoice in data]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        logger.info(f"Downloads concluídos. Total: {len([r for r in results if r])} faturas baixadas com sucesso.")