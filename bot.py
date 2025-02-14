import telebot

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Group me har message check karne ke liye
@bot.message_handler(func=lambda message: True)
def check_message(message):
    bad_words = ["spam", "abuse", "scam"]  # Yahan aap custom words add kar sakte hain
    if any(word in message.text.lower() for word in bad_words):
        bot.send_message(message.chat.id, f"🚨 Alert! {message.from_user.first_name} ne restricted word use kiya! ⚠️")

bot.polling()
