from fastapi import FastAPI
import uvicorn

import __metadata__
import config
from routes import arithmatic_router, examine_router


app = FastAPI(
    openapi_url=f"{config.PATH_PREFIX}/openapi.json",
    docs_url=f"{config.PATH_PREFIX}/docs/",
    title=__metadata__.__title__,
    description=__metadata__.__description__,
    version=__metadata__.__version__,
    contact=__metadata__.__contact__,
    openapi_tags=__metadata__.__tags__,
)


@app.get(f"{config.PATH_PREFIX}/health-check/", tags=["Public"])
async def health_check():
    """Endpoint for health check."""
    return {"message": f"{config.APP_NAME} service is running."}


@app.get(f"{config.PATH_PREFIX}/version/", tags=["Public"])
async def version():
    """Endpoint for API version."""
    return {"message": __metadata__.__version__}


app.include_router(
    arithmatic_router,
    prefix=config.PATH_PREFIX + "/math",
    tags=["Math"],
)

app.include_router(
    examine_router,
    prefix=config.PATH_PREFIX + "/examine",
    tags=["Examine"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
