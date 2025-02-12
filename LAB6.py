# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: 'vertical'
    
    TextInput:
        id: result
        font_size: 32
        readonly: True
        halign: 'center'
        multiline: False
    
    GridLayout:
        cols: 4
        rows: 4
        
        Button:
            text: '7'
            on_press: result.text += self.text
        Button:
            text: '8'
            on_press: result.text += self.text
        Button:
            text: '9'
            on_press: result.text += self.text
        Button:
            text: '/'
            on_press: result.text += self.text
        
        Button:
            text: '4'
            on_press: result.text += self.text
        Button:
            text: '5'
            on_press: result.text += self.text
        Button:
            text: '6'
            on_press: result.text += self.text
        Button:
            text: '*'
            on_press: result.text += self.text
        
        Button:
            text: '1'
            on_press: result.text += self.text
        Button:
            text: '2'
            on_press: result.text += self.text
        Button:
            text: '3'
            on_press: result.text += self.text
        Button:
            text: '-'
            on_press: result.text += self.text
        
        Button:
            text: 'C'
            on_press: result.text = ''
        Button:
            text: '0'
            on_press: result.text += self.text
        Button:
            text: '='
            on_press: result.text = result.text + " = " + str(eval(result.text)) if result.text else ''
        Button:
            text: '+'
            on_press: result.text += self.text
"""

class CalculatorApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    CalculatorApp().run()
