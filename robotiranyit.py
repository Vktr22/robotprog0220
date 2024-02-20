from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

class Robot():

    def __init__(self):
        # Create your objects here.
        self.ev3 = EV3Brick()
        # motorok kezelése
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)

        self.us = UltrasonicSensor(Port.S4)
        self.ts = TouchSensor(Port.S1)
        self.cs = ColorSensor(Port.S3)
        self.gs = GyroSensor(Port.S2)
        self.robot = DriveBase(self.jm, self.bm, 55, 142)

    def fordula(self):
        #mind2 motor azonos sebességgel megy - drivebase kell - turn fordulásra

        self.robot.turn(360)
        
        """self.robot.settings(2000, 100)   # Állítsuk be a robot sebességét és gyorsítását
        self.robot.turn(90)      # Fordítsuk jobbra a robotot
        time.sleep(3)          # Várjunk egy ideig, majd állítsuk le a robotot
        self.robot.stop()
        self.robot.drive(-100, 0)    # Mozgassuk hátra a robotot mindkét motorral azonos sebességgel
        time.sleep(3)          # Várjunk egy ideig, majd állítsuk le a robotot
        self.robot.stop()
        self.robot.turn(-90)     # Fordítsuk balra a robotot
        time.sleep(3)          # Várjunk egy ideig, majd állítsuk le a robotot
        self.robot.stop()
        """
        self.ev3.speaker.beep()

    def fordulb(self):
        #ellentetes iranyban mozognak a motorok - kulon kell a motorokat
        pass

    def fordulc(self):
        #egy iranyba mas sebesseggel mozognak a motorok - kulon kell a motorokat
        pass