# https://discord.com/api/v9/channels/849021065619570751/messages
import os

# import time module, Observer, FileSystemEventHandler
import requests
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print("file.py is active now")

header = {
    'authorization': 'NzExMjUzNDI5MzU1MjgyNDMz.YLVGFw.sHzsHR7uGFxsPfW76jgjqsUMpSA'
}


def sendMsg(cnt):
    payload = {
        'content': cnt
    }
    r = requests.post(
        "https://discord.com/api/v9/channels/849021065619570751/messages", data=payload, headers=header)


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "/home/shivansh/Shivansh Comp Pract/Discord Bot Final/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("New file found")
            if(os.path.exists("cmd.txt")):
                file = open("cmd.txt", 'r+')
                body = file.read()
                file.close()
                print(body)
                os.remove("cmd.txt")
                lst = body.split("\n")
                for k in lst:
                    if k != "":
                        sendMsg(k)

        elif event.event_type == 'modified':
            print("Modifications detected")
            if(os.path.exists("cmd.txt")):
                file = open("cmd.txt", 'r+')
                body = file.read()
                file.close()
                print(body)
                os.remove("cmd.txt")
                lst = body.split("\n")
                for k in lst:
                    if k != "":
                        sendMsg(k)


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
