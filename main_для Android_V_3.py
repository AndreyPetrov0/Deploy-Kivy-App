
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_string("""


<MenuScale>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        BoxLayout:
            scale_input: 0
            orientation: 'vertical'
            size_hint: .9, .9
            size: 300, 300
            padding: '20sp'
            spacing: '15sp'

            Label:
                text: 'Шкала приладу'
                font_size: '25sp'

            Button:
                text: '630 мм'
                font_size: '25sp'
                on_press: root.r_scale('71') 
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '900 мм'
                font_size: '25sp'
                on_press: root.r_scale('50') 
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '1000 мм'
                font_size: '25sp'
                on_press: root.r_scale('43')
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '1600 мм'
                font_size: '25sp'
                on_press: root.r_scale('28')
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '2000 мм'
                font_size: '25sp'
                on_press: root.r_scale('22')
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '2500 мм'
                font_size: '25sp'
                on_press: root.r_scale('18')
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'

            Button:
                text: '4000 мм'
                font_size: '25sp'
                on_press: root.r_scale('11')
                on_press: root.manager.current = 'CorrectionScreen'
                background_color: .95, .93, .22, 1
                background_normal: ''
                color: '#000000'


<CorrectionScreen>:
    correct_input: text_input

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.8, 0.5
            spacing: '25sp'

            Image:
                source: 'CorrectionScreen.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            TextInput:
                id: text_input
                multiline: False
                input_filter: 'int'
                font_size: '30sp'
                size_hint: 0.7, 0.4
                padding_x: 20, 20
                padding_y: 35, 20
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                hint_text: '0'

            Button:
                text: 'Прийняти'
                font_size: '20sp'
                size_hint: 0.7, 0.4
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.r_correct()
                on_press: root.manager.current = 'NumberScreen'

        


<NumberScreen>:
    number_input: text_input

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'


        BoxLayout:
            orientation: 'vertical'
            size_hint: .8, .5
            spacing: '25sp'

            Image:
                source: 'NumberScreen.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            TextInput:
                id: text_input
                multiline: False
                input_type: 'number'
                input_filter: 'int'
                font_size: '30sp'
                size_hint: 0.7, 0.4
                padding_x: 20, 20
                padding_y: 35, 20
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                hint_text: '0'

            Button:
                text: 'Прийняти'
                font_size: '20sp'
                size_hint: 0.7, 0.4
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.r_number()
                on_press: root.manager.current = 'CalculationScreen'




<CalculationScreen>:
    calc_result: calc_result

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        
        
        

        BoxLayout:
            orientation: 'vertical'
            size_hint: .8, .8
            padding: '90sp'
            spacing: '30sp'
            
            Label:
                text: 'Результат розрахунку введіть у датчик'
                font_size: '17sp'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                

            Label:
                id: calc_result
                text: '0'
                font_size: '40sp'
                size_hint: 1.1, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            Button:
                text: 'Розрахувати'
                font_size: '20sp'
                size_hint: 2.2, 1.5
                background_color: .14, .88, .61, 1
                background_normal: ''
                on_press: root.calculation()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            Button:
                text: 'Повернутись до меню'
                font_size: '18sp'
                size_hint: 2.2, 1.5
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.restart()
                on_press: root.manager.current = 'MenuScale'



""")

f = {'s': 0, 'c': 0, 'n': 0}
result = ''

def func(scale, correct, number):
    mg = 65535
    calc_corect = number + (correct * scale)

    if calc_corect < 0:
        return str(mg + calc_corect)

    if calc_corect > mg:
        return str(calc_corect - mg)

    else:
        return str(calc_corect)


class MenuScale(Screen):
    def r_scale(self, scale):
        f['s'] = int(scale)


class CorrectionScreen(Screen):
    def r_correct(self):
        try:
            f['c'] = int(self.correct_input.text)
        except:
            f['c'] = 0
        finally:
            self.correct_input.text = ''


class NumberScreen(Screen):
    def r_number(self):
        try:
            f['n'] = int(self.number_input.text)
        except:
            f['n'] = 0
        finally:
            self.number_input.text = ''


class CalculationScreen(Screen):
    def calculation(self):
        result = str(func(f['s'], f['c'], f['n']))
        self.calc_result.text = str(result)

    def restart(self):
        f['s'] = 0
        f['c'] = 0
        f['n'] = 0
        self.calc_result.text = '0'


class Level_SpotterApp(App):
    icon = 'icon.png'
    presplash = 'presplash.png'
    def build(self):
        
        al = AnchorLayout()

        sm = ScreenManager()
        sm.add_widget(MenuScale(name='MenuScale'))
        sm.add_widget(CorrectionScreen(name='CorrectionScreen'))
        sm.add_widget(NumberScreen(name='NumberScreen'))
        sm.add_widget(CalculationScreen(name='CalculationScreen'))

        al.add_widget(sm)
        return al


if __name__ == '__main__':
    Level_SpotterApp().run()