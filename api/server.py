import uvicorn

from fastapi import FastAPI

from routers import main_page


server = FastAPI()

server.include_router(main_page.router)

if __name__ == '__main__':
    uvicorn.run(server, host='0.0.0.0', port=8080)