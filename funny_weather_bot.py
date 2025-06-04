import requests
from telegram.ext import Updater, CommandHandler

# Tvoji tokeni
TELEGRAM_TOKEN = '7398802739:AAFMuOII303MLdQAZZ7xt5VFvicZ9GsWPLA'
WEATHER_API_KEY = '8d92e5e1a5e04017609037c01f4ad832'

# Šaljiva prognoza
def funny_forecast(temp, weather):
    weather = weather.lower()
    if "rain" in weather:
        return "Pada kiša kao suze bivše kad vidi tvoj story. 🌧️"
    elif "clear" in weather:
        return "Sunčano je, taman da opereš kola da bi odmah pala kiša. ☀️"
    elif "cloud" in weather:
        return "Oblačno je, taman za gledanje serija ceo dan. ☁️"
    elif "snow" in weather:
        return "Sneg pada, ajde sad pravi Sneška i kukaj što je hladno. ❄️"
    else:
        return "Vreme je... kao tvoj ljubavni život – nestabilno. 🌪️"

# Komanda /vreme
def get_weather(update, context):
    city = ' '.join(context.args) or 'Beograd'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=sr"
    response = requests.get(url).json()

    if response.get("main"):
        temp = response["main"]["temp"]
        weather = response["weather"][0]["description"]
        forecast = funny_forecast(temp, weather)
        update.message.reply_text(f"{city.title()}: {temp}°C, {forecast}")
    else:
        update.message.reply_text("Ne mogu da pronađem to mesto. Da nisi izmislio grad? 🤨")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("vreme", get_weather))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
