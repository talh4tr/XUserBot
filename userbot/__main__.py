from pyrogram import Client, idle

from userbot import app, Db

if __name__ == "__main__":
  app.start()
  me = app.get_me()
  Db.initialize_db(me.id)
  app.send_message("me", "`Database is initialized!`")
  idle()
