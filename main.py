import discord
import os
import quotes
import random
import msg
import datalist
from keep_alive import keep_alive


# discord
client = discord.Client()

# user interactiom
user = msg.Interactions()

# discord msg formatting
write = msg.Formatting()

# dijalankan saat bot baru saja di run
@client.event
async def on_ready() :
  print(f'Logged in as {client.user}')
  # client.user = bot ini

  # menampilkan status listening
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='-tulung'))


# function untuk mengolah command
@client.event
async def on_message(msg):
  # jika msg-nya dari bot ini maka abaikan
  if msg.author == client.user :
    return

  # mendapatkan input dari user
  user_input = msg.content

  # mengeluarkan output
  # msg.channel.send()

  if len(user_input) > 8 and user_input.isupper() and not any(word in user_input for word in user.capsExcepts) :
    await msg.channel.send('`CAPSLOCK JEBOL BRO?`')

  # jika user mengetik /tulung di chat
  if user_input.startswith('-tulung') :
    await msg.channel.send(write.bold('-quote') + ' = mengeluarkan quotes bijak')

  elif any(word in user_input.lower() for word in user.help) :
    await msg.channel.send(write.bold('mupeng') + '\nlu sokap ?')

  if user_input.startswith('-quote') :
    quote = quotes.getQuote()
    await msg.channel.send(f'{write.quote_bold_italic(quote)}')

  if any(word in user_input.lower() for word in user.toxic) :
    await msg.channel.send(random.choice(user.replyToxic))

  # database
  if user_input.startswith('-datarespond') :
      respond = user_input.split('-datarespond ',1)[1].capitalize()
      if respond.lower() == 'true' :
        datalist.set_data_respond(True)
      elif respond.lower() == 'false' :
        datalist.set_data_respond(False)
      await msg.channel.send(f'data respond berhasil diubah menjadi {write.bold(respond)}')
  
  if user_input.startswith('-getdatarespond') :
    respond = datalist.get_data_respond()
    await msg.channel.send(f'data respond : {write.bold(respond)}')
    return

  if datalist.get_data_respond() :
    if user_input.startswith('-add') :
      data = user_input.split('-add ',1)[1]
      datalist.store_data(data)
      await msg.channel.send(f'{write.bold(data)} telah ditambahkan')

    if user_input.startswith('-get') :
      get_datalist = datalist.get_data()
      await msg.channel.send(get_datalist)

    if user_input.startswith('-del') :
      index = user_input.split('-del ',1)[1]
      delete = datalist.delete_data(int(index))
      await msg.channel.send(delete)


keep_alive()

# menjalankan bot
client.run(os.getenv('TOKEN'))
