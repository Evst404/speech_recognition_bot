# Бот для распознавания речи Devman

Этот проект реализует два умных бота, интегрированных с DialogFlow для обработки естественного языка:

Телеграм-бот: Отвечает на сообщения пользователей умными ответами.
ВК-бот: Обрабатывает сообщения в группе ВКонтакте, уступая техподдержке при непонятных запросах.

Telegram-bot:

![](https://github.com/user-attachments/assets/c68d192b-290d-4d33-945c-df47460ca55a)

Vk-bot:

![Анимация2](https://github.com/user-attachments/assets/a3288d11-041e-446d-813a-47fc627e6073)

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
Выполнить команду в консоли (Локально):

Телеграм: 
```python telegram_bot.py```

ВКонтакте: 
```python vk_bot.py```

На сервере: Боты развёрнуты как systemd-сервисы на DigitalOcean VPS. Для перезапуска:
```
sudo systemctl restart telegram-bot
sudo systemctl restart vk-bot
```

## Развёртывание

Боты развёрнуты на DigitalOcean VPS (IP: 178.128.196.169) с использованием systemd-сервисов.
Мониторинг ошибок настроен: при сбоях уведомления отправляются в Telegram-лог-бот (требуется LOG_BOT_TOKEN и LOG_CHAT_ID).


