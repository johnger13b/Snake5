# -*- coding: utf-8 -*-
# En ocasiones el widget TextInput muestra un error para
# solucionar instala xclip 
# $ sudo apt-get install xclip
import kivy
import os
import sqlite3

from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics","hight","640")

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label 
from kivy.uix.screenmanager import ScreenManager, Screen 
#from kivy.uix.screenmanager import FadeTransition
#from kivy.properties import StringProperty

def connect_to_database(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_usuario(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def create_table_usuario(cursor):
    cursor.execute(
        '''
        CREATE TABLE Usuario(
        Nombre    TEXT  PRIMARY KEY  NOT NULL,
        Telefono  INT                NOT NULL,
        EPS       TEXT               NOT NULL,
        Rh        TEXT               NOT NULL,  
        C_Emergencia      TEXT               NOT NULL,      
        T_emergencia      INT                NOT NULL,
        Correo      TEXT               NOT NULL, 
        Contraseña  TEXT               NOT NULL
        )'''
    )
    
class MainWid(ScreenManager):
    def __init__(self,**kwargs):
       super(MainWid,self).__init__()

        
       self.APP_PATH = os.getcwd()
       self.DB_PATH = self.APP_PATH+'/my_database.db'
        
       self.StartWid = StartWid(self)
       self.SosWid = SosWid(self)
       self.IniSecWid = IniSecWid(self)
       self.IniRegWid = IniRegWid(self)
       self.PriAuxWid = PriAuxWid(self)
       self.RutaSv_Wid = RutaSv_Wid(self)
       self.EventoWid = EventoWid(self)
       self.addEventoWid = addEventoWid(self)       
       self.ConsultaWid = ConsultaWid(self)
       self.HistorialWid = HistorialWid(self)       
       
       wid = Screen(name='start')
       wid.add_widget(self.StartWid)
       self.add_widget(wid)
       
       wid = Screen(name='sos')
       wid.add_widget(self.SosWid)
       self.add_widget(wid)  
       
       wid = Screen(name='inicio_sec')
       wid.add_widget(self.IniSecWid)
       self.add_widget(wid)   
       
       wid = Screen(name='inicio_reg')
       wid.add_widget(self.IniRegWid)
       self.add_widget(wid)        
       
       wid = Screen(name='P_aux')
       wid.add_widget(self.PriAuxWid)
       self.add_widget(wid)     
       
       wid = Screen(name='Ruta_SV')
       wid.add_widget(self.RutaSv_Wid)
       self.add_widget(wid)         
       
       wid = Screen(name='Eventos')
       wid.add_widget(self.EventoWid)
       self.add_widget(wid)     
       
       wid = Screen(name='addEvento')
       wid.add_widget(self.addEventoWid)
       self.add_widget(wid)    
       
       wid = Screen(name='consulta')
       wid.add_widget(self.ConsultaWid)
       self.add_widget(wid)    
       
       wid = Screen(name='Historia')
       wid.add_widget(self.HistorialWid)
       self.add_widget(wid)                                     
       
       self.goto_start()
       
    def goto_start(self):
        self.current = 'start'
        
    def goto_sos(self):
        self.current = 'sos'        
        
    def goto_inicio(self):
        self.current = 'inicio'  
        
    def goto_ini_seccion(self):
        self.current = 'inicio_sec'   
        
    def goto_ini_registro(self):
        self.current = 'inicio_reg'    
        
    def goto_P_aux(self):
        self.current = 'P_aux'        
        
    def goto_Ruta_SV(self):
        self.current = 'Ruta_SV'       
        
    def goto_Eventos(self):
        self.current = 'Eventos'     
        
    def goto_addEvento(self):
        self.current = 'addEvento'   
        
    def goto_consulta(self):
        self.current = 'consulta'     
        
    def goto_historia(self):
        self.current = 'Historia'                
                                                  
#-------------------------------------------------------------------        
class StartWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(StartWid,self).__init__()
        self.mainwid = mainwid
        
    def m_SOS(self):
        self.mainwid.goto_sos()   
        
    def inicio_seccion(self):
        self.mainwid.goto_ini_seccion()    
        
    def inicio_registro(self):
        self.mainwid.goto_ini_registro()             
#-------------------------------------------------------------------        
class SosWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(SosWid,self).__init__()
        self.mainwid = mainwid
            
    def P_aux(self):
        self.mainwid.goto_P_aux()  
        
    def Ruta_SV(self):
        self.mainwid.goto_Ruta_SV()          
        
    def m_INICIO(self):
        self.mainwid.goto_start()         
#-------------------------------------------------------------------
class IniSecWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(IniSecWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_start()  
        
    def Eventos(self):
        self.mainwid.goto_Eventos()         
        
#-------------------------------------------------------------------
class RutaSv_Wid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(RutaSv_Wid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_sos()         
#-------------------------------------------------------------------
class IniRegWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(IniRegWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_start()  
        
    def create_database(self):
        connect_to_database(self.mainwid.DB_PATH)
        
    def insert_data(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        d1 = self.ids.ti_nombre.text
        d2 = self.ids.ti_telefono.text
        d3 = self.ids.ti_EPS.text
        d4 = self.ids.ti_RH.text
        d5 = self.ids.ti_C_emergencia.text
        d6 = self.ids.ti_T_emergencia.text
        d7 = self.ids.ti_Correo.text
        d8 = self.ids.ti_Contrasena.text
        a1 = (d1,d2,d3,d4,d5,d6,d7,d8)
        s1 = 'INSERT INTO Productos(Nombre, Telefono, EPS, Rh, C_Emergencia, T_emergencia, Correo, Contraseña)'
        s2 = 'VALUES(%s,"%s","%s",%s,%s,"%s",%s,%s)' % a1
        try:
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            self.mainwid.goto_database()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

#-------------------------------------------------------------------
class PriAuxWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(PriAuxWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_sos()  
        
#-------------------------------------------------------------------
class EventoWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(EventoWid,self).__init__()
        self.mainwid = mainwid
        
    def add_Evento(self):
        self.mainwid.goto_addEvento()   
        
    def consulta(self):
        self.mainwid.goto_consulta()    
        
    def historia(self):
        self.mainwid.goto_historia()                      
        
    def m_INICIO(self):
        self.mainwid.goto_start()  
        
#-----------------------------------------------------------
class addEventoWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(addEventoWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_Eventos()    
        
#-----------------------------------------------------------
class ConsultaWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(ConsultaWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_Eventos()          

#-----------------------------------------------------------
class HistorialWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(HistorialWid,self).__init__()
        self.mainwid = mainwid
        
    def m_INICIO(self):
        self.mainwid.goto_Eventos()  
        

#-------------------------------------------------------------------
class MainApp(App):
    title = 'SnakeApp'
    def build(self):
        return MainWid()

#==================================================================
if __name__ == '__main__':
    MainApp().run()
    
    