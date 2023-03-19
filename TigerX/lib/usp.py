from TigerX import *
from TigerX.lib import *

async def user_premium(c, m):
    out = ""
    async for mr in c.get_chat_members(m.chat.id):
        if mr.user.is_premium:
             out+= mr.user.mention + "\n" 
        else:
             await m.reply_text("no user premium")
             return
        try: 
             await m.reply_text(out)
        except Exception as e:
             await m.reply_text(f"{e}")
             return    
