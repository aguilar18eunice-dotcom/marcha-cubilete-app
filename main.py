# main.py - App Marcha Cubilete (versión mínima que compila)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (360, 640)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='MARCHA CUBILETE 2024', font_size=24))
        layout.add_widget(Label(text='Sistema de coordinación', font_size=16))
        btn = Button(text='ENTRAR AL SISTEMA', size_hint=(1, 0.2))
        btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(btn)
        self.add_widget(layout)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='MENÚ PRINCIPAL', font_size=20))
        
        menus = ['🗺️ MAPA EN VIVO', '👥 MI GRUPO', '💬 CHAT', '👤 MI PERFIL', '🚨 EMERGENCIA']
        for menu in menus:
            btn = Button(text=menu, size_hint=(1, 0.15))
            layout.add_widget(btn)
        
        btn_back = Button(text='← VOLVER', size_hint=(1, 0.1))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'login'))
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

class MarchaApp(App):
    def build(self):
        self.title = 'Marcha Cubilete 2024'
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MarchaApp().run()
