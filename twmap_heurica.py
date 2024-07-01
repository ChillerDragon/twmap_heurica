#!/usr/bin/env python3

from typing import Optional

import twmap

class LayerPosition:
    group: int
    layer: int

    def __init__(self, group: int, layer: int):
        self.group = group
        self.layer = layer

    def __repr__(self) -> str:
        return f"<LayerPostion group={self.group} layer={self.layer}>"

def get_freeze_layer_indecies(map: twmap.Map) -> Optional[LayerPosition]:
    pos = LayerPosition(0, 0)
    for g in map.groups:
        for l in g.layers:
            if l.kind() == 'Tiles':
                if not l.image:
                    continue
                img = map.images[l.image]
                print(img.name)
                print(l.width())
    return pos

m = twmap.Map("/home/chiller/.teeworlds/maps/ChillBlock.map")
pos = get_freeze_layer_indecies(m)
print(pos)

