import asyncio

import config

import zcord

bot = zcord.Bot(config.DISCORD_TOKEN)


async def main():
    async with bot.http:
        resp = await bot.http.request(
            "POST",
            f"/channels/{config.CHANNEL_ID}/messages",
            json={"content": "Hello, world!"},
        )
        m = zcord.Message._from_payload(dict(resp))
        print(m)


asyncio.run(main())
