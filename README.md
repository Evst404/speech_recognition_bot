# Бот для распознавания речи Devman

Этот проект реализует два умных бота, интегрированных с DialogFlow для обработки естественного языка:

Телеграм-бот: Отвечает на сообщения пользователей умными ответами.
ВК-бот: Обрабатывает сообщения в группе ВКонтакте, уступая техподдержке при непонятных запросах.

## Установка
1. Склонируй репозиторий:
```
git clone <https://github.com/Evst404/speech_recognition_bot>
```
2. Установи зависимости:
```
pip install -r requirements.txt
```
3. Настрой переменные окружения в .env:
```
TELEGRAM_BOT_TOKEN=ваш-telegram-токен
VK_GROUP_TOKEN=ваш-vk-групповой-токен
DIALOGFLOW_PROJECT_ID=devman-speech-recognition-bot
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```
## Запуск ботов:
Выполнить команду в консоли:

Телеграм: 
```python telegram_bot.py```

ВКонтакте: 
```python vk_bot.py```


