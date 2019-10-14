from gpiozero import LED,Button,Buzzer
from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import tkinter

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
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    
    root = tkinter.Tk()
    root.geometry("665x500+300+200")
    root.title('evm')
    root.configure(borderwidth="1")
    root.configure(relief="sunken")
    root.configure(background="#ffffff")
    root.configure(cursor="arrow")
    root.configure(highlightbackground="#d9d9d9")
    root.configure(highlightcolor="black")
    w1 = tkinter.Label(root, text="e-voting machine using RPi!", font=("Arial Bold", 22), bg='#ffffff', fg='#000066')
    w1.grid(row=0,column=1)
    
    Label1 = tkinter.Label(root)
    _img1 = tkinter.PhotoImage(file="/home/pi/evm/nps.png")
    Label1.configure(image=_img1)
    Label1.configure(background='#ffffff')
    Label1.configure(text='''Label''')
    Label1.grid(row=1,column=1)
    
    
    m = tkinter.Label(root, text="Teams", font=("Arial Bold", 20), bg='#ffffff', fg='#800000', justify='right')
    l = tkinter.Label(root, text="Votes", font=("Arial Bold", 20), bg='#ffffff', fg='#800000', justify='left')
    m1 = tkinter.Label(root, text="Aakash", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='right')
    l1 = tkinter.Label(root, text="", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='left')
    m2 = tkinter.Label(root, text="Pruthvi", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='right')
    l2 = tkinter.Label(root, text="", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='left')
    m3 = tkinter.Label(root, text="Vaayu", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='right')
    l3 = tkinter.Label(root, text="", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='left')
    m4 = tkinter.Label(root, text="Varuna", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='right')
    l4 = tkinter.Label(root, text="", font=("Arial Bold", 15), bg='#ffffff', fg='#000066', justify='left')
    
    
    m.grid(row=2, column=0, padx=25, pady=8, sticky='e')
    m1.grid(row=3, column=0, padx=25, pady=8, sticky='e')
    m2.grid(row=4, column=0, padx=25, pady=8, sticky='e')
    m3.grid(row=5, column=0, padx=25, pady=8, sticky='e')
    m4.grid(row=6, column=0, padx=25, pady=8, sticky='e')
    
    l.grid(row=2, column=2, pady=8, sticky='w')
    l1.grid(row=3, column=2, pady=8, sticky='w')
    l2.grid(row=4, column=2, pady=8, sticky='w')
    l3.grid(row=5, column=2, pady=8, sticky='w')
    l4.grid(row=6, column=2, pady=8, sticky='w')
    
    l1.configure(text=counter1)
    l2.configure(text=counter2)
    l3.configure(text=counter3)
    l4.configure(text=counter4)
    
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
    lcd.cursor_position(0, 0)
    lcd.message = "R - "
    lcd.cursor_position(4, 0)
    lcd.message = str(counter1)
    lcd.cursor_position(8, 0)
    lcd.message = "G - "
    lcd.cursor_position(12, 0)
    lcd.message = str(counter2)
    lcd.cursor_position(0, 1)
    lcd.message = "Y - "
    lcd.cursor_position(4, 1)
    lcd.message = str(counter3)
    lcd.cursor_position(8, 1)
    lcd.message = "B - "
    lcd.cursor_position(12, 1)
    lcd.message = str(counter4)
    
    while(True):
        if(but1.value):            
            led1.on()
            buzz.off()
            print('Aakash')            
            counter1 = counter1 + 1
            lcd.cursor_position(0, 0)
            lcd.message = "R - "
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "G - "
            lcd.cursor_position(12, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "Y - "
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(8, 1)
            lcd.message = "B - "
            lcd.cursor_position(12, 1)
            lcd.message = str(counter4)
            print(counter1)
            l1.configure(text=counter1)
            l2.configure(text=counter2)
            l3.configure(text=counter3)
            l4.configure(text=counter4)
            root.update()
            sleep(2)
            led1.off()
            buzz.on()
        if(but2.value):            
            led2.on()
            buzz.off()
            print('Pruthvi')        
            counter2 = counter2 + 1
            lcd.message = "R - "
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "G - "
            lcd.cursor_position(12, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "Y - "
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(8, 1)
            lcd.message = "B - "
            lcd.cursor_position(12, 1)
            lcd.message = str(counter4)
            print(counter2)
            l1.configure(text=counter1)
            l2.configure(text=counter2)
            l3.configure(text=counter3)
            l4.configure(text=counter4)
            root.update()
            sleep(2)
            led2.off()
            buzz.on()
        if(but3.value):            
            led3.on()
            buzz.off()
            print('Vaayu')        
            counter3 = counter3 + 1
            lcd.message = "R - "
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "G - "
            lcd.cursor_position(12, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "Y - "
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(8, 1)
            lcd.message = "B - "
            lcd.cursor_position(12, 1)
            lcd.message = str(counter4)
            print(counter3)
            l1.configure(text=counter1)
            l2.configure(text=counter2)
            l3.configure(text=counter3)
            l4.configure(text=counter4)
            root.update()
            sleep(2)
            led3.off()
            buzz.on()
        if(but4.value):            
            led4.on()
            buzz.off()
            print('Varuna')        
            counter4 = counter4 + 1
            lcd.message = "R - "
            lcd.cursor_position(4, 0)
            lcd.message = str(counter1)
            lcd.cursor_position(8, 0)
            lcd.message = "G - "
            lcd.cursor_position(12, 0)
            lcd.message = str(counter2)
            lcd.cursor_position(0, 1)
            lcd.message = "Y - "
            lcd.cursor_position(4, 1)
            lcd.message = str(counter3)
            lcd.cursor_position(8, 1)
            lcd.message = "B - "
            lcd.cursor_position(12, 1)
            lcd.message = str(counter4)
            print(counter4)
            l1.configure(text=counter1)
            l2.configure(text=counter2)
            l3.configure(text=counter3)
            l4.configure(text=counter4)
            root.update()
            sleep(2)
            led4.off()
            buzz.on()
        root.update()
if __name__ == "__main__":
    main()
        