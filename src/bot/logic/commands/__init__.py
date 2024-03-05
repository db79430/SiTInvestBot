"""This package is used for a bot logic implementation."""
from src.bot.logic.commands.start import start_router as start_router
from src.bot.logic.handlers import handlers_router
from src.bot.logic.register.router import register_router
from aiogram import Router

bot_router = Router(name=__name__)

bot_router.include_routers(
    start_router,
    register_router,
    handlers_router,
)
