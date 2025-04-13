from fastapi import FastAPI
import uvicorn

from views.add_measurements import router as add_measurements_router
from views.add_general_info import router as add_general_information_router

app = FastAPI()
app.include_router(add_measurements_router)
app.include_router(add_general_information_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
