from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


KV = """
<Root>:
    orientation: "vertical"
    padding: dp(16)
    spacing: dp(12)

    Label:
        text: "Recycling App"
        font_size: '24sp'
        size_hint_y: None
        height: self.texture_size[1] + dp(8)
        halign: 'center'
        valign: 'middle'
        text_size: self.width, None

    Label:
        text: "This is a starter mobile UI built with Kivy."
        size_hint_y: None
        height: self.texture_size[1] + dp(8)
        halign: 'center'
        valign: 'middle'
        text_size: self.width, None

    Button:
        text: "Tap to do something"
        size_hint_y: None
        height: dp(48)
        on_release: app.on_primary_action()
"""


class Root(BoxLayout):
    pass


class RecyclingApp(App):
    def build(self):
        self.title = "Recycling App"
        Builder.load_string(KV)
        return Root()

    def on_primary_action(self):
        # Placeholder hook for your app logic. Replace with your own behavior.
        print("Primary action tapped")


if __name__ == "__main__":
    RecyclingApp().run()
