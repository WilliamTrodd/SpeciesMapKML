#-------------------------------------------------------------------------------
# Name:        bat_map_gui_test
# Purpose:
#
# Author:      willi_000
#
# Created:     09/07/2018
# Copyright:   (c) willi_000 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

import openpyxl


class bat_map(App):

    def build(self):
        return file_loader()

    def mk_tbl(file_in, sheet):
        print(file_in, sheet)

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return

    def file_load(path):
        wb = openpyxl.load_workbook(path, data_only = True)
        return



class file_loader(GridLayout):

    def __init__(self, **kwargs):
        super(file_loader, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="File Path"))
        self.file_path = TextInput(multiline=False)

        next_button = Button(text = "File is okay?")

        next_button.bind(on_press = lambda x:(bat_map.file_load(self.file_path)))



class menu_screen(GridLayout):

    def __init__(self, **kwargs):
        super(menu_screen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="File Path"))
        self.file_path = TextInput(multiline=False)
        self.add_widget(self.file_path)
        self.add_widget(Label(text="Sheet Number"))
        self.sheet = TextInput(multiline=False)
        self.add_widget(self.sheet)

        make_maps = Button(text = "Make Maps!")

        make_maps.bind(on_press = lambda x:(bat_map.mk_tbl(self.file_path,self.sheet)))

        self.add_widget(make_maps)


if __name__ == '__main__':
    bat_map().run()

