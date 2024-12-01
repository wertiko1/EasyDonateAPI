from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl, EmailStr


class Server(BaseModel):
    id: int
    name: str
    ip: str
    port: str
    version: Optional[str]
    is_port_hidden: int
    hide_ip: int
    is_hidden: int
    shop_id: int
    created_at: datetime
    updated_at: datetime


class Product(BaseModel):
    id: int
    name: str
    price: float
    old_price: Optional[float]
    type: str
    number: int
    commands: List[str]
    withdraw_commands: Optional[List[str]]
    withdraw_commands_days: Optional[int]
    additional_fields: Optional[dict]
    description: Optional[str]
    image: HttpUrl
    first_delete: int
    shop_id: int
    created_at: datetime
    updated_at: datetime
    servers: List[Server]


class PaymentCommand(BaseModel):
    command: str
    response: str


class PaymentProduct(BaseModel):
    id: int
    name: str
    price: float
    old_price: Optional[float]
    type: str
    number: int
    commands: List[str]
    withdraw_commands: Optional[List[str]]
    withdraw_commands_days: Optional[int]
    additional_fields: Optional[dict]
    description: Optional[str]
    image: HttpUrl
    first_delete: int
    shop_id: int
    created_at: datetime
    updated_at: datetime
    sort_index: int


class Payment(BaseModel):
    id: int
    customer: str
    email: Optional[EmailStr]
    shop_id: int
    server_id: int
    status: int
    enrolled: float
    payment_system: str
    payment_type: str
    sent_commands: List[PaymentCommand]
    error: Optional[str]
    created_at: datetime
    updated_at: datetime
    products: List[PaymentProduct]
    server: Server


class BaseResponse(BaseModel):
    success: bool


class PaymentsResponse(BaseResponse):
    response: List[Payment]


class PaymentResponse(BaseResponse):
    response: Payment


class ProductsResponse(BaseResponse):
    response: List[Product]


class ProductResponse(BaseResponse):
    response: Product
