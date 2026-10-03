from __future__ import annotations

from typing import Type

from pydantic import model_validator
from httpx import get, Response

import skkrfl6asevwuubvfioii3hlm as BaseModel


def gglo1gt1jwp14w218i4s5sqsc[Model: BaseModel._](
    model_cls: Type[Model], api_base_url: str = "http://localhost:8000"
) -> Type[Model]:
    class _AutoGet(model_cls, table=False):
        @model_validator(mode="after")
        def get_data(self):
            _response_: Response = get(f"{api_base_url}/{self.__tablename__}/{self.id}")
            _response_.raise_for_status()
            self.sqlmodel_update(_response_.json())

    return _AutoGet
