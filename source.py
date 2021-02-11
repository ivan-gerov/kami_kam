#!/usr/local/bin/python
# -*- coding: utf8

import decryption_util, tasks

def main():
    if tasks.task_controller(tasks.TASKS):
        try:
            with open("./data/encoded_message_for_Kami.txt", 
                      encoding="utf8", mode="r") as f:
                message = f.read()
        except Exception as e:
            print(e)
            raise Exception("Миличко, моля те, намери файла 'encoded_message_for_Kami.txt' и го сложи в същата папка като source.py")

        message = [char for char in message]
        message = decryption_util.unshuffle_list(message)
        print("#-----------------------#")
        print("".join(message))
        print("#-----------------------#")
if __name__ == "__main__":
    main()