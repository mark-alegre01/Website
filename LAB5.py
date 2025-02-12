from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

class MyGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Task 1: Number Guessing Game
        self.correct_number = 7
        self.add_widget(Label(text="Choose a number between 1 and 10:"))
        self.guess_input = TextInput(multiline=False)
        self.add_widget(self.guess_input)
        self.guess_button = Button(text="Check Guess")
        self.guess_button.bind(on_press=self.check_guess)
        self.add_widget(self.guess_button)
        self.guess_result = Label(text="")
        self.add_widget(self.guess_result)
        
        # Task 2: Word Count
        self.add_widget(Label(text="Enter a sentence:"))
        self.sentence_input = TextInput(multiline=False)
        self.add_widget(self.sentence_input)
        self.word_count_button = Button(text="Count Words")
        self.word_count_button.bind(on_press=self.count_words)
        self.add_widget(self.word_count_button)
        self.word_count_result = Label(text="")
        self.add_widget(self.word_count_result)
        
        # Task 3: Sum and Average
        self.add_widget(Label(text="Enter two numbers:"))
        self.num1_input = TextInput(multiline=False)
        self.num2_input = TextInput(multiline=False)
        self.add_widget(self.num1_input)
        self.add_widget(self.num2_input)
        self.calc_button = Button(text="Calculate Sum & Average")
        self.calc_button.bind(on_press=self.calculate_sum_avg)
        self.add_widget(self.calc_button)
        self.calc_result = Label(text="")
        self.add_widget(self.calc_result)
        
        # Task 4: Triangle Perimeter & Area
        self.add_widget(Label(text="Enter three sides of a triangle:"))
        self.side1_input = TextInput(multiline=False)
        self.side2_input = TextInput(multiline=False)
        self.side3_input = TextInput(multiline=False)
        self.add_widget(self.side1_input)
        self.add_widget(self.side2_input)
        self.add_widget(self.side3_input)
        self.triangle_button = Button(text="Calculate Perimeter & Area")
        self.triangle_button.bind(on_press=self.calculate_triangle)
        self.add_widget(self.triangle_button)
        self.triangle_result = Label(text="")
        self.add_widget(self.triangle_result)
        
    def check_guess(self, instance):
        guess = self.guess_input.text
        if guess.isdigit() and int(guess) == self.correct_number:
            self.guess_result.text = "Correct!"
        else:
            self.guess_result.text = "Incorrect! Try again."
    
    def count_words(self, instance):
        sentence = self.sentence_input.text.strip()
        word_count = len(sentence.split()) if sentence else 0
        self.word_count_result.text = f"Word Count: {word_count}"
    
    def calculate_sum_avg(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            total = num1 + num2
            avg = total / 2
            self.calc_result.text = f"Sum: {total}, Average: {avg:.2f}"
        except ValueError:
            self.calc_result.text = "Invalid input! Enter numbers."
    
    def calculate_triangle(self, instance):
        try:
            a = float(self.side1_input.text)
            b = float(self.side2_input.text)
            c = float(self.side3_input.text)
            perimeter = a + b + c
            s = perimeter / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            self.triangle_result.text = f"Perimeter: {perimeter}, Area: {area:.2f}"
        except ValueError:
            self.triangle_result.text = "Invalid input! Enter numbers."
        except:
            self.triangle_result.text = "Invalid triangle sides!"

class MyApp(App):
    def build(self):
        return MyGUI()

if __name__ == "__main__":
    MyApp().run()
