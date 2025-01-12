# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#


import requests
from io import BytesIO
import os
import json
import random
import asyncio
from pyrogram import *
from pyrogram.types import *

from TigerX import OPENAI_API

from TigerX import *
from TigerX.lib import *

async def chatgpt_ask(c, m):
    question = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    if not question:
       await m.reply(f"use command <code>.{m.command[0]} [question]</code> to ask questions using the API.")
       return

    if not OPENAI_API:
       await m.reply("missing api key : `OPENAI_API`")
       return

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API}"}
    json_data = {"model": "text-davinci-003", "prompt": question, "max_tokens": 200, "temperature": 0}

    msg = await m.reply(f"Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception as e:
        await msg.edit_text(f"Yahh, sorry i can't get your answer: {e}")


# credits @xtsea

async def chatpgt_image_generator(c, m):
    A = "h"
    B = "t"
    C = "t"
    D = "p"
    E = "s"
    chatgpt_api_url = "api.openai.com"
    version = "v1"
    new_image = "images/generations"
    model = "image-alpha-001"
    new_link = A + B + C + D + E

    image_text = (m.text.split(None, 1)[1] if len(m.command) != 1 else None)
    if not image_text:
       await m.reply_text(f"example <code>+{m.command[0]} superhero<code> : to using the chatgpt api image")
       return

    if not OPENAI_API:
       await m.reply_text("Missing Api key: <code>OPENAI_API</code>")
       return

    headers={"Authorization": f"Bearer {OPENAI_API}"}
    json={"model": model, "prompt": image_text, "size": "1024x1024", "response_format": "url"}

    response = requests.post(f"{new_link}://{chatgpt_api_url}/{version}/{new_image}", headers=headers, json=json)
    try:
        image_url = response.json()['data'][0]['url']
    except Exception:
        pass
        return
    image_content = requests.get(image_url).content
    new_caption = f"Question: {image_text}"
    try:
        pro = await m.reply_text("<code>Uplading chatgpt image......</code>")
        await c.send_photo(m.chat.id, photo=BytesIO(image_content), caption=new_caption, reply_to_message_id=m.id)
    except Exception as e:
        await pro.edit_text(str(e))
    try:
        await pro.delete()
    except Exception:
        pass
