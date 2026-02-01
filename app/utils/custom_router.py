from enum import Enum

from fastapi import APIRouter
from typing import Callable, Any
from fastapi_utils.cbv import cbv


class CustomRouter(APIRouter):
    def get_route(self, path : str , * ,  include_in_schema : bool = True , **kwargs : Any ) -> Callable:
        #1. Standardize removing trailing zero
        if path.endswith("/") and path != "/" :
            path = path[:-1]


