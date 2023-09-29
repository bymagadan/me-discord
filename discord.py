from pypresence import Presence
from time import time

RPC = Presence(" // ")
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
    state=" ",
    details=" ",
    start=time(),
    buttons=btns,
    large_image=" ",
    small_image=" ",
    large_text=" ",
    small_text=" "
    
)
input()

#not relevant :/
