#!/usr/bin/env python3

import emails
import datas
import sys
import datetime

if __name__ == "__main__":
    '''Simple monitoring service to gather data about free cpu left, free RAM left,
    free disk space left and if localhost correctly resolves to 127.0.0.1.
    
    Expects a textfile as a parameter formated with lines:
    [0] SMTP server
    [1] SMTP port
    [2] SMTP login (and sender e-mail address)
    [3] SMTP password
    [4] Recipient's e-mail address'''

    cpu, memory, disk, localhost_ip = datas.gather()
    result = datas.evaluate(cpu, memory, disk, localhost_ip)

    try:
        mail_file = sys.argv[1]
        credentials = []
        now = datetime.datetime.now().ctime() 

        with open(mail_file, 'r') as f:
            # save credentials in a list, split them by newline and ignore the
            # last empty string then save them to
            credentials = f.read().split('\n')[:-1]
            server, port, login, password, recipient = credentials 
            f.close()

        if result != 0 and result != 1:                                                                                            
            subject = "Monitor PC Alert"
            body = now + " - " + result

            message = emails.generate(login, recipient, subject, body)
            emails.send(message, server , port, login, password)

        elif result == 1:                                                                                                          
            print("{} - Error, something went wrong".format(now))
        else:
            print("{} - Everything is OK".format(now))

    except Exception as e:
        raise e
