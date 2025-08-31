import aiohttp
from datetime import datetime
from src import config
from typing import List, Dict
import logging as logger
from datetime import datetime

async def extract_data() -> List[Dict]:
        """
        Faz POST na API /seed e retorna a lista de faturas já com datas convertidas.
        """
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest"
        }
        url = config.URL_SITE.rstrip("/") + "/seed"
        print("Requisitando:", url)

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, data={}) as resp:
                resp.raise_for_status()
                response_json = await resp.json()
                data = response_json["data"]

        for item in data:
            item['duedate_dt'] = datetime.strptime(item['duedate'], config.DATE_FORMAT).date()
        
        filtered_data = [i for i in data if i['duedate_dt'] <= datetime.now().date()]
        logger.info(f"Total de faturas para download encontradas com vencimento até hoje: {len(filtered_data)}")
        return filtered_data