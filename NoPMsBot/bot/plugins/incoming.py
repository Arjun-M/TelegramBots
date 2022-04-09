from core import client , Bot
from pyTelegramClient import Button,  Markup 

stored = []
chat = None

def onMessage(event):
    result = Bot.copyMessage(chat , event.update["chat"]["id"] , event.update["message_id"] )
    if result.get("ok" , True) is False:
        return event.respond("Failed to sendMessage to this chat , Seems like he have blocked me .")
    event.respond("I have delivered your message to the recipient .")    
    
@client.messageHandler( types=[ "contact" , "location" , "via_bot" ,"voice" , "video_note" , "text" , "photo" , "audio" , "document" , "animation" , "sticker" , "video"] )
def incoming( event ):
    update = event.update
    fromuser = update["chat"]["id"]
    markup = Markup.inline_keyboard([
        [ Button.inline("Reply", f"/reply {fromuser}") , Button.inline("Info", f"/info {fromuser}") ]
    ])
    result = Bot.copyMessage( 2087092793 , update["user"]["id"] , update["message_id"] , reply_markup=markup )
    if result.get("ok" , True) is False:
        stored.append( { "chat" : update["user"]["id"] , "message" : update["message_id"] } )
        return event.respond("Seems , my admin is busy and forgot to unblock me . Don't worry I will forward your message when he unblock me ." , reply=True)
    return event.respond("Fine, your message have been forwarded to my admin .")

@client.callbackQueryHandler( data=["/storedMessage"] )
def storedMessage( event ):
    if len(stored) < 1:
        return event.answer("You haven't recived any messages when you was away .")
    for x in stored:
        fromuser = x["chat"]
        markup = Markup.inline_keyboard([
            [ Button.inline("Reply", f"/reply {fromuser}") , Button.inline("Info", f"/info {fromuser}") ]
        ])
        Bot.copyMessage( 2087092793 , fromuser , x["message"] , reply_markup=markup )
    event.respond("You have recived "+len(stored)+" messages when you was away .",reply=True)
    stored = []
    

@client.callbackQueryHandler( regexp="/reply (.*)" )
def reply( event ):
    user = event.json["data"].split(" ")[1]
    chat = user
    client.addEventListner(user , onMessage)
    
    
