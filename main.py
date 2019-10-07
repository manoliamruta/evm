from gpiozero import LED,Button,Buzzer
from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

def main():
    # Modify this if you have a different sized character LCD
    lcd_columns = 16
    lcd_rows = 2
    # Metro M0/M4 Pin Config:
    lcd_rs = digitalio.DigitalInOut(board.D26)
    lcd_en = digitalio.DigitalInOut(board.D19)
    lcd_d4 = digitalio.DigitalInOut(board.D13)
    lcd_d5 = digitalio.DigitalInOut(board.D6)
    lcd_d6 = digitalio.DigitalInOut(board.D5)
    lcd_d7 = digitalio.DigitalInOut(board.D21)
    lcd_backlight = digitalio.DigitalInOut(board.D2)

    # Initialise the LCD class
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                          lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    # Turn backlight on
    lcd.backlight = True
    lcd.cursor = False
    # Print a two line message
    lcd.message="e-voting machine\nusing RPi"
    # Wait 5s
    sleep(3)
    lcd.clear()
    
    but1 = Button(25)
    but2 = Button(24)
    but3 = Button(23)
    but4 = Button(3)
    led1 = LED(22)
    led2 = LED(27)
    led3 = LED(17)
    led4 = LED(18)
    buzz = Buzzer(2)    
    buzz.on()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    lcd.cursor_position(0, 0)
    lcd.message = "BJP-"
    lcd.cursor_position(4, 0)
    lcd.message = str(counter1)
    lcd.cursor_position(8, 0)
    lcd.message = "Cong-"
    lcd.cursor_position(13, 0)
    lcd.message = str(counter2)
    lcd.cursor_position(0, 1)
    lcd.message = "NDA-"
    lcd.cursor_position(4, 1)
    lcd.message = str(counter3)
    lcd.cursor_position(9, 1)
    lcd.message = "AAP-"
    lcd.cursor_position(13, 1)
    lcd.message = str(counter4)     
    while(True):
        if(but1.value):            
            led1.on()
            buzz.off()
            print('BJP')            
            counter1 = counter1 + 1
            lcd.cursor_position(0, 0)
            lcd.message = "BJP-"
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "Cong-"
            lcd.cursor_position(13, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "NDA-"
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(9, 1)
            lcd.message = "AAP-"
            lcd.cursor_position(13, 1)
            lcd.message = str(counter4)     
            print(counter1)
            sleep(3)
            led1.off()
            buzz.on()
        if(but2.value):            
            led2.on()
            buzz.off()
            print('Cong')        
            counter2 = counter2 + 1
            lcd.cursor_position(0, 0)
            lcd.message = "BJP-"
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "Cong-"
            lcd.cursor_position(13, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "NDA-"
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(9, 1)
            lcd.message = "AAP-"
            lcd.cursor_position(13, 1)
            lcd.message = str(counter4)     
            print(counter2)
            sleep(3)
            led2.off()
            buzz.on()
        if(but3.value):            
            led3.on()
            buzz.off()
            print('NDA')        
            counter3 = counter3 + 1
            lcd.cursor_position(0, 0)
            lcd.message = "BJP-"
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "Cong-"
            lcd.cursor_position(13, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "NDA-"
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(9, 1)
            lcd.message = "AAP-"
            lcd.cursor_position(13, 1)
            lcd.message = str(counter4)     
            print(counter3)
            sleep(3)
            led3.off()
            buzz.on()
        if(but4.value):            
            led4.on()
            buzz.off()
            print('AAP')        
            counter4 = counter4 + 1
            lcd.cursor_position(0, 0)
            lcd.message = "BJP-"
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "Cong-"
            lcd.cursor_position(13, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "NDA-"
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(9, 1)
            lcd.message = "AAP-"
            lcd.cursor_position(13, 1)
            lcd.message = str(counter4)     
            print(counter4)
            sleep(3)
            led4.off()
            buzz.on()
        
if __name__ == "__main__":
    main()
        