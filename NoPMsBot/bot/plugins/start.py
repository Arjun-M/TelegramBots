from .core import client , Bot
from pyTelegramClient import Button , Markup 



@client.messageHandler( commands= ["/start" , "/help"] )
def start( event ):
    markup = Markup.inline_keyboard([
        [Button.url("Admin","https://t.me/itz_ArjunM") , Button.url("Github","https://github.com/Arjun-M")],
        [Button.url("Source Code" , "https://github.com/Arjun-M/TelegramBots")]
    ])
    event.respond("Hello , I am PM chat bot of @itz_ArjunM\n\n<i>You can contact him through me .</i>" , parse_mode= "html", reply = True , reply_markup = markup)

