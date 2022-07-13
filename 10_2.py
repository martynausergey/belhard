from pydantic import BaseModel

class order_item(BaseModel):
    id: int
    order_id: int
    product_id: int
    total: int
class products(order_item):
    id: int
    category_id: int
    price: int
    media: str
    total: int
    is_published: bool
    name_en: str
    name: str
class categories(products):
    id: int
    parent_id: int
    is_published: bool
    name_en: str
    name: str
class orders():
    id: int
    bot_user_id: int
    date_create:
    status_id: int
    invoice_id: int
class bot_users(languages, invoices):
    id: int
    is_blocked: bool
    balance: int
    language_id: int
class languages():
    id: int
    language_code: int
class invoices():
    id: int
    bot_user_id: int
    date_create: int
    total: int
    status_id: int
