# WalkCheckin

**WalkCheckin** is a simple automation script that sends a daily WeChat message including:

- A philosophical quote  
- Real-time weather info for four selected cities  
- A motivational sentence, dynamically chosen based on the weather  

Designed to run automatically on an Ubuntu server using `cron`.

## 🚀 Features

- 🌟 Inspirational quote from [Hitokoto](https://hitokoto.cn/)  
- 🌦 Real-time weather data via [QWeather (HeFeng)](https://dev.qweather.com/)  
- 🤖 Adaptive encouragements based on weather (e.g., rainy or hot days)  
- 🔔 Push notification via [PushPlus](http://www.pushplus.plus/)  
- 🖥️ Cron-based long-term scheduling  

## 📁 Project Structure

```
walkcheckin/
├── data/
│   ├── config.yaml             # Private configuration (ignored)
│   └── config.example.yaml     # Public example for setup
├── quote_fetcher.py
├── weather_fetcher.py
├── message_generator.py
├── message_sender.py
├── main.py
└── requirements.txt
```

## ⚙️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create your config file:

```bash
cp data/config.example.yaml data/config.yaml
```

Edit `config.yaml` with your API keys and city information.

3. Run the script manually:

```bash
python main.py
```

## 📅 Automate with Crontab

Example: Run daily at 10 PM

```bash
0 22 * * * cd /path/to/walkcheckin && source /path/to/venv/bin/activate && python main.py >> logs/run.log 2>&1
```

## 📝 License

MIT
