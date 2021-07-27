###############################
# APPLET RUN by Srujan Gurram #
###############################

# USAGE: python appletrun.py EX_13_1.java
# WHAT IT DOES: it runs applet code from given java file in a new window

import os
import sys
import atexit
import subprocess
import re
import colorama
from colorama import Fore
java_version = float(re.search('\"(\d+\.\d+).*\"', subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT).decode('utf-8')).groups()[0])
if java_version >= 8 :
    print(Fore.RED +"[ERROR] Applets Not supported on "+java_version+" version of Java")
    print(Fore.BLUE +"[SUGGESTION] change to java 8 or less")
    print(Fore.WHITE)
else:
    user_input_path = sys.argv[-1].strip()
    program_path = os.path.abspath(user_input_path)
    program_file_name = os.path.splitext(os.path.basename(program_path))[0]
    if len(sys.argv) > 1:
        os.system("javac " + program_path)
        if os.path.isfile(program_file_name+".class"):
            print(Fore.GREEN + "[COMPILE] Applet Compiled")
            with open("applet.html", "w") as html_file:   
                html_file.write(
                    '''
                    <html>
                        <body>
                            <applet code="'''+program_file_name+'''.class" width="300" height="300"> </applet>
                        </body>
                    </html>
                    ''')
            print(Fore.BLUE + "[RUNNING] Applet Started")
            os.system("appletviewer applet.html")
        else:
            print(Fore.RED +"[Error] Compilation failed")
            print(Fore.WHITE)

    else:
        print(Fore.RED + "[ERROR] No file specified")
        print(Fore.BLUE + "USAGE: python appletrun.py <path_to_java_file>")
        print(Fore.BLUE + "Example: python appletrun.py EX_13_1.java")
        print(Fore.WHITE)
    
    def exit_handler():
        try:
            os.remove(os.path.splitext(program_path)[0] + ".class")
            os.remove("applet.html")
            print(Fore.GREEN +"[Sucess] Applet closed successfully")
            print(Fore.WHITE)
        except:
            pass
        
    atexit.register(exit_handler)