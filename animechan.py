# Humanoid - UserBot
#
# This file is a part of < https://github.com/TeamHumanoid/HumanoidAddons/>

"""
Fetch Random anime quotes

Command : `{i}aniquote`
"""

import requests

from . import *


@Humanoid_cmd(pattern="aniquote")
async def _(ult):
    u = await eor(ult, "...")
    try:
        resp = requests.get("https://animechan.vercel.app/api/random").json()
        results = f"**{resp['quote']}**\n"
        results += f" — __{resp['character']} ({resp['anime']})__"
        return await u.edit(results)
    except Exception:
        await u.edit("`Something went wrong LOL ...`")
