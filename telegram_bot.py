# Настроить кирилицу.
# Указать командам исполняющие методы.
# Интерфейс.


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram_bot_commands import *

app = ApplicationBuilder().token("5157594801:AAFHHasq8CBNBoT5y6V55vvkMYuawHJk4_8").build()

app.add_handler(CommandHandler("hello", hello_command))             # Приветствие
app.add_handler(CommandHandler("help", help_command))               # Показать список команд
app.add_handler(CommandHandler("ID", id_command))                   # 1 - вывод ID
app.add_handler(CommandHandler("FIO", fio_command))                 # 2 - вывод ФИО
# app.add_handler(CommandHandler("Birthday", birthday_command))     # 3 - вывод ДР
# app.add_handler(CommandHandler("Progress", progress_command))     # 4 - вывод успеваемости
# app.add_handler(CommandHandler("Sex", sex_command))               # 5 - вывод пола
# app.add_handler(CommandHandler("All data", all_data_command))     # 6 - вывод всех данных
# app.add_handler(CommandHandler("Exit", exit_command))             # 0 - выход

print('server start')

app.run_polling()

# t.me/Ivan_Ivanovichh_bot