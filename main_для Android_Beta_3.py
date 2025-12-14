from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.core.text import LabelBase

from kivy.properties import StringProperty

# --‐-------- прозрачная панель
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform
# ----------'

Builder.load_string("""

<MenuScaleScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
        size_hint: None, None
        size: '400px', '4500px'
        
        
        BoxLayout:
            orientation: 'vertical'
            position: 'center'
            size_hint: None, None
            size: '2000px', '4500px'  
            
            Image:
                source: 'metal-2.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: '2000px', '4500px'
        
        BoxLayout:
        # layout для бордера кнопак шкалы
            orientation: 'vertical'
            padding: '-7px'
            spacing: '35px'
            position: 'center'  
            size_hint: None, None
            size: '400px', '2950px'
            
            MenuButton_border:

            MenuButton_border:

            MenuButton_border:

            MenuButton_border:

            MenuButton_border:

            MenuButton_border:
    
            MenuButton_border:

        
        
        BoxLayout:
            scale_input: 0
            orientation: 'vertical'
            padding: '50px'
            spacing: '50px'
            position: 'center'  
            size_hint: None, None
            size: '900px', '3000px'
           
            Label:
          #      font_name: 'Montserrat-BoldItalic.ttf'
                text: 'Шкала приладу'
                font_size: '85px'
                size_hint: None, None
                size: '800px', '200px'
                italic: True
                color: (1, 1, 1, 1)
                background_color: (0, 0, 0, 0.3)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]
                
            MenuButton:
                text: '± 315 мм | 630 мм'
                on_press: root.enter_scale('71', 'Шкала приладу: ± 315 мм | 630 мм') 
                on_press: root.manager.current = 'CorrectionScreen'             
                
            MenuButton:
                text: '900 мм'
                on_press: root.enter_scale('50', 'Шкала приладу: 900 мм') 
                on_press: root.manager.current = 'CorrectionScreen'
                
            MenuButton:
                text: '1000 мм'
                on_press: root.enter_scale('43', 'Шкала приладу: 1000 мм')
                on_press: root.manager.current = 'CorrectionScreen'
            
            MenuButton:
                text: '1600 мм'
                on_press: root.enter_scale('28', 'Шкала приладу: 1600 мм')
                on_press: root.manager.current = 'CorrectionScreen' 

            MenuButton:
                text: '2000 мм'
                on_press: root.enter_scale('22', 'Шкала приладу: 2000 мм')
                on_press: root.manager.current = 'CorrectionScreen'

            MenuButton:
                text: '2500 мм'
                on_press: root.enter_scale('18', 'Шкала приладу: 2500 мм')
                on_press: root.manager.current = 'CorrectionScreen'

            MenuButton:
                text: '4000 мм'
                on_press: root.enter_scale('11', 'Шкала приладу: 4000 мм')
                on_press: root.manager.current = 'CorrectionScreen'
           

<MenuButton@Button>:
  #  font_name: 'CustomFontName'
    font_size: '70px'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.95, .93, .22, 1) 
    color: '#000000' 
    size_hint: None, None
    size: '750px', '145px'
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: (.95, .93, .22, 1) if self.state=='normal' else (.53,100,.8,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [45, 2, 45, 2]


<MenuButton_border@Button>:
    font_size: '70px'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.95, .93, .22, 1) 
    color: '#000000' 
    size_hint: None, None
    size: '765px', '160px'
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: (.0, .0, .0, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [45, 2, 45, 2]
     
 

# -------------------- ВВОД ЧИСЛА ДЛЯ КОРЕКТИРОВКИ -------------
<CorrectionScreen>:
    correct_input: value
    value_correct: value
    image: image_widget

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '600px', '4500px'
        

        # Основной слой
        BoxLayout:
            orientation: 'vertical'
            position: 'center'
            size_hint: None, None
            size: '2000px', '4500px'  
            
            Image:
                source: 'metal-2.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: '2000px', '4500px'
     

        # Слой картинки для надписи
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '400px', '1800px'

            Image:
                source: 'CorrectionScreen.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '900px', '550px'
                background_color: (0, 0, 0, 0.3)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]
   

        # Слой надписи для картинки
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '420px', '1730px'
            
            Label:
       #         font_name: 'Montserrat-BoldItalic.ttf'
                text: 'Введіть значення на яке буде скоригований прилад'
                color: (1, 1, 1, 1)
                font_size: '19sp'
                halign: 'center'
                valign: 'middle'
                text_size: (750, None)
                size_hint: (None, None)
                size: (400, 200)


        # Слой фона инпута
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '731px', '2070px'
            
            Label:
       #         font_name: 'Montserrat-BoldItalic.ttf'
                text: 'мм'
                color: (215, 55, 72, 1)
                font_size: '22sp'
                halign: 'right'
                valign: 'middle'
                text_size: (540, None)
                size_hint: (None, None)
                size: (700, 170)
                background_color: (0, 0, 0, 0.5)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]    
        

        # Слой инпута 
        BoxLayout:
            orientation: 'horizontal'
            padding: '12px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '550px', '3950px'
            
            Image:
                id: image_widget
                source: root.image_source 
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '100px', '100px'
            
            TextInput:
   #             font_name: 'Montserrat-Bold.ttf'
                id: value
                multiline: False
                readonly: True
                font_size: '100px'
                padding_x: '10px', '10px'
                padding_y: '1px', '1px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                hint_text: '0'
                size_hint: None, None
                size: '300px', '130px'
                background_color: (0, 0, 0, 0)
                foreground_color: (0, 1, 0, 1)
                halign: 'center'
          
               
        # layout для боредра
        BoxLayout:   
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
            size_hint: None, None
            size: '725px', '4520px'
            spacing: '1px'

            BACK_border:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '359px', '155px'

            ENTER_border:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '359px', '155px'    
         
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
            size_hint: None, None
            size: '710px', '4520px'
            spacing: '5px'

            BACK:
                text: 'Назад'
                font_size: '50px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'MenuScaleScreen'
                size_hint: None, None
                size: '350px', '140px'

            ENTER:
                text: 'Прийняти'
                font_size: '50px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.enter_correct()
                on_press: root.manager.current = 'NumberScreen'
                size_hint: None, None
                size: '350px', '140px'       
        

        # layout для бордера
        GridLayout:     
            cols: 3
            rows: 4  
            size_hint: None, None
            size: '750px', '10px'       
            padding: '-35px', '2395px'
            spacing: '15px'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:
 
            ModNumberBotton_border:
    
            ModNumberBotton_border:
  
            ModNumberBotton_border:

            ModNumberBotton_border:
    
            ModNumberBotton_border:
     
    
        GridLayout:
            cols: 3
            rows: 4  
            size_hint: None, None
            size: '810px', '10px'       
            padding: '0px', '2400px'
            spacing: '25px'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            ModNumberBotton:
                text: '1'
                on_press: root.change_image()
                on_press: root.on_button_press('1')
                on_press: root.change_image()

            ModNumberBotton:
                text: '2'
                on_press: root.change_image()
                on_press: root.on_button_press('2')
                on_press: root.change_image()

            ModNumberBotton:
                text: '3'
                on_press: root.change_image()
                on_press: root.on_button_press('3')
                on_press: root.change_image()

            ModNumberBotton:
                text: '4'
                on_press: root.change_image()
                on_press: root.on_button_press('4')
                on_press: root.change_image()

            ModNumberBotton:
                text: '5'
                on_press: root.change_image()
                on_press: root.on_button_press('5')
                on_press: root.change_image()

            ModNumberBotton:
                text: '6'
                on_press: root.change_image()
                on_press: root.on_button_press('6')
                on_press: root.change_image()

            ModNumberBotton:
                text: '7'
                on_press: root.change_image()
                on_press: root.on_button_press('7')
                on_press: root.change_image()

            ModNumberBotton:
                text: '8'
                on_press: root.change_image()
                on_press: root.on_button_press('8')
                on_press: root.change_image()

            ModNumberBotton:
                text: '9'
                on_press: root.change_image()
                on_press: root.on_button_press('9')
                on_press: root.change_image()

            ModNumberBotton:
                font_size: '90px'
                text: '-'
                on_press: root.change_image()
                on_press: root.on_button_press('-')
                on_press: root.change_image()

            ModNumberBotton:
                text: '0'
                on_press: root.on_button_press('0')
              
            ModNumberBotton:
                font_size: '60px'
                text: '<'
                on_press: root.change_image()
                on_press: root.on_button_press('<')
                on_press: root.change_image()
                

<ModNumberBotton@Button>:
 #   font_name: 'CustomFontName'
  #  font_name: 'Montserrat-Bold.ttf'
    size_hint: None, None
    size: '250px', '140px'
    font_size: '60px'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.21, .2, .35, 1) 
    color: '#000000' 
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: (.9, .8, .4, 1.2) if self.state=='normal' else (0,.7,.7,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [42]


<ModNumberBotton_border@Button>:
    size_hint: None, None
    size: '260px', '150px'
    font_size: '55px'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.21, .2, .35, 1) 
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    canvas.before:
        Color:
            rgba: (.0, .0, .0, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [42]
            

<ENTER@Button>:
#    font_name: 'CustomFontName'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.25, .40, .82, 1) 
    canvas.before:
        Color:
            rgba: (.25, .40, .82, 1) if self.state=='normal' else (0,0,.70,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [0, 40, 40, 0]

<BACK@Button>:
#    font_name: 'CustomFontName'
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.25, .40, .82, 1) 
    canvas.before:
        Color:
            rgba: (.25, .40, .82, 1) if self.state=='normal' else (0,0,.70,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [40, 0, 0, 40]
            

<ENTER_border@Button>:
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.25, .40, .82, 1) 
    canvas.before:
        Color:
            rgba: (.0, .0, .0, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [0, 45, 45, 0]

<BACK_border@Button>:
    background_color: (0, 0, 0, 0)
    background_normal: ''
    back_color: (.25, .40, .82, 1) 
    canvas.before:
        Color:
            rgba: (.0, .0, .0, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [45, 0, 0, 45]



# -------------------- ВВОД ЧИСЛА С ДАТЧИКА -------------
<NumberScreen>:
    number_input: value
    value_number: value

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '600px', '4500px'

        BoxLayout:
            orientation: 'vertical'
            position: 'center'
            size_hint: None, None
            size: '2000px', '4500px'  
            
            Image:
                source: 'metal-2.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: '2000px', '4500px'

        
        # Слой картинки для надписи
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '400px', '1800px'

            Image:
                source: 'NumberScreen.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '900px', '550px'
                background_color: (0, 0, 0, 0.3)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]


        # Слой надписи для картинки
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '420px', '1730px'
            
            Label:
      #          font_name: 'Montserrat-BoldItalic.ttf'
                text: 'Введіть значення на дисплею датчика в пункті 2.6.1'
                color: (1, 1, 1, 1)
                font_size: '19sp'
                halign: 'center'
                valign: 'middle'
                text_size: (750, None)
                size_hint: (None, None)
                size: (400, 200)


        # Слой фона инпута
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '731px', '2070px'
            
            Label:
      #          font_name: 'Montserrat-BoldItalic.ttf'
                text: ''
                color: (215, 55, 72, 1)
                font_size: '22sp'
                halign: 'right'
                valign: 'middle'
                text_size: (540, None)
                size_hint: (None, None)
                size: (700, 170)
                background_color: (0, 0, 0, 0.5)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]   
        

        # Слой инпута 
        BoxLayout:
            orientation: 'horizontal'
            padding: '97px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '550px', '3950px'

            TextInput:
    #            font_name: 'Montserrat-Bold.ttf'
                id: value
                multiline: False
                readonly: True
                font_size: '100px'
                padding_x: '10px', '10px'
                padding_y: '1px', '1px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                hint_text: '0'
                size_hint: None, None
                size: '350px', '130px'
                background_color: (0, 0, 0, 0)
                foreground_color: (0, 1, 0, 1)
                halign: 'center'


        # layout для боредра
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
            size_hint: None, None
            size: '725px', '4520px'
            spacing: '1px'

            BACK_border:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '359px', '155px'

            ENTER_border:
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '359px', '155px'    
         
         
        BoxLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
            size_hint: None, None
            size: '710px', '4520px'
            spacing: '5px'

            BACK:
                text: 'Назад'
                font_size: '50px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'CorrectionScreen'
                size_hint: None, None
                size: '350px', '140px'

            ENTER:
                text: 'Прийняти'
                font_size: '50px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.enter_number()
                on_press: root.manager.current = 'CalculationScreen'
                size_hint: None, None
                size: '350px', '140px'        

        GridLayout:
        # layout для бордера
            cols: 3
            rows: 4  
            size_hint: None, None
            size: '750px', '10px'       
            padding: '-35px', '2395px'
            spacing: '15px'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            ModNumberBotton_border:

            ModNumberBotton_border:

            ModNumberBotton_border:
            
            ModNumberBotton_border:
               
            ModNumberBotton_border:
               
            ModNumberBotton_border:
               
            ModNumberBotton_border:

            ModNumberBotton_border:
               
            ModNumberBotton_border:
                
            ModNumberBotton_border:
        
            ModNumberBotton_border:
     
            ModNumberBotton_border:
          
    
        GridLayout:
            cols: 3
            rows: 4  
            size_hint: None, None
            size: '810px', '10px'       
            padding: '0px', '2400px'
            spacing: '25px'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            ModNumberBotton:
                text: '1'
                on_press: root.on_button_press('1')

            ModNumberBotton:
                text: '2'
                on_press: root.on_button_press('2')

            ModNumberBotton:
                text: '3'
                on_press: root.on_button_press('3')

            ModNumberBotton:
                text: '4'
                on_press: root.on_button_press('4')

            ModNumberBotton:
                text: '5'
                on_press: root.on_button_press('5')

            ModNumberBotton:
                text: '6'
                on_press: root.on_button_press('6')

            ModNumberBotton:
                text: '7'
                on_press: root.on_button_press('7')

            ModNumberBotton:
                text: '8'
                on_press: root.on_button_press('8')

            ModNumberBotton:
                text: '9'
                on_press: root.on_button_press('9')

            ModNumberBotton:
                text: 'C'
                on_press: root.on_button_press('C')

            ModNumberBotton:
                text: '0'
                on_press: root.on_button_press('0')

            ModNumberBotton:
                font_size: '60px'
                text: '<'
                on_press: root.on_button_press('<')





<CalculationScreen>:
    calc_result: calc_result
    name_scale: name_scale
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '400px', '4500px'        
        
        BoxLayout:
            orientation: 'vertical'
            position: 'center'
            size_hint: None, None
            size: '2000px', '4500px'  
            
            Image:
                source: 'metal-2.jpg'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: '2000px', '4500px'
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: '400px', '2450px'
            spacing: '100px'
            
            Image:
                source: 'Last.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '650px', '650px'       

    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '400px', '1800px'
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: '800px', '440px'
            spacing: '100px'
            
            Image:
                source: 'CalculationScreen.png'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '870px', '280px'
                background_color: (0, 0, 0, 0.3)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [60]
                        
            Label
                id: name_scale
                font_size: '60px'
                text: ''
                size_hint: None, None
                size: '800px', '120px'
                italic: True
                
        BoxLayout:
            orientation: 'vertical'
            padding: '10px', '10px'
            spacing: '10px'
            position: 'center'  
            size_hint: None, None
            size: '420px', '190px'
            
            Label:
    #            font_name: 'Montserrat-BoldItalic.ttf'
                text: 'Результат розрахунку введіть у датчик'
                color: (1, 1, 1, 1)
                font_size: '20sp'
                halign: 'center'
                valign: 'middle'
                text_size: (750, None)
                size_hint: (None, None)
                size: (400, 200)
                
	AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '338px', '500px'
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: '310px', '360px'
            spacing: '15px'
            
            Label:
                id: calc_result
                text: '0'
                color: '#4CFF38' 
                font_size: '160px'
                size_hint: None, None
                size: '310px', '420px'
               
                
	AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5} 
        size_hint: None, None
        size: '400px', '300px'
        
        
        BoxLayout:
        # layout для бордера
            orientation: 'vertical'
            size_hint: None, None
            size: '400px', '907px'
            spacing: '65px'
            
            Button: 
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '515px', '160px'
                background_color: (0, 0, 0, 0)
                background_normal: ''
                back_color: (.0,.0,.0,1) 
                canvas.before:
                    Color:
                        rgba: self.back_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [38]
                        
            Button: 
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '515px', '160px'
                background_color: (0, 0, 0, 0)
                background_normal: ''
                back_color: (.0,.0,.0,1) 
                canvas.before:
                    Color:
                        rgba: self.back_color
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [38]
        
        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: '400px', '900px'
            spacing: '80px'
            
            Button:
  #              font_name: 'CustomFontName'
                text: 'Розрахувати'
                font_size: '55px'
                on_press: root.calculation()
                color: '#000000'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: '500px', '145px'
                background_color: (0, 0, 0, 0)
                background_normal: ''
                back_color: (.30,100,.22,1) 
                canvas.before:
                    Color:
                        rgba: self.back_color if self.state=='normal' else (.21,.59,.24,1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [35]
            
            
            Button:
 #               font_name: 'CustomFontName'
                text: 'Шкала приладу'
                font_size: '50px'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.restart()
                on_press: root.manager.current = 'MenuScaleScreen'
                size_hint: None, None
                size: '500px', '145px'
                background_color: (0, 0, 0, 0)
                background_normal: ''
                back_color: (.25, .40, .82, 1) 
                canvas.before:
                    Color:
                        rgba: self.back_color if self.state=='normal' else (0,0,.70,1)
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [35]
              

""")

cache = {'scale_value': 0, 'correct_value': 0, 'number_value': 0, 'name_scale': ''}
result = ''

def func_calc(scale, correct, number):
    mg = 65535
    calc_correct = number + (correct * scale)
    if calc_correct < 0:
        return str(mg + calc_correct)
    if calc_correct > mg:
        return str(calc_correct - mg)
    else:
        return str(calc_correct)


class MenuScaleScreen(Screen):
    def enter_scale(self, scale, name_scale):
        cache['scale_value'] = int(scale)
        cache['name_scale'] = str(name_scale)
       

class CorrectionScreen(Screen):

    #-------------------
    # Определите свойство для картинки, чтобы оно могло меняться через KV
    image_source = StringProperty('D_1.png') 

    def change_image(self):
        # Логика смены картинки
        if len(self.value_correct.text) != 0:
            if self.value_correct.text[0] == '+':
                self.image_source = 'Up.png'      
            else:
                self.image_source = 'Down.png'
        else:
            self.image_source = 'D_1.png'
    #-------------------

    max_len = 3
    def enter_correct(self):
        try:
            cache['correct_value'] = int(self.correct_input.text)
        except:
            cache['correct_value'] = 0
        finally:
            self.correct_input.text = ''
            self.max_len = 3

    def on_button_press(self, number):
        if number == '-':
                if len(self.value_correct.text) != 0:
                    if self.value_correct.text[0] == '+':
                        self.value_correct.text = self.value_correct.text[1:]
                if len(self.value_correct.text) == 0:
                    self.value_correct.text += number
                    self.max_len = 4
                elif self.value_correct.text[0] == '-':
                    self.value_correct.text = self.value_correct.text[1:]
                    self.max_len = 3
                elif self.value_correct.text[0] == '0':
                    self.value_correct.text = '-'
                    self.max_len = 4
                else:                  
                    self.value_correct.text = '-' + self.value_correct.text[:]
                    self.max_len = 4

        elif number == '<':
            self.value_correct.text = self.value_correct.text[:-1]
            if len(self.value_correct.text) == 0:
                self.max_len = 3

        elif len(self.value_correct.text) < self.max_len:
            self.value_correct.text += number
            if number == '0':
                if len(self.value_correct.text) == 0:
                    self.value_correct.text += number
                elif self.value_correct.text[0] == '0':
                    self.value_correct.text = '0'
                elif self.value_correct.text[0] == '-' and self.value_correct.text[1] == '0':
                    self.value_correct.text = self.value_correct.text[:-1]
                elif self.value_correct.text[0] == '+' and self.value_correct.text[1] == '0':
                    self.value_correct.text = self.value_correct.text[:-1]
            else:
                if self.value_correct.text[0] == '0':
                    self.value_correct.text = self.value_correct.text[1:]

        if len(self.value_correct.text) != 0:
            if self.value_correct.text[0] != '+' and self.value_correct.text[0] != '-':
                if int(self.value_correct.text) > 0:
                    self.max_len = 4
                    self.value_correct.text = '+' + self.value_correct.text
 
           
