# [h] copy glyphs to mask

from vanilla import *
from AppKit import NSColor

def full_name(font):
    full_name = '%s %s' % (font.info.familyName, font.info.styleName)
    return full_name 

class copyToLayerDialog(object):

    _title = 'copy glyphs to background'
    _mark_color = (1, 0, 0, 1)
    _all_fonts_names = []
    _target_layer = 'background'

    def __init__(self, font):

        self._all_fonts = AllFonts()

        for f in self._all_fonts:
            self._all_fonts_names.append(full_name(f))

        self.w = FloatingWindow((190, 140), self._title, closable=False)
        # target layer
        self.w._target_label = TextBox((10, 10, -10, 17), "target font")
        self.w._target_value = PopUpButton((10, 35, -10, 20), self._all_fonts_names)
        # color
        self.w.mark_checkbox = CheckBox((10, 70, -10, 20), "mark glyphs", value=True)
        self.w.mark_color = ColorWell((120, 70, -13, 20), color=NSColor.colorWithCalibratedRed_green_blue_alpha_(*self._mark_color))
        # buttons
        self.w.button_apply = Button((10, -45, 80, 0), "apply", callback=self.apply_callback)
        self.w.button_close = Button((-90, -45, 80, 0), "close", callback=self.close_callback)
        self.w.open()

    def apply_callback(self, sender):

        self.font = CurrentFont()

        _layer_name = self._target_layer
        _target_font = self._all_fonts[self.w._target_value.get()]

        _mark = self.w.mark_checkbox.get()
        _mark_color = self.w.mark_color.get()
        _mark_color = (_mark_color.redComponent(), _mark_color.greenComponent(), _mark_color.blueComponent(), _mark_color.alphaComponent())

        print 'copying glyphs to mask...\n'
        print '\tsource font: %s (current layer)' % full_name(self.font)
        print '\ttarget font: %s (layer: %s)' % (full_name(_target_font), self._target_layer)
        print

        for gName in self.font.selection:
            print '\t%s' % gName,
            #self.font[gName].prepareUndo('copy glyph to mask')
            #f[gName].copyToLayer(_layer_name, clear=True)
            if _mark:
                _target_font[gName].mark = _mark_color
            #self.font[gName].performUndo()
            #self.font[gName].update()
        print
        print '\n...done.\n'

    def close_callback(self, sender):
        self.w.close()

f = CurrentFont()
copyToLayerDialog(f)

