import kivy
kivy.require('1.0.9')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

import os, socket, string, sys, tempfile, thread, time #, unittest
from M2Crypto import Rand, SSL, m2, Err


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    otherlabel_wid = ObjectProperty()
    info = StringProperty()
    moreinfo = StringProperty()
    
    #TODO some M2Crypto stuff that sets moreinfo
    self.moreinfo = 'Change to this'

    # handle button press
    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.otherlabel_wid.txt = self.moreinfo
        self.info = 'New info text'


class ControllerApp(App):
    def build(self):
        return Controller(info='Hello world')


if __name__ == '__main__':
    ControllerApp().run()