class NumberScreen(Screen):
    def enter_number(self):
        try:
            cache['number_value'] = int(self.number_input.text)
        except:
            cache['number_value'] = 0
        finally:
            self.number_input.text = ''

    def on_button_press(self, number):
        if number == '<':
            self.value_number.text = self.value_number.text[:-1]
        elif number == 'C':
            self.value_number.text = ''

        elif len(self.value_number.text) < 5:
            self.value_number.text += number
            if number == '0':
                if len(self.value_number.text) == 0:
                    self.value_number.text += number
                elif self.value_number.text[0] == '0':
                    self.value_number.text = '0'
                elif self.value_number.text[0] == '-' and self.value_number.text[1] == '0':
                    self.value_number.text = self.value_number.text[:-1]
            else:
                if self.value_number.text[0] == '0':
                    self.value_number.text = self.value_number.text[1:]


class CalculationScreen(Screen):
    def calculation(self):
        result = str(func_calc(
            cache['scale_value'], 
            cache['correct_value'], 
            cache['number_value']))
        self.calc_result.text = str(result)
        self.name_scale.text = cache['name_scale']

    def restart(self):
        cache['scale_value'] = 0
        cache['correct_value'] = 0
        cache['number_value'] = 0
        self.calc_result.text = '0'
        self.name_scale.text = ''

