import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from requests import HTTPError
from fast_api import settings
from fast_api.routers.hello import router as test_router
from fast_api.routers.fsharp import router as fsharp_router
import secrets
from fastapi import status, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from fastapi.middleware.trustedhost import TrustedHostMiddleware

http_basic = HTTPBasic()


def authorize(credentials: HTTPBasicCredentials = Depends(http_basic)) -> str:
    if settings.HTTP_BASIC_USERNAME and settings.HTTP_BASIC_PASSWORD:
        correct_username = secrets.compare_digest(credentials.username, settings.HTTP_BASIC_USERNAME)
        correct_password = secrets.compare_digest(credentials.password, settings.HTTP_BASIC_PASSWORD)
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username


app = FastAPI()
origins = [
    "http://localhost:1234"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# custom error handling
@app.exception_handler(HTTPError)
async def requests_exception_handler(request: Request, exc: HTTPError):
    return JSONResponse(
        # status_code=exc.response.status_code,
        status_code=400,
        content={
            "message": exc.response.text,
        },
    )


@app.get("/", tags=["Index"], dependencies=[Depends(authorize)])
async def index():
    return {"message": "Hello World"}


@app.get("/me")
def get_current_user(username: str = Depends(authorize)):
    return {"username": username}


# Add routers
app.include_router(fsharp_router, prefix="/api", dependencies=[Depends(authorize)])
if settings.DEBUG:  # only in debug mode
    app.include_router(test_router, prefix="/api", dependencies=[Depends(authorize)])

# Add middlewares
if settings.ALLOWED_HOSTS:
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS,
    )


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fast_api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
