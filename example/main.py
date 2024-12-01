import asyncio

from api import EasyDonateAPI

EASYDONATE_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXX"  # Замените на ваш реальный токен
api_client = EasyDonateAPI(EASYDONATE_TOKEN)


async def create_payment_example():
    """
    Пример создания платежа
    """
    payment_url = await api_client.create_payment(
        customer="Player123",
        server_id=1,
        products=[{"id": 101, "quantity": 1}],
        email="player123@example.com",
        coupon="COUPON123",
        success_url="https://example.com/success"
    )
    if payment_url:
        print(f"Платеж успешно создан. URL для оплаты: {payment_url}")
    else:
        print("Не удалось создать платеж.")


async def get_payments_example():
    """
    Пример получения списка платежей
    """
    payments = await api_client.get_payments()
    if payments:
        print(f"Найдено {len(payments)} платежей:")
        for payment in payments:
            print(f"- ID: {payment.id}, Сумма: {payment.amount}, Статус: {payment.status}")
    else:
        print("Не удалось получить список платежей.")


async def get_payment_details_example(payment_id: str):
    """
    Пример получения информации о платеже
    """
    payment_details = await api_client.get_payment_details(payment_id)
    if payment_details:
        print(f"Детали платежа:\n{payment_details}")
    else:
        print("Не удалось получить информацию о платеже.")


async def get_products_example():
    """
    Пример получения списка товаров
    """
    products = await api_client.get_products()
    if products:
        print(f"Найдено {len(products)} товаров:")
        for product in products:
            print(f"- ID: {product.id}, Название: {product.name}, Цена: {product.price}")
    else:
        print("Не удалось получить список товаров.")


async def get_product_details_example(product_id: str):
    """
    Пример получения информации о товаре
    """
    product_details = await api_client.get_product_details(product_id)
    if product_details:
        print(f"Детали товара:\n{product_details}")
    else:
        print("Не удалось получить информацию о товаре.")


async def main():
    await create_payment_example()

    await get_payments_example()

    await get_products_example()


# Usage
if __name__ == "__main__":
    asyncio.run(main())
