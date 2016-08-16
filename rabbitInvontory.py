from piui import PiUi
import functools
import os
import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))

class Piui(object):

    def __init__(self):
        self.title = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))
        self.nameTxt = None
        self.breedTxt = None
        self.massTxt = None
        self.ageTxt = None
        self.doaTxt = None
        self.dodTxt = None
        self.genderTxt = None
        self.probelmTxt = None
        self.housingTxt = None
        self.BioTxt = None
        self.fixed = None
        self.litter = None
        self.adaptable = None

    def _toggle(self, what, value):
        if what == 'fixed':
            self.fixed = value
        if what == 'litter':
            self.litter = value
        if what == 'adaptable':
            self.adaptable = value

    def _add_bun_page(self):
        self.page = self.ui.new_ui_page(title="Add Bunny", prev_text="Back", onprevclick=self._main_menu_)
        self.title = self.page.add_textbox("Name:", 'h1')
        self.nameTxt = self.page.add_input('text')
        self.title = self.page.add_textbox('Breed:', 'h1')
        self.breedTxt = self.page.add_input('text')
        self.title = self.page.add_textbox('Weight(lbs):', 'h1')
        self.massTxt = self.page.add_input('text')
        self.title = self.page.add_textbox('Age(years):', 'h1')
        self.ageTxt = self.page.add_input('text')
        self.title = self.page.add_textbox('Day of Arrival:', 'h1')
        self.doaTxt = self.page.add_input('text')
        self.title = self.page.add_textbox('Gender:', 'h1')
        self.genderTxt = self.page.add_input('text')
        self.list = self.page.add_list()
        self.list.add_item('Fixed:', chevron=False, toggle=True, ontoggle=functools.partial(self._toggle, 'fixed'))
        self.list.add_item('Litter box Trained:', chevron=False, toggle=True, ontoggle=functools.partial(self._toggle,
                                                                                                         'litter'))
        self.list.add_item('Adaptable:', chevron=False, toggle=True, ontoggle=functools.partial(self._toggle,
                                                                                                'adaptable'))
        self.title = self.page.add_textbox('Bio:', 'h1')
        self.BioTxt = self.page.add_input('text')

    def _main_menu_(self):
        self.page = self.ui.new_ui_page(title='Rabbit Inventory')
        self.list = self.page.add_list()
        self.list.add_item('Add Bunny', chevron=True, onclick=self._add_bun_page)
        self.ui.done()

    def _main_(self):
        self._main_menu_()
        self.ui.done()


def _main_():
    piui = Piui()
    piui._main_()


_main_()
