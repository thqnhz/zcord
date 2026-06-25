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
        print("=" * 20)
        resp = await bot.http.request(
            "GET",
            f"/guilds/{config.GUILD_ID}/roles",
        )
        for g in resp:
            m = zcord.Role._from_payload(dict(g))
            print(m)
            print("=" * 20)


asyncio.run(main())
