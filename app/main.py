from telegram.ext import Application, CommandHandler
from .config import Settings
from .db import Database
from .handlers import Handlers

def build_app(settings, db):
    h=Handlers(db,settings)
    app=Application.builder().token(settings.telegram_bot_token).build()
    app.add_handler(CommandHandler("start",h.start)); app.add_handler(CommandHandler("help",h.help)); app.add_handler(CommandHandler("status",h.status)); app.add_handler(CommandHandler("target",h.target)); app.add_handler(CommandHandler("finding",h.finding)); app.add_handler(CommandHandler("report",h.report)); app.add_handler(CommandHandler("ask",h.ask))
    return app

def main():
    settings=Settings.from_env(); db=Database(settings.database_path); build_app(settings,db).run_polling()

if __name__ == "__main__": main()
