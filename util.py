import os
import re
from functools import reduce
import requests

# constants
WELCOME_CHANNEL = 'random' # channel in which to send welcome message for new members
MESSAGE_EMOJI = '🐴' # emoji that'll be mainly used to react to user messages
RESPONSE_EMOJI = '🚚' # emoji that'll be used to react to all bot messages
FIXED_COGS = [ # all cogs that aren't from the google sheet
    'Reuniões', 'OnMemberJoin', 'Decisions',
    'Counters', 'Utilities', 'Birthday',
    'Rent'
]
AVAILABLE_REACTIONS = [ # list of reactions that'll be used in poll-like commands
    '🤠', '🍉', '💘', '🏂',
    '🧨', '🎂', '💣', '🎷', '🛹'
]
VOCATIVES = [ # list of vocatives that'll be used on the welcome message for new members
    'anjo', 'consagrado', 'comparsa',
    'amigo', 'caro', 'cumpadi', 'bonito',
    'campeão', 'tributarista', 'chegado',
    'peregrino', 'camponês', 'patrão',
    'donatário', 'bacharel', 'iluminado',
    'democrata', 'parnasiano', 'vacinado',
    'querido', 'barbeiro', 'zé', 'filho'
]

async def reactToResponse(bot, response, emojiList = []):
    if not emojiList: emojiList = []

    emojiList.insert(0, RESPONSE_EMOJI)
    for emoji in emojiList:
        try:
            await response.add_reaction(emoji)
        except:
            print(f"   [**] There was an error while reacting {emoji} to the response.")
        else:
            print(f"   [**] The reaction {emoji} was successfully added to the response.")

async def reactToMessage(bot, message, emojiList: list):
    for emoji in emojiList:
        try:
            await message.add_reaction(emoji)
        except:
            print(f"   [**] There was an error while reacting {emoji} to the message.")
        else:
            print(f"   [**] The reaction {emoji} was successfully added.")

# downloads the image from a link and returns it's path
def getImage(img: str):
    if img.startswith('http'):
        try: r = requests.get(img)

        except:
            print('   [**] There was an error with the image link: ' + img)
            img = False

        else:
            with open('aux.png', 'wb') as f: f.write(r.content)
            r.close()

            img = 'aux.png'
            print('   [**] The image was successfully downloaded.')

    else:
        print('   [**] There is no image to attach.')
        img = False

    return img

# Generates cogs based on the sheet's commands
def refreshCogs(bot, hasLoaded=True):
    if not os.path.isdir('./cogs'): os.mkdir('./cogs')

    # Unloads and then removes all cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename.replace('.py', '') not in FIXED_COGS:
            if hasLoaded: bot.unload_extension(f'cogs.{filename.replace(".py","")}')
            os.remove(f'./cogs/{filename}')

    # Loads all cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and (filename.replace('.py', '') not in FIXED_COGS or not hasLoaded):
            bot.load_extension(f'cogs.{filename.replace(".py","")}')

    return
