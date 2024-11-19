from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ Simple app to dynamically create labels for each name """

    def build(self):
        names = ["Harry", "John", "Michael", "Diana", "Dallas"]
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in names:
            label = self.create_label(name)
            self.root.ids.labels_box.add_widget(label)

        return self.root

    def create_label(self, name):
        label = Label(text=name, font_size=32)
        return label


if __name__ == "__main__":
    DynamicLabelsApp().run()
