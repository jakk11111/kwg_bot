
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7688797707:AAEH1i8JUUht2Ld6MHr14-eVCNjy6lEf5fI"  # 请根据需要自行更换

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🔥 Official portal", url="https://kwg04.com/")],
        [InlineKeyboardButton("📲 Contact Customer Service", url="https://kwg04.com/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🎉 Welcome to the KWG Official Robot!\n\nPlease click the button below to enter the platform。",
        reply_markup=reply_markup
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("✅ Bot 已启动，监听中...")
    updater.idle()

if __name__ == '__main__':
    main()
