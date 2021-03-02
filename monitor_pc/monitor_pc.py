#!/usr/bin/env python3

import emails
import datas
import sys
import datetime

if __name__ == "__main__":
    cpu, memory, disk, localhost_ip = datas.gather()
    result = datas.evaluate(cpu, memory, disk, localhost_ip)
    try:
        mail_file = sys.argv[1]
        credentials = []
        now = datetime.datetime.now().ctime() 
        with open(mail_file, 'r') as f:
            # save credentials in a list, split them by newline and ignore the
            # last empty string
            credentials = f.read().split('\n')[:-1]
            server, port, sender, password, recipient = credentials 
            f.close()
        if result != 0 and result != 1:                                                                                            
            subject = "Monitor PC Alert"
            body = now + " - " + result
            print(sender, recipient, subject, body)
            message = emails.generate(sender, recipient, subject, body)
            print(message, server , port, sender, password)
            emails.send(message, server , port, sender, password)

        elif result == 1:                                                                                                          
            print("{} - Error, something went wrong".format(now))
        else:
            print("{} - Everything is OK".format(now))

    except Exception as e:
        raise e