#LabelBase.register(name="CustomFontName", 
 #                  fn_regular="Montserrat-Medium.ttf")




def hide_status_bar():
    # функция для прозрачной панели снизу и сверху
    if platform == 'android':
        from jnius import autoclass, cast
        from android.runnable import run_on_ui_thread
        
        Color = autoclass("android.graphics.Color")
        WindowManager = autoclass('android.view.WindowManager$LayoutParams')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity


        @run_on_ui_thread
        def _hide_status_bar(color):
            window = activity.getWindow()
            window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
            window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
            window.setStatusBarColor(Color.parseColor(color)) 
            window.setNavigationBarColor(Color.parseColor(color))

        _hide_status_bar('#000000ff')


class Level_SpotterApp(App):
    #Main class
    def build(self):
        hide_status_bar() # запуск функции для скрытия панели
        
        al = AnchorLayout()
        
        sm = ScreenManager(transition=FadeTransition(duration='0.1'))
        sm.add_widget(MenuScaleScreen(name='MenuScaleScreen'))
        sm.add_widget(CorrectionScreen(name='CorrectionScreen'))
        sm.add_widget(NumberScreen(name='NumberScreen'))
        sm.add_widget(CalculationScreen(name='CalculationScreen'))

        al.add_widget(sm)
        return al


if __name__ == '__main__':
    Level_SpotterApp().run()