from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7884027155:AAF4H_eahkORElZolVVPumtscMpNbKH_TEA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Это черновик Куда Намылились 🙌"
                                    '\n'
                                    '\nДоступные команды:'
                                    '\n/connect - связаться с админом канала'
                                    '\n/post - опубликовать свой пост в ленте канала')

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Чтобы связаться с админом канала - пиши @wherelera")

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸Прайс-лист на публикации в канале:"
                                    '\nФормат '"Сторис"' (публикация на 24 часа) - стоит мильён'
                                    '\nФормат "Пост" - стоит как крыло самолёта'
                                    '\nФормат "Пост + закреп" - стоит как самолёт')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("connect", connect))
app.add_handler(CommandHandler("post", post))


print("Бот запущен...")
app.run_polling()