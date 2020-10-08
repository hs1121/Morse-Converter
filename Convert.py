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
                    
    def __init__(self,text,mode):
        if(mode==0):
            self.Text=text.strip()
            self.Morse=self.Convert_text(self.Text)
        else :
            self.Morse=text.strip(' /')
            self.Text=self.Convert_morse(self.Morse)
    
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
        return converted

    def Convert_morse(self,text):
        Converted=""
        for string in text.split():
            if string=='/':
                Converted+=" "
            else:
                if string not in self.Dict_morse.keys():
                    pass
                else :
                    Converted+=self.Dict_morse[string]
        return Converted


def test():
    mode=eval(input())
    text=input()
    obj=Convert(text,mode)
    print(obj.Text)
    print(obj.Morse)

test()