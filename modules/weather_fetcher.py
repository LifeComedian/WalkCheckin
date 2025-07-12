import requests
import os
import yaml

config_path = os.path.join(os.path.dirname(__file__), "../data/config.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["api_keys"]["heweather"]["key"]
API_HOST = config["api_keys"]["heweather"]["host"]

def get_location_id(city_name):
    """
    根据城市名获取和风天气 LocationID
    """
    try:
        url = f"https://{API_HOST}/geo/v2/city/lookup?location={city_name}&lang=zh"
        headers = {
            "X-QW-Api-Key": API_KEY
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data["code"] == "200" and data["location"]:
                return data["location"][0]["id"]
            else:
                print(f"{city_name}：获取LocationID失败 code: {data.get('code')}")
                return None
        else:
            print(f"{city_name}：请求失败 status: {response.status_code}")
            return None
    except Exception as e:
        print(f"{city_name}：请求出错: {e}")
        return None

def get_weather(city_name):
    """
    获取指定城市当前天气信息
    返回格式：'城市：天气, 温度℃'
    """
    location_id = get_location_id(city_name)
    if not location_id:
        return f"{city_name}：未能获取LocationID"

    try:
        weather_url = f"https://{API_HOST}/v7/weather/now?location={location_id}&lang=zh"
        headers = {
            "X-QW-Api-Key": API_KEY
        }
        wea_response = requests.get(weather_url, headers=headers, timeout=5)
        if wea_response.status_code == 200:
            wea_data = wea_response.json()
            if wea_data["code"] == "200":
                weather = wea_data["now"]["text"]
                temp = wea_data["now"]["temp"]
                return f"{city_name}：{weather}, {temp}℃"
            else:
                return f"{city_name}：获取天气失败 code: {wea_data.get('code')}"
        else:
            return f"{city_name}：天气请求失败 {wea_response.status_code}"

    except Exception as e:
        return f"{city_name}：天气获取出错: {e}"

# 测试
if __name__ == "__main__":
    cities = ["南通", "厦门", "昆山", "如皋"]
    for city in cities:
        print(get_weather(city))
