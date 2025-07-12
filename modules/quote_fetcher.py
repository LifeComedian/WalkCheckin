import requests

def get_quote():
    """
    从一言（hitokoto.cn）获取一句哲理短句。
    返回格式：'内容 —— 来源'
    """
    url = "https://v1.hitokoto.cn/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            hitokoto = data['hitokoto']
            from_where = data['from']
            return f"{hitokoto} —— {from_where}"
        else:
            return "【获取一言失败】"
    except Exception as e:
        return f"【获取一言出错: {e}】"

# 测试
if __name__ == "__main__":
    print(get_quote())
