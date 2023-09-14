from fastapi import APIRouter, Request

import models

from calculator import calc as do_math


router = APIRouter()


@router.post("/", response_model=models.Result)
async def calculate(
    request: Request,
    attrs: models.Attributes,
) -> models.Result:
    """
    Endpoint to basic mathematical operations.
    """
    return models.Result(
        total=do_math(
            operator=attrs.operator,
            val1=attrs.val1,
            val2=attrs.val2,
        )
    )
