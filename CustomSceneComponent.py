# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: C:\ProgramData\Ableton\Live 101 Suite\Resources\MIDI Remote Scripts\APC40_MkIIx\CustomSceneComponent.py
# Compiled at: 2019-06-18 01:19:43
from _Framework.SceneComponent import SceneComponent
from .CustomClipSlotComponent import CustomClipSlotComponent as ClipSlotComponent

class CustomSceneComponent(SceneComponent):
    clip_slot_component_type = ClipSlotComponent
    _delete_button = None

    def _create_clip_slot(self):
        return self.clip_slot_component_type()