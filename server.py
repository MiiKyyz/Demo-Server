import socket
import threading
from kivy.clock import Clock
import  main



class Gemys_Server:

    PORT = 8080
    IP = socket.gethostbyname(socket.gethostname())
    HEADER = 10
    online = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    the_teller = ''
    list_of_people_connected = {}
    list_of_ip = []
    first_connection = False


    def __init__(self):
        self.online.bind((self.IP, self.PORT))
        main.Main_Server_Gemys.connect = self.first_connection



    def handle_client(self,conn, addr):
        print(f"User {addr} has initialized session!")

        self.ip = addr
        self.list_of_ip.append(self.ip)




        msg_show = ''
        BYTES = 20
        connected = True
        self.first_connection = True

        while connected:

            msg = conn.recv(BYTES)
            msg_show += str(msg.decode('utf-8'))

            if self.first_connection is True:


                if len(msg) != 0:
                    if len(msg) < BYTES:
                        #print(f'name {msg_show}')

                        self.list_of_people_connected[msg_show] = addr




                        #Clock.schedule_once(main.Main_Server_Gemys().add_connected)



                        msg_show = ''
                        msg = ''
                        self.first_connection = False



                else:
                    pass

            else:

                if len(msg) != 0:
                    if len(msg) < BYTES:
                        print(f'message from {addr[0]}{msg_show}')

                        msg_show = ''


        conn.close()

    def start(self):
        self.online.listen()
        print(F"SERVER STARTED AT STATE {self.IP}")

        while True:
            conn , addr = self.online.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()





            conn.send(bytes("Welcome User", "utf-8"))

    def miki(self):

        while True:
            print("miky")


main_thread = threading.Thread(target=Gemys_Server().miki)
main_thread.start()