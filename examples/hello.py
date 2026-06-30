import asyncio

import config

import zcord

bot = zcord.Bot(config.DISCORD_TOKEN)


async def main():
    print(zcord.__version__)
    async with bot.http:
        resp = await bot.http.request(
            "POST",
            f"/channels/{config.CHANNEL_ID}/messages",
            json={"content": "Hello, world!"},
        )
        m = zcord.Message._from_payload(dict(resp))
        print("=" * 20)
        print(m)
        print("Message creation timestamp")
        print(m.timestamp)
        print("Message timestamp parsed with id")
        print(m.id.to_datetime())
        print("=" * 20)


asyncio.run(main())
