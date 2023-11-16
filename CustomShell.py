import subprocess as sub

while True:
     command = input("Shell => ")
     cmd = sub.check_output(command, shell=True).decode()
     print(cmd)
     if command=="Exit":
         break
