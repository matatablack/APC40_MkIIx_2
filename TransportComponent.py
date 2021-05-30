# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: C:\ProgramData\Ableton\Live 101 Suite\Resources\MIDI Remote Scripts\APC40_MkIIx\TransportComponent.py
# Compiled at: 2019-06-18 00:58:30
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import ButtonControl
from _Framework.SubjectSlot import subject_slot
from _Framework.TransportComponent import TransportComponent as TransportComponentBase
from _Framework.Util import clamp

class TransportComponent(TransportComponentBase):
    shift_button = ButtonControl()

    def __init__(self, *a, **k):

        def play_toggle_model_transform(val):
            if self.shift_button.is_pressed:
                return False
            return val

        k[b'play_toggle_model_transform'] = play_toggle_model_transform
        super(TransportComponent, self).__init__(*a, **k)
        self._tempo_encoder_control = None
        return

    def set_tempo_encoder(self, control):
        assert not control or control.message_map_mode() in (
         Live.MidiMap.MapMode.relative_smooth_two_compliment,
         Live.MidiMap.MapMode.relative_two_compliment)
        if control != self._tempo_encoder_control:
            self._tempo_encoder_control = control
            self._tempo_encoder_value.subject = control
            self.update()

    @subject_slot(b'value')
    def _tempo_encoder_value(self, value):
        if self.is_enabled():
            step = 0.1 if self.shift_button.is_pressed else 1.0
            amount = value - 128 if value >= 64 else value
            self.song().tempo = clamp(self.song().tempo + amount * step, 20, 999)