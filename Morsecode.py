from tkinter import *
from tkinter import simpledialog
import time         # for sleep() function
import winsound
import threading
from tkinter import messagebox
from PIL import ImageTk,Image

layout_bg="#e6a835"
text_col="#000"
run =True



def on_closing():     # when close button is pressed
   if messagebox.askokcancel("Quit", "Do you want to quit?"):
       global run
       run=False

class Home:
    def __init__(self,root):
       self.max_height =root.winfo_screenheight() 
       self.max_width = root.winfo_screenwidth()         # setting dimentions for max and initial window
       self.cur_height =600
       self.cur_width = 800

       root.title('Morsecode Converter')
       root.configure(background=layout_bg)                               # Setting the root window
       root.geometry(str(self.cur_width)+"x"+str(self.cur_height)+"+0+0")
       root.minsize(800, 600)

       self.l_heading=Label(root,fg=text_col, bg=layout_bg,text="MORSECODE CONVERTER")

       self.t_input=Text(root,bg="#edd29f")
       self.t_output=Text(root,bg="#edd29f",state=DISABLED)
       self.t_light=Text(root,bg="#000",state=DISABLED)

       self.is_playing=False
       self.is_sound=True      # check the status of the putton press
       self.is_light=False
       self.mode_text=True
       self.invalid_flag=False

       ########################### check box ################################
       self.checkbox_morse=Checkbutton(root, text = "Morse Code",variable=self.mode_text,onvalue = 1, offvalue = 0,command =self.onClick_mode,bg=layout_bg)


       ############################################## Buttons ######################################################################
       self.b_play=Button(root,command = self.onClick_play)
       self.b_pause=Button(root,command = self.onClick_pause)
       self.b_repeat=Button(root,command = self.onClick_repeat)
       self.b_sound=Button(root,command = self.onClick_sound)
       self.b_light=Button(root,command = self.onClick_light)
       self.b_submit=Button(root,command = self.onClick_submit)
       self.b_write=Button(root,command = self.onClick_write)


    def update_fun(self):    # function to update the parameters (similar to constraint layout)
        root.update()
        self.cur_height =root.winfo_height()     # Updating the window size 
        self.cur_width =root.winfo_width()

        self.l_heading.configure(font=("Courier", self.cast_text(44)))
        #self.b_write.configure(text='Write')

        self.place_mod(self.l_heading,30,5,40,5)
        self.place_mod(self.checkbox_morse,25,17,10,2)
        self.place_mod(self.t_input,25,20,50,15)
        self.place_mod(self.b_play,35,36,5,5)
        self.place_mod(self.b_pause,40,36,5,5)
        self.place_mod(self.b_repeat,45,36,5,5)
        self.place_mod(self.b_sound,50,36,5,5)
        self.place_mod(self.b_light,55,36,5,5)
        self.place_mod(self.b_write,45,61,10,5)

        if self.is_light:
            self.place_mod(self.t_output,25,45,25,15)
            self.place_mod(self.t_light,50,45,25,15)
        else:
            self.t_light.place_forget()
            self.place_mod(self.t_output,25,45,50,15)


        self.place_mod(self.b_submit,70,36,5,5)
        self.b_submit.configure(text="Submit",font=("Helvetica",self.cast_text(20)))
        self.b_write.configure(text="Save as doc",font=("Helvetica", self.cast_text(20)))
        self.img_but()

        root.update()


       #######################################  image buttons function   ###################################
    def img_but(self): 
        self.i_play=Image.open("Resources/play.png")
        self.i_pause=Image.open("Resources/pause.png")
        self.i_repeat=Image.open("Resources/repeat.png")
        self.i_sound=Image.open("Resources/sound.png")
        self.i_light=Image.open("Resources/light.png")

        self.i_play=self.i_play.resize((self.castx(2), self.casty(2)), Image. ANTIALIAS)
        self.i_pause=self.i_pause.resize((self.castx(2), self.casty(2)), Image. ANTIALIAS)
        self.i_repeat=self.i_repeat.resize((self.castx(2), self.casty(2)), Image. ANTIALIAS)
        self.i_sound=self.i_sound.resize((self.castx(2), self.casty(2)), Image. ANTIALIAS)
        self.i_light=self.i_light.resize((self.castx(2), self.casty(2)), Image. ANTIALIAS)

        self.i_play=ImageTk.PhotoImage(self.i_play)
        self.i_pause=ImageTk.PhotoImage(self.i_pause)
        self.i_repeat=ImageTk.PhotoImage(self.i_repeat)
        self.i_sound=ImageTk.PhotoImage(self.i_sound)
        self.i_light=ImageTk.PhotoImage(self.i_light)

        self.b_pause.configure(image=self.i_pause)
        self.b_play.configure(image=self.i_play)
        self.b_light.configure(image=self.i_light)
        self.b_sound.configure(image=self.i_sound)
        self.b_repeat.configure(image=self.i_repeat)

        if self.is_sound:
            self.b_sound.configure(bg=layout_bg)
            self.b_light.configure(bg="#fff")
        else:
            self.b_light.configure(bg=layout_bg)
            self.b_sound.configure(bg="#fff")


   #################################################### ON CLICK FUNCTIONS #####################################

    def onClick_play(self):
        if not(self.is_playing):
            if self.is_sound:
                self.is_playing=True
                threading.Thread(target=convert_obj.Play_sound).start()

            if self.is_light:
                self.is_playing=True
                convert_obj.flash_light()

    def onClick_pause(self):
        self.is_playing=False

    def onClick_repeat(self):
       self.is_playing=False
       self.onClick_play()

    def onClick_sound(self):
       self.is_sound=True
       self.is_light=False
       self.is_playing=False

    def onClick_light(self):
       self.is_sound=False
       self.is_light=True
       self.is_playing=False
    
    def onClick_write(self):
        fileName = str(simpledialog.askstring(title="Save as",prompt="Enter file name"))
        try:
            if fileName!='None':
                file_obj.write_file(convert_obj.Text,convert_obj.Morse,fileName)
        except:
            pass


    def onClick_submit(self):
       self.t_output.configure(state=NORMAL)
       self.t_output.delete('1.0', END)
       inp=""
       inp = self.t_input.get("1.0",END)
       if len(inp)==1:
          messagebox.showwarning("Warning", "Enter an appropriate string") 
       else:
           if not(self.invalid_flag):
            self.t_output.insert(INSERT,convert_obj.ret_str(inp,self.mode_text))
            self.t_output.configure(state=DISABLED)
           self.invalid_flag=False


    def onClick_mode(self):
        self.mode_text=not(self.mode_text)

    def light_bg(self,bg_col):
        self.t_light.configure(bg=bg_col)
        self.update_fun()

    def invalid_action(self):
        messagebox.showwarning("Warning", "Enter an appropriate string")
        self.t_input.delete('1.0', END)
        self.invalid_flag=True;



     #####################  Life easior making functions ##################
    def place_mod(self,obj,x1,y1,x2,y2):
        obj.place(x=self.castx(x1),y=self.casty(y1),width=self.castx(x2),height=self.casty(y2))
    ####################      casting functions to handle variable screen size   #############
    def cast_text(self,f_size):
        return (int)(self.cur_width/self.max_width*f_size)
    def castx(self,x):                  # converting the window width from 1 to 100 to make placing widgets easily
       return(int)(x/100*self.cur_width)
    def casty(self,y):                   # converting the window height from 1 to 100 to make placing widgets easily
      return(int)(y/100*self.cur_height)


