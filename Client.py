import socket
import threading
import tkinter as tk
from tkinter import scrolledtext


class ClientSocket:
    def __init__(self, host='127.0.0.1', port=8081):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.listeners = []

        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))
        self.notify_listeners(f"나: {message}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.notify_listeners(f"상대방: {message}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def register_listener(self, listener):
        self.listeners.append(listener)

    def notify_listeners(self, message):
        for listener in self.listeners:
            listener(message)


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.pack(pady=10)

        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=5, padx=10, side=tk.LEFT, fill=tk.X, expand=True)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5, padx=10, side=tk.RIGHT)

        self.message_entry.bind("<Return>", self.send_message)

        self.client_socket = ClientSocket()
        self.client_socket.register_listener(self.display_message)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_socket.send_message(message)
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()

'''
from socket import *
import threading
import time

class Client_socket:
    def send(sock):
        while True:
            sendData = input('')
            sock.send(sendData.encode('utf-8'))

    def receive(sock):
        while True:
            recvData = sock.recv(1024)
            print('상대방 :', recvData.decode('utf-8'))

    port = 8081

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', port))

    print('접속 완료')

    sender = threading.Thread(target=send, args=(clientSock,))
    receiver = threading.Thread(target=receive, args=(clientSock,))

    sender.start()
    receiver.start()

    while True:
        time.sleep(1)
        pass
'''
