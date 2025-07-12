import requests
import os
import yaml

config_path = os.path.join(os.path.dirname(__file__), "../data/config.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

PUSHPLUS_TOKEN = config["api_keys"]["pushplus"]

def send_to_pushplus(message):
    url = "http://www.pushplus.plus/send"
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "今日打卡提醒",
        "content": message,
        "template": "txt"
    }
    try:
        response = requests.post(url, json=data, timeout=5)
        if response.status_code == 200:
            print("消息已推送到微信")
        else:
            print(f"推送失败 status: {response.status_code}")
    except Exception as e:
        print(f"推送出错: {e}")

if __name__ == "__main__":
    send_to_pushplus("测试推送内容")
