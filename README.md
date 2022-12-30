# django_telegram_bot

Algorithm: 
1. Register
2. Find bot and send access_token
3. Send message using REST API (Specify Authorization header)
4. Get all messages (Specify Authorization header)

### POST https://django-telegram-bot.herokuapp.com/api/register/
Body:
{
    "username": "username",
    "password": "password",
    "first_name": "first_name",
    "last_name": "last_name"
}

### GET https://django-telegram-bot.herokuapp.com/api/get-bot-link/

### POST https://django-telegram-bot.herokuapp.com/api/token/
Body:
{
    "username": "username",
    "password": "password"
}

### POST https://django-telegram-bot.herokuapp.com/api/token/refresh/
Body:
{
    "refresh": "refresh_token"
}

### POST https://django-telegram-bot.herokuapp.com/api/messages/send
Authorization header: Bearer access_token

Body:
{
    "text": "your text"
}

### GET https://django-telegram-bot.herokuapp.com/api/messages
Authorization header: Bearer access_token
