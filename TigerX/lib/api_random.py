# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtsea

import requests

async def api_ceo_dog(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_DOG = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(API_DOG)
    if response.status_code == 200:
        data_ceo = response.json()
        try:
            photo_dog_url = data_ceo["message"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return 
        await client.send_photo(message.chat.id, photo=photo_dog_url, reply_to_message_id=message.id)
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_big_cat(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_BIG_CAT = "https://randombig.cat/roar.json"
    response = requests.get(API_BIG_CAT)
    if response.status_code == 200:
        data_cat = response.json()
        try:
            photo_cat_url = data_cat["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        await client.send_photo(message.chat.id, photo=photo_cat_url, reply_to_message_id=message.id)
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_ceo_dog2(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_CEO_DOG2 = "https://random.dog/woof.json"
    response = requests.get(API_CEO_DOG2)
    if response.status_code == 200:
        data_dog2 = response.json()
        try:
            photo_dog2_url = data_dog2["url"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        await client.send_photo(message.chat.id, photo=photo_dog2_url, reply_to_message_id=message.id)
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass

async def api_fox_ca(client, message):
    ran = await message.reply_text("<code>Uploading.......</code>")
    API_FOX_CA = "https://randomfox.ca/floof/"
    response = requests.get(API_FOX_CA)
    if response.status_code == 200:
        data_fox = response.json()
        try:
            photo_fox_url = data_fox["image"]
        except Exception as e:
            await ran.edit_text(f"Error requests: {e}")
            return
        await client.send_photo(message.chat.id, photo=photo_fox_url, reply_to_message_id=message.id)
    else:
        await ran.edit_text("Sorry, there was an error processing your request. Please try again later")
    try:
        await ran.delete()
    except Exception:
        pass