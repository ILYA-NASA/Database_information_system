from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/1 - ID\n/2 - ФИО\n/3 - День рождения\n/4 - Успеваемость\n/5 - Пол\n/6 - Все данные\n/0 - Выход')

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'12345')

async def fio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Иван Иваныч')

async def birthday_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'29.02.1970')

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Успевает')

async def sex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Мужской')

async def all_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Какие-то все данные')

async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Всем пока')