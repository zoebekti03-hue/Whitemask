from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Setting warna dasar Red Hood
BLACK = get_color_from_hex('#050505')
RED = get_color_from_hex('#FF0000')
DARK_RED = get_color_from_hex('#800000')

class WhitemaskApp(App):
    def build(self):
        # Layout Utama
        self.root = BoxLayout(orientation='vertical', spacing=10, padding=20)
        Window.clearcolor = BLACK

        # Header
        header = Label(
            text='WHITEMASK HQ',
            font_size='32sp',
            bold=True,
            color=RED,
            size_hint_y=None,
            height=100
        )
        self.root.add_widget(header)

        # Navigasi Simpel
        nav = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_jadwal = Button(text='SCHEDULE', background_color=DARK_RED)
        btn_intel = Button(text='INTEL', background_color=DARK_RED)
        nav.add_widget(btn_jadwal)
        nav.add_widget(btn_intel)
        self.root.add_widget(nav)

        # Area Konten (Scrollable)
        self.scroll = ScrollView()
        self.content_area = BoxLayout(orientation='vertical', size_hint_y=None, spacing=15)
        self.content_area.bind(minimum_height=self.content_area.setter('height'))
        
        # Default View: Jadwal
        self.show_jadwal()
        
        self.scroll.add_widget(self.content_area)
        self.root.add_widget(self.scroll)

        # Event Button
        btn_jadwal.bind(on_press=self.show_jadwal)
        btn_intel.bind(on_press=self.show_intel)

        return self.root

    def show_jadwal(self, *args):
        self.content_area.clear_widgets()
        jadwal = [
            ("SELASA", "Matematika (MTK)"),
            ("RABU", "Belajar HTML (Coding)"),
            ("KAMIS", "Bahasa Inggris"),
            ("SABTU", "Ekonomi (Mission Active)")
        ]
        for hari, mapel in jadwal:
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=80, padding=10)
            card.add_widget(Label(text=hari, color=RED, bold=True, halign='left'))
            card.add_widget(Label(text=mapel, font_size='18sp'))
            self.content_area.add_widget(card)

    def show_intel(self, *args):
        self.content_area.clear_widgets()
        intel_data = [
            ("INFLASI", "Terlalu banyak uang beredar = Harga Naik."),
            ("BANK SENTRAL", "Pengontrol bunga & cetak uang."),
            ("PERURI", "Pabrik pencetak uang resmi RI.")
        ]
        for topik, isi in intel_data:
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=100, padding=10)
            card.add_widget(Label(text=topik, color=RED, bold=True))
            l = Label(text=isi, text_size=(Window.width - 40, None), halign='center')
            card.add_widget(l)
            self.content_area.add_widget(card)

if __name__ == '__main__':
    WhitemaskApp().run()
