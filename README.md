Purpose:
Create a robot to send certain messages in groupchat for daily walking checkin.

The message contains:
1. a paragraph of philoosophy content
2. today's weather report in 4 cities: Nantong, Rugao, Xiamen, and Kunshan
3. a encourage notice randomly chosen from my given 5 sentences

Environment:
The robot is built on a laptop with Ubuntu system.

Structure:
walkcheckin/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── quote_fetcher.py
│   ├── weather_fetcher.py
│   └── message_sender.py
├── data/
│   ├── quotes_cache.json
│   └── config.yaml
├── logs/
│   └── run.log
├── requirements.txt
└── README.md

💛 **WalkCheckin 项目 README.md**

---

# 🌤️ WalkCheckin

**每日微信打卡提醒生成器**

每天定时获取：

* 一段哲理名言（来自一言 API）
* 四个指定城市的天气情况（来自和风天气 API）
* 根据天气和温度智能切换的鼓励语

并通过 **PushPlus** 推送到你的微信，手动复制发送到微信群，完成每日 check-in 任务。

---

## 📁 **项目结构**

```
walkcheckin/
├── data/
│   └── config.yaml
├── logs/
│   └── run.log
├── modules/
│   ├── quote_fetcher.py
│   ├── weather_fetcher.py
│   └── message_generator.py
├── main.py
└── README.md
```

---

## ⚙️ **依赖安装**

1. 进入项目文件夹

```bash
cd ~/projects/walkcheckin
```

2. 激活 venv

```bash
source /home/lc/venv/bin/activate
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

若没有 requirements.txt，可使用：

```bash
pip install requests pyyaml
```

---

## 🔑 **配置**

### **data/config.yaml**

```yaml
cities:
  - 北京
  - 上海
  - 广州
  - 深圳

encouragements:
  default: "今天也是元气满满的一天，去完成你的目标吧！"
  rain: "下雨天也要保持好心情，记得带伞哦！"
  hot: "今天很热，注意补水防晒，照顾好自己！"
```

---

## 🚀 **运行**

### **手动运行**

```bash
cd ~/projects/walkcheckin
/home/lc/venv/bin/python main.py
```

---

### **自动定时运行**

1. 打开 crontab

```bash
crontab -e
```

2. 添加任务

```
0 22 * * * cd /home/lc/projects/walkcheckin && /home/lc/venv/bin/python main.py >> logs/run.log 2>&1
```

📌 **每天 22:00 自动运行**。

---

## 🔧 **环境检查**

✅ 查看当前 python 路径：

```bash
which python
```

✅ 检查 venv python 路径是否存在：

```bash
ls /home/lc/venv/bin/python
```

✅ 测试 cronjob 是否运行成功：

查看 `logs/run.log` 输出。

---

## 💡 **后续优化 TODO**

* [ ] 使用 Server 酱 企业微信机器人直接群发
* [ ] Docker 化部署
* [ ] 日志异常告警通知
* [ ] 多人项目协作部署流程

---

✨ **WalkCheckin v1.0**

👨‍💻 **Author**: lc
🗓️ **Date**: 2025-07-02
🌟 **Description**: 最简单的每日提醒，也能成为长期 discipline 的起点。

---
