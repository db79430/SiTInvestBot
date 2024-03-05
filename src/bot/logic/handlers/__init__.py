from aiogram import Router
from .info_more_handlers import info_more_router as info_more_router
from .invest_handlers import invest_router as invest_router


handlers_router = Router(name=__name__)

handlers_router.include_routers(info_more_router, invest_router)