############################################### class home ends###############################################################
###############################################################################################################################


# main class for conversion of morse code
class Convert:
    # list of two dictionaries for conversion
    # Dict_text for direct conversion
    # Dict_morse for inverse conversion
    Dict_text =  {       
                'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-'
                } 
    Dict_morse={v:k for k,v in Dict_text.items()} 
                    
    # Initialising object by assigning the english string to variable Text and
    # morse-code string to Morse variable
    def __init__(self):
        self.Text=""
        self.Morse=""
    def ret_str(self,text,mode):
        if(mode==1):
            self.Text=text.strip()    #strip extra whitespace around the string
            self.Morse=self.Convert_text(self.Text)
            return self.Morse
        else :
            self.Morse=text.strip(' /')  #strip extra whitespace and / around the morse string
            self.Text=self.Convert_morse(self.Morse)
            return self.Text
    

    # Function to convert from english to morse
    def Convert_text(self,text):
        converted=""
        for char in text.upper():
            if char==' ' :
                converted+="/ "
            else:
                if char not in self.Dict_text.keys():
                    print("ok")
                else :
                    converted+=self.Dict_text[char]
                    converted+=" "
        return converted.strip()

    #Function to convert from morse to English
    def Convert_morse(self,text):
        Converted=""
        for string in text.split():
            if string=='/':
                     Converted+=" "
            else:
                if string not in self.Dict_morse.keys():
                    home_obj.invalid_action()
                    break
                else :
                    Converted+=self.Dict_morse[string]
        return Converted

    # Function for playing sound 
    def Play_sound(self):
        var=[]
        for ch in self.Morse: 
            if home_obj.is_playing==False:
                break
            if ch=='-':
                winsound.Beep(1000,300)    #Beep of duration 300ms
                time.sleep(.1)
            elif ch=='.':
                 winsound.Beep(1000,100)    #Beep of duration 100ms
                 time.sleep(.1)
            elif ch==' ':
                time.sleep(.2)
        home_obj.is_playing=False
    def flash_light(self):
        for ch in self.Morse:
            if home_obj.is_playing==False:
              break
            if ch=='-':
                home_obj.light_bg("#fff")
                time.sleep(.3)
                home_obj.light_bg("#000")
            elif ch=='.':
               home_obj.light_bg("#fff")
               time.sleep(.1)
               home_obj.light_bg("#000")
            elif ch==' ':
                home_obj.light_bg("#000")
                time.sleep(.2)
            home_obj.light_bg("#000")
            time.sleep(.1)
        home_obj.is_playing=False


############################################### class Converter ends###########################################################
###############################################################################################################################

class File:

    # Initialising class
    def __init__(self): 
        pass
    # function to appen a file with the english as well as morse text to file name passed by user as "name"
    def write_file(self,eng,morse,name):
        fname=name+".txt"
        with open(fname,"a") as file:
            # file.write("-"*10+"\n")
            file.write("English:\n"+eng+"\n\nMorse:\n"+morse+"\n")
            file.write("-"*100+"\n")

############################################### class file ends###############################################################
###############################################################################################################################



root = Tk()
home_obj=Home(root) 
file_obj=File()
convert_obj=Convert()
root.protocol("WM_DELETE_WINDOW", on_closing)   # event handling for clicling close button

def main():
    while run:         # alternative to mainloop() to edit updtes as required
        root.after(16,home_obj.update_fun())
    root.destroy()
main()