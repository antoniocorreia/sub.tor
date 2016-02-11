#
# Created by Antonio Correia Feb, 2016
#

import os
import glob
from textblob import TextBlob

translateTo = "pt-br"

def translate(text):
    blob = TextBlob(text)
    return blob.translate(to="pt-br")
   
os.chdir(os.getcwd())

for file in glob.glob("*.vtt"):
    print("Traduzindo "+file)
    
    sub_file = open(file,"r")
    sub_text = sub_file.readlines()
    trans_text = ""
    
    for line in sub_text:
        
        if not(line[:1].isdigit() or line.strip() == ""):
            line = str(translate(line))

        if line.strip() == "":
            line = "\n"
        
        trans_text = trans_text + line

    trans_file = open(file[:len(file)-1]+translateTo+".srt","w")
    trans_file.write(trans_text)
    trans_file.close()
    print(file+" traduzido")
    
    sub_file.close()


