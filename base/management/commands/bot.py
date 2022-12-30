from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from rest_framework_simplejwt.tokens import AccessToken

from base.models import Profile

from . import messages

def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs) 
        except Exception as e:
            error_message = f'Error: {е}'
            print(error_message)
            raise e

    return inner

@log_errors
def check_token(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    token_str = update.message.text
    access_token = None
    try:
        access_token = AccessToken(token_str)
    except:
        update.message.reply_text( 
            text = messages.INVALID_TOKEN,
        )

    user = User.objects.get(id = access_token['user_id'])

    profile = Profile( 
        chat_id = chat_id,
        user = user,
        username = update.message.from_user.username,
    )

    profile.save()

    update.message.reply_text( 
        text = messages.USER_SAVED,
    )

class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5, 
            read_timeout=1.0,
        )
        bot = Bot(
            request=request, 
            token=settings.TOKEN, 
        )
        print(bot.get_me())

        updater = Updater(
            bot = bot,
            use_context = True,
        )

        message_handler = MessageHandler(Filters.text, check_token)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()