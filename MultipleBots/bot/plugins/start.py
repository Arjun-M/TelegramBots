from .core import client1 , client2 , Bot1 , Bot2 
from pyTelegramClient import Button , Markup 



@client1.messageHandler( types= ["text"] )
def start( event ):
    markup = Markup.inline_keyboard([
        [Button.url("Admin","https://t.me/itz_ArjunM") , Button.url("Github","https://github.com/Arjun-M")],
        [Button.url("Source Code" , "https://github.com/Arjun-M/TelegramBots")]
    ])
    event.respond("Example multiple bot in single server .", reply=True)
    
    
@client2.messageHandler( types= ["text"] )
def start( event ):
    markup = Markup.inline_keyboard([
        [Button.url("Admin","https://t.me/itz_ArjunM") , Button.url("Github","https://github.com/Arjun-M")],
        [Button.url("Source Code" , "https://github.com/Arjun-M/TelegramBots")]
    ])
    event.respond("Example multiple bot in single server .", reply=True)
