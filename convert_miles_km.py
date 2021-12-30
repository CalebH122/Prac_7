from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Convertor(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (700, 280)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_add(self, number):
        try:
            result = int(number) + 1
            self.root.ids.input_number.text = str(result)
            self.root.ids.output_number.text = str(result * 1.609)
        except ValueError:
            new_number = 0 + 1
            self.root.ids.input_number.text = str(new_number)
            self.root.ids.output_number.text = str(new_number * 1.609)

    def handle_minus(self, number):
        try:
            result = int(number) - 1
            self.root.ids.input_number.text = str(result)
            self.root.ids.output_number.text = str(result * 1.609)
        except ValueError:
            new_number = 0 - 1
            self.root.ids.input_number.text = str(new_number)
            self.root.ids.output_number.text = str(new_number * 1.609)

    def convert_mkm(self, meter):
        try:
            km = int(meter) * 1.609
            self.root.ids.output_number.text = str(km)
        except ValueError:
            self.root.ids.input_number.text = str(0)


Convertor().run()
