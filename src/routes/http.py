from fastapi import APIRouter, Request

import models


router = APIRouter()


@router.post("/", response_model=models.ExamineRequest)
async def http(
    request: Request,
) -> models.ExamineRequest:
    """
    Endpoint for examining the request object.
    """
    return models.ExamineRequest(
        headers=request.headers,
        body=""
    )
