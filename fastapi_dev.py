import uvicorn
from fastapi_frm.app import app

uvicorn.run(app, host="127.0.0.1", port=8081)
