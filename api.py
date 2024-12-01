import json
from typing import List, Optional
from urllib.parse import urljoin

from aiohttp import ClientSession, ClientResponseError

from models import (
    PaymentsResponse,
    PaymentResponse,
    ProductsResponse,
    ProductResponse,
    Payment,
    Product
)


class EasyDonateAPI:
    def __init__(self, token: str) -> None:
        self._base_url = 'https://easydonate.ru/api/v3/'
        self._headers = {
            "Shop-Key": token
        }

    async def _request(self, method: str, endpoint: str, params: dict = None, data: dict = None) -> Optional[dict]:
        """
        Вспомогательный метод для запросов к API
        """
        url = urljoin(self._base_url, endpoint)
        async with ClientSession() as session:
            try:
                async with session.request(method, url, headers=self._headers, params=params, json=data) as response:
                    response.raise_for_status()
                    return await response.json()
            except ClientResponseError as e:
                print(f"HTTP error occurred: {e.status} - {e.message}")
            except Exception as e:
                print(f"An error occurred: {e}")
            return None

    async def create_payment(self, customer: str, server_id: int, products: list, email: str = None, coupon: str = None,
                             success_url: str = None) -> Optional[str]:
        """
        Создание платежа
        """
        endpoint = "shop/payment/create"
        data = {
            "customer": customer,
            "server_id": server_id,
            "products": json.dumps(products),
            "email": email,
            "coupon": coupon,
            "success_url": success_url,
        }
        response = await self._request("POST", endpoint, data=data)
        if response and response.get("success"):
            return response["response"]["url"]
        else:
            print(f"Error while creating payment: {response.get('message')}")
            return None

    async def get_payments(self) -> List[Payment]:
        """
        Получение списка платежей
        """
        endpoint = "shop/payments"
        response = await self._request("GET", endpoint)
        if response and response.get("success"):
            return PaymentsResponse(**response).response
        else:
            print(f"Error fetching payments: {response.get('message')}")
            return []

    async def get_payment_details(self, payment_id: str) -> Optional[Payment]:
        """
        Получение информации о платеже
        """
        endpoint = f"shop/payment/{payment_id}"
        response = await self._request("GET", endpoint)
        if response and response.get("success"):
            return PaymentResponse(**response).response
        else:
            print(f"Error fetching payment details: {response.get('message')}")
            return None

    async def get_products(self) -> List[Product]:
        """
        Получение списка товаров
        """
        endpoint = "shop/products"
        response = await self._request("GET", endpoint)
        if response and response.get("success"):
            return ProductsResponse(**response).response
        else:
            print(f"Error fetching products: {response.get('message')}")
            return []

    async def get_product_details(self, product_id: str) -> Optional[Product]:
        """
        Получение информации о товаре
        """
        endpoint = f"shop/product/{product_id}"
        response = await self._request("GET", endpoint)
        if response and response.get("success"):
            return ProductResponse(**response).response
        else:
            print(f"Error fetching product details: {response.get('message')}")
            return None
