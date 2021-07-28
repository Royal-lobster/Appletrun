#!python

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
def main():
    try:
        java_version = float(re.search('\"(\d+\.\d+).*\"', subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT).decode('utf-8')).groups()[0])
    except:
        print('\033[91m' +'[Error] Java not found. Please install java <= 8 and try again.'+ '\x1b[0m')
        print('\033[94m' +'[SUGGESTION] Install from here: https://www.azul.com/downloads/?package=jdk'+ '\x1b[0m')
        java_version = None
    if java_version != None and java_version >= 8 :
        print('\033[91m' +"[ERROR] Applets Not supported on "+str(java_version)+" version of Java"+ '\x1b[0m')
        print('\033[94m' +"[SUGGESTION] change to java 8 or less"+ '\x1b[0m')
        print('\033[94m' +'[SUGGESTION] Install from here: https://www.azul.com/downloads/?package=jdk'+ '\x1b[0m')
    elif java_version != None:
        user_input_path = sys.argv[-1].strip()
        program_path = os.path.abspath(user_input_path)
        program_file_name = os.path.splitext(os.path.basename(program_path))[0]
        if len(sys.argv) > 1:
            os.system("javac " + program_path)
            if os.path.isfile(program_file_name+".class"):
                print('\033[92m' + "[COMPILE] Applet Compiled")
                with open("applet.html", "w") as html_file:   
                    html_file.write(
                        '''
                        <html>
                            <body>
                                <applet code="'''+program_file_name+'''.class" width="300" height="300"> </applet>
                            </body>
                        </html>
                        ''')
                print('\033[94m' + "[RUNNING] Applet Started"+ '\x1b[0m')
                os.system("appletviewer applet.html"+ '\x1b[0m')
            else:
                print('\033[91m' +"[Error] Compilation failed"+ '\x1b[0m')

        else:
            print('\033[91m' + "[ERROR] No file specified"+ '\x1b[0m')
            print('\033[94m' + "USAGE: python appletrun.py <path_to_java_file>"+ '\x1b[0m')
            print('\033[94m' + "Example: python appletrun.py EX_13_1.java"+ '\x1b[0m')
        
        def exit_handler():
            try:
                os.remove(os.path.splitext(program_path)[0] + ".class")
                os.remove("applet.html")
                print('\033[92m' +"[Success] Applet closed successfully"+ '\x1b[0m')
            except:
                pass
            
        atexit.register(exit_handler)
if __name__ == "__main__":
    main()