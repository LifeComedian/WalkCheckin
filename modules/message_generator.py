from modules.quote_fetcher import get_quote
from modules.weather_fetcher import get_weather
import yaml

def generate_message():
    """
    生成每日打卡提醒消息
    """
    # 读取配置文件
    with open("data/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    encouragements = config["encouragements"]

    # 获取哲理名言
    quote = get_quote()

    # 获取各城市天气
    cities = config["cities"]
    weather_list = []
    rain_detected = False
    hot_detected = False

    for city in cities:
        weather_result = get_weather(city)
        weather_list.append(weather_result)

        # 检测“雨”
        if "雨" in weather_result:
            rain_detected = True

        # 检测温度
        try:
            temp_str = weather_result.split(",")[-1].strip()
            temp_value = int(temp_str.replace("℃", "").replace("°C", ""))
            if temp_value > 30:
                hot_detected = True
        except:
            pass

    weather_info = "\n".join(weather_list)

    # 根据天气情况选择鼓励语
    if rain_detected:
        encouragement = encouragements.get("rain", encouragements["default"])
    elif hot_detected:
        encouragement = encouragements.get("hot", encouragements["default"])
    else:
        encouragement = encouragements["default"]

    # 组合最终消息
    message = f"{quote}\n\n{weather_info}\n\n{encouragement}"
    return message

# 测试
if __name__ == "__main__":
    msg = generate_message()
    print(msg)
    with open("daily_checkin.txt", "w") as f:
        f.write(msg)
