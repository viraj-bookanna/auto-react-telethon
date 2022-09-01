import logging,os,asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import functions, types
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
load_dotenv(override=True)

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
STRING_SESSION = os.getenv('STRING_SESSION')
EMOJI = os.getenv('EMOJI')
TARGET = os.getenv('TARGET')
DELAY = int(os.getenv('DELAY'))

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
async def main():
    messages = await client.get_messages(TARGET, limit=1)
    last_message = messages[0]
    while True:
        try:
            async for message in client.iter_messages(TARGET, offset_id=last_message.id, reverse=True):
                result = await client(functions.messages.SendReactionRequest(
                    peer=TARGET,
                    msg_id=message.id,
                    big=True,
                    reaction=EMOJI
                ))
                last_message = message
        except Exception as e:
            print(repr(e))
        await asyncio.sleep(DELAY)
with client:
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        exit()