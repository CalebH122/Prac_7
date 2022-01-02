from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ['John', 'Sam', 'Jackson', 'David', 'Nathan', 'Jeff']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.add_labels()
        return self.root

    def add_labels(self):
        for name in self.name_list:
            button = Button(text=name)
            self.root.ids.main.add_widget(button)


DynamicLabels().run()
