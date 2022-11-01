import uvicorn
from .settings import settings

uvicorn.run(
    'workshop.app:app',
    reload=True,
    host=settings.server_host,
    port=settings.server_port,

)