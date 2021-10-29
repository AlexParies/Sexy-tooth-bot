import discord
import keep_alive
keep_alive.keep_alive()



class MyClient(discord.Client):
    async def on_ready(self):

        print('Logged on as', self.user)

    async def on_message(self, message):







      

      
      if message.content == "whos joe?":
       await message.channel.send("https://cdn.discordapp.com/attachments/871878422526308395/903656585266602014/image0.jpg")
      if message.content == 'nilbog':
        await message.channel.send("nilbog is goblin backwards!")
    
      if message.content == 'teeth commands':
        await message.channel.send('(joe, Badger time, cube pls?[alex only*]), cube pls, cube pls!, am i the original starwalker, teeth commands, mike, whos joe?, nilbog')
      #commands
 
        #que prank for the lawls
      if message.content == 'mike':
         await message.channel.send("we dont need mike")
     #mike
      if message.author == self.user:
        return

      if message.author.id == 870022416313753642:

        if message.content == 'joe':
            await message.channel.send('mother')
        # joe mom joke
        if message.content == 'Badger time':
            await message.channel.send('https://cdn.discordapp.com/attachments/871878422526308395/902999507573284945/zXHZWGLWNQkrS.gif')
#badger time


        if message.content == 'cube pls':
            await message.channel.send('🧊')
        

        if message.content == 'cube pls?':
            await message.channel.send('no')        
        if message.content=='cube pls!':
          x = 0
          while x < 30:
            await message.channel.send("🧊")
            x = x + 1        
            #cubes
        #only i can talk
        
      if message.author.id == 344082647787634690:
        if message.content == 'am i the original starwalker':
            await message.channel.send("You am not the original          starwalker")
          # starwalker       
      if message.author.id == 344082647787634690:
        return
      if message.author == self.user:
        if message.content == 'am i the original starwalker':
            await message.channel.send("You am the original          starwalker")

      if message.author.id == 870022416313753642:
        return
      if message.author == self.user:
        if message.content == 'cube pls':
            await message.channel.send("no")
        if message.content == 'cube pls!':
            await message.channel.send("no")


client = MyClient()

client.run('OTAzMzM1MjkyODM5Mjg0Nzg2.YXrejA.yUQ4hDh_R6zADrnsfMrorISTvGw')