from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/Hello\n/Help\n/ID\n/FIO\n/Birthday\n/Progress\n/Sex\n/All_data\n/Exit')

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'12345')

async def fio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Иван Иваныч')

# async def birthday_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def sex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def all_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')