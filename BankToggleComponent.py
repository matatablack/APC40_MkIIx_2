# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: C:\ProgramData\Ableton\Live 101 Suite\Resources\MIDI Remote Scripts\APC40_MkIIx\BankToggleComponent.py
# Compiled at: 2019-06-18 00:58:30
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ComboElement import ToggleElement
from _Framework.Control import ToggleButtonControl
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent

class BankToggleComponent(ControlSurfaceComponent):
    bank_toggle_button = ToggleButtonControl()

    def __init__(self, *a, **k):
        super(BankToggleComponent, self).__init__(*a, **k)
        self._toggle_elements = []

    @bank_toggle_button.toggled
    def bank_toggle_button(self, toggled, button):
        for e in self._toggle_elements:
            e.set_toggled(toggled)

    def create_toggle_element(self, *a, **k):
        element = ToggleElement(*a, **k)
        element.toggled = self.bank_toggle_button.is_toggled
        self._toggle_elements.append(element)
        return element