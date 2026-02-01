# Things Learnt till now 
## 2.1 Routers & Custom Routers

### Why It Matters
Routers organize endpoints into logical groups. The codebase uses a custom router for trailing slash handling.

### Basic Router
```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/purchase-orders",
    tags=["Purchase Orders"]
)

@router.get("/")
async def list_purchase_orders():
    return {"orders": []}

@router.get("/{po_id}")
async def get_purchase_order(po_id: str):
    return {"po_id": po_id}
```

### Custom Router (From Codebase)
**File**: `backend/server_class.py`
```python
from fastapi import APIRouter
from typing import Any, Callable

class CustomRouter(APIRouter):
    """
    Custom Router that handles trailing slashes.
    /api/orders and /api/orders/ both work.
    """

    def api_route(
        self,
        path: str,
        *,
        include_in_schema: bool = True,
        **kwargs: Any
    ) -> Callable:
        # Remove trailing slash from path
        if path.endswith("/"):
            path = path[:-1]

        # Register main route
        add_path = super().api_route(
            path,
            include_in_schema=include_in_schema,
            **kwargs
        )

        # Register alternate route with trailing slash (hidden from docs)
        alternate_path = path + "/"
        add_alternate_path = super().api_route(
            alternate_path,
            include_in_schema=False,
            **kwargs
        )

        def decorator(func):
            add_alternate_path(func)  # Register /path/
            return add_path(func)     # Register /path

        return decorator

def append_router_prefix(router, prefix):
    """Utility to add prefix to existing router"""
    custom_router = CustomRouter(prefix=prefix)
    custom_router.include_router(router)
    return custom_router
```

### Registering Routers
**File**: `backend/inventory_server.py`
```python
from fastapi import FastAPI
from server_class import Server

# Define routers with optional prefixes
inventory_routers = [
    {"router": po_router},                                    # /api/v1/...
    {"router": dashboard_router},                             # /api/v1/...
    {"router": optimization_router, "prefix": "/api/v3"}     # /api/v3/...
]

# Server class handles registration
inventory_server = Server(inventory_routers)
app = inventory_server.get_app()
```

---

## 2.2 Class-Based Views (CBV)

### Why It Matters
All controllers in the codebase use CBV pattern for organizing related endpoints.

### Basic CBV Pattern
**File**: `backend/inventory_smart/controller/po.py`
```python
from fastapi import APIRouter, Request, Header
from fastapi_class import cbv

router = APIRouter(prefix="/purchase-order", tags=["Purchase Order"])

@cbv(router)  # Decorator that enables class-based views
class PurchaseOrder:
    """
    All purchase order related endpoints.
    Methods become route handlers.
    """

    def __init__(self):
        # Called once when class is instantiated
        self.service = PurchaseOrderService()

    @router.get("/place-holder/{po_id}/article/{article}/details")
    @tenant_context_decorator
    async def get_placeholder_article_details(
        self,
        po_id: str,
        article: str,
        request: Request,
        retail_region: Optional[str] = Query(None),
        authorization: str = Header(...)
    ):
        table_config, data = await self.service.get_purchase_order_article_details(
            request.state.tenant, po_id, article, retail_region=retail_region
        )
        return {"data": {"table_config": table_config, "table_data": data}}

    @router.post("/place-holder/{po_id}/validate")
    @tenant_context_decorator
    async def validate_po(
        self,
        po_id: str,
        input_data: List[ArticleMappedStoreDetails],
        request: Request,
        authorization: str = Header(...)
    ):
        mapped_stores = DataFrame([data.dict() for data in input_data])
        response = await self.service.validate_po(
            request.state.tenant, po_id, mapped_stores
        )
        return {"data": response}
```

### Benefits of CBV
```python
@cbv(router)
class InventoryController:
    """
    Benefits:
    1. Shared state across methods (self.service)
    2. Logical grouping of related endpoints
    3. Cleaner code organization
    4. Easy to add shared setup in __init__
    """

    def __init__(self):
        # Shared across all methods
        self.service = InventoryService()
        self.logger = logging.getLogger(__name__)

    @router.get("/items")
    async def list_items(self, request: Request):
        self.logger.info("Listing items")
        return await self.service.list_items(request.state.tenant)

    @router.get("/items/{item_id}")
    async def get_item(self, item_id: str, request: Request):
        self.logger.info(f"Getting item {item_id}")
        return await self.service.get_item(request.state.tenant, item_id)
```

---

