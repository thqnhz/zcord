import asyncio

import config

import zcord


async def main():
    print(zcord.__version__)
    async with zcord.Bot(config.DISCORD_TOKEN) as bot:
        m = await bot.http.send_message(
            config.CHANNEL_ID, content="Hello, world!"
        )

    # or
    # bot = zcord.Bot(config.DISCORD_TOKEN)
    # m = await bot.http.send_message(config.CHANNEL_ID, content="Hello, world!")
    # await bot.close()

    print("=" * 20)
    print(m)
    print("=" * 20)


asyncio.run(main())
