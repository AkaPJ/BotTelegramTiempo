# ☀️ **TELEGRAM BOT THAT SENDS THE WEATHER FORECAST 🌦️**

A friendly **Telegram bot** that sends the weather forecast to your group or chat **every 12 hours**—fully customizable and automated! 🚀

---

## ✨ **Features**

- 📅 **Automatic Weather Updates** – Sends the weather forecast **twice a day** (you can customize the schedule!).  
- 🌍 **Custom Location** – Choose your location using **latitude and longitude** coordinates.  
- 🔒 **Free & Automated** – Runs on **GitHub Actions**, so no need to worry about servers—**100% FREE!**  
- 🛠️ **Simple & Customizable** – Easy to set up, personalize, and expand!  

---

## 📦 **Requirements**

Make sure you have the following before starting:  

- 🐍 **Python 3.11** or higher  
- 🔑 Access to the **OpenWeatherMap API**  
- 🤖 A **Telegram bot** created via [**@BotFather**](https://t.me/botfather)  
- 📢 A **chat or group** where the bot will send the weather updates  
- ✅ **GitHub Actions** enabled on your repository  

---

## 📚 **Installation**

Follow these steps to get your bot up and running:  

1. **Clone the repository:**  

```bash
git clone https://github.com/AkaPJ/BotTelegramTiempo.git
cd BotTelegramTiempo
```

2. **(Optional) Create a virtual environment:**  

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install the required dependencies:**  

```bash
pip install -r requirements.txt
```

4. **Set up your environment variables:**  

Create a `.env` file in the root directory and add the following:  

```env
WEATHER_API_KEY=your_openweathermap_api_key
CHAT_ID=your_telegram_chat_id
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

5. **Run the bot:**  

Just execute:  

```bash
python bot.py
```

🎉 **Enjoy the automated weather updates!**  

---

## 📅 **Customize the Schedule**

Want to change when the bot sends the weather updates? No problem!  

Simply modify the schedule in the following file:  

```bash
.github/workflows/telegram.yml
```

For example, the following code will send updates at **8:00 AM and 8:00 PM (UTC)**:  

```yaml
on:
  schedule:
    - cron: '0 8,20 * * *'
```

🔍 **Tip:** Use [**crontab.guru**](https://crontab.guru) to easily generate and understand cron expressions.  

---

## 🛠️ **Contribute**

We welcome **all contributions**—whether it's fixing bugs, adding features, or improving documentation. Here's how to contribute:  

1. **Fork** the repository.  
2. **Create** a new branch for your feature or fix.  
3. **Submit** a pull request.  

🙌 **Thank you for helping make this bot even better!**
