from . import APIBaseClass
from app.config import app_config
from app.templates import templates
from fastapi import Request
from fastapi.responses import HTMLResponse


class AppInfo(APIBaseClass):

    def __init__(self):
        super().__init__()
        self.router.add_api_route('/', self.homepage, methods=['GET'], status_code=200, response_class=HTMLResponse)
        self.router.add_api_route('/', self.life_check, methods=['POST'], status_code=200)
        self.app_name = app_config.app_name
        self.app_version = app_config.app_version

    async def homepage(self, request: Request):
        return templates.TemplateResponse("index.html", context={'request': request,
                                                                 'app_name': self.app_name,
                                                                 'app_version': self.app_version})

    def life_check(self):
        return f'SUMIT Warehouse {self.app_name} version {self.app_version} is live...'

