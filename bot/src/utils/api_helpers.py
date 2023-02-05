
"""
Provides helper functions for interacting with the Telema Web Service API,
allowing for easier and more convenient access to the API.
It provides functions for making GET, POST, PUT, PATCH, DELETE requests to the API
and returning the responses in a convenient json format.
"""

import aiohttp
from typing import Optional


async def _make_request(
    url: str,
    method: str,
    data: Optional[dict[str, str]] = None,
    chat_id: Optional[str] = None
):
    """
    Makes a request to the Telegram API.
    :param url: The bot's API token. (Created with @BotFather)
    :param method: HTTP method to be used. Defaults to 'get'.
    :param data: payload data for request.
    :return: The result parsed to a JSON dictionary.
    """
    if chat_id:
        headers = {'chat_id': chat_id}

    async with aiohttp.ClientSession(headers=headers) as session:
        if method == 'GET':
            async with session.get(url) as resp:
                return await resp.json(), resp.status
        elif method == 'POST':
            async with session.post(url, data=data) as resp:
                return await resp.json(), resp.status
        elif method == 'PUT':
            async with session.put(url, data=data) as resp:
                return await resp.json(), resp.status
        elif method == 'PATCH':
            async with session.patch(url, data=data) as resp:
                return await resp.json(), resp.status
        elif method == 'DELETE':
            async with session.delete(url) as resp:
                return await resp.json(), resp.status
        else:
            raise ValueError(
                f"Invalid method: {method}. Only 'GET', 'POST', 'PUT', 'PATCH' or 'DELETE' are allowed.")


async def get_user_status(chat_id: str):
    url = 'http://localhost:8000/users/me/status'
    response, status = await _make_request(url=url, method='GET', chat_id=chat_id)
    return response['is_active']
