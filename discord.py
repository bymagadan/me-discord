from pypresence import Presence
from time import time

RPC = Presence("859819593827745792")
btns = [
    {
        "label": "VK",
        "url": "https://vk.com/hxuzjtocnzvv5g2rtg2bhwkcb"
    },

    {
        "label": "GitHub",
        "url": "https://github.com/bymagadan"
    }
]
RPC.connect()
RPC.update(
    state="КБТуху на 81 ворота!",
    details="ТСД для хуесосов",
    start=time(),
    buttons=btns,
    large_image="doomerdns1",
    small_image="znxnpl7xyao",
    large_text="пошли покурим?",
    small_text="пошли..."
    
)
input()

