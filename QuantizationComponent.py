# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: C:\ProgramData\Ableton\Live 101 Suite\Resources\MIDI Remote Scripts\APC40_MkIIx\QuantizationComponent.py
# Compiled at: 2019-06-18 00:58:30
from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.Control import RadioButtonControl, control_list
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot
AVAILABLE_QUANTIZATION = [
 Live.Song.Quantization.q_no_q,
 Live.Song.Quantization.q_8_bars,
 Live.Song.Quantization.q_4_bars,
 Live.Song.Quantization.q_2_bars,
 Live.Song.Quantization.q_bar,
 Live.Song.Quantization.q_quarter,
 Live.Song.Quantization.q_eight,
 Live.Song.Quantization.q_sixtenth]

class QuantizationComponent(ControlSurfaceComponent):
    quantization_buttons = control_list(RadioButtonControl)

    def __init__(self, *a, **k):
        super(QuantizationComponent, self).__init__(*a, **k)
        self.quantization_buttons.control_count = len(AVAILABLE_QUANTIZATION) + 1
        self._on_clip_trigger_quantization_changed.subject = self.song()
        self._on_clip_trigger_quantization_changed()

    @quantization_buttons.checked
    def quantization_buttons(self, button):
        if 0 <= button.index < len(AVAILABLE_QUANTIZATION):
            quantization = AVAILABLE_QUANTIZATION[button.index]
            if quantization != self.song().clip_trigger_quantization:
                self.song().clip_trigger_quantization = quantization

    @subject_slot(b'clip_trigger_quantization')
    def _on_clip_trigger_quantization_changed(self):
        self._get_button(self.song().clip_trigger_quantization).is_checked = True

    def _get_button(self, quantization):
        if quantization in AVAILABLE_QUANTIZATION:
            return self.quantization_buttons[AVAILABLE_QUANTIZATION.index(quantization)]
        return self.quantization_buttons[(-1)]