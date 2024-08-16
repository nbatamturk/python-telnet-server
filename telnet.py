# -*- coding: utf-8 -*-
import socket
import subprocess
import threading
import os
import time
import signal

def run_command_with_timeout(command, client_socket, timeout):
    try:
        # Komutu subprocess ile çalıştırma
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        start_time = time.time()
        
        while True:
            if process.poll() is not None:
                break

            if time.time() - start_time > timeout:
                process.terminate()
                client_socket.sendall(b"\n[INFO] Command timed out.\n")
                break

            output = process.stdout.readline()
            if output:
                client_socket.sendall(output.decode('utf-8').encode('utf-8'))
            time.sleep(0.1)

        # Sonuçları göndermeyi bitir
        client_socket.sendall(b"\n[INFO] Command finished.\n")
    except Exception as e:
        client_socket.sendall("Error: {}\n".format(str(e)).encode('utf-8'))

def start_telnet_server(host='0.0.0.0', port=23):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Telnet server listening on {0}:{1}".format(host, port))

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print("Connection from {0}".format(client_address))
            client_socket.sendall(b"Welcome to the Telnet server! Type commands and press Enter.\n")

            current_directory = os.getcwd()
            
            while True:
                try:
                    client_socket.sendall("{0}$ ".format(current_directory).encode('utf-8'))
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    command = data.decode('utf-8').strip()
                    print("Command received:", command)  # Log the command

                    if command.lower() == 'exit':
                        client_socket.sendall(b"Goodbye!\n")
                        break

                    if command.startswith('cd '):
                        new_directory = command[3:].strip()
                        if os.path.isdir(new_directory):
                            os.chdir(new_directory)
                            current_directory = os.getcwd()
                            client_socket.sendall("Changed directory to {0}\n".format(current_directory).encode('utf-8'))
                        else:
                            client_socket.sendall("No such directory: {0}\n".format(new_directory).encode('utf-8'))
                    else:
                        # Komutu çalıştır
                        if command.startswith('tail'):
                            tail_thread = threading.Thread(target=run_command_with_timeout, args=(command, client_socket, 30))
                            tail_thread.start()
                        else:
                            try:
                                # Komut çalıştırma ve zaman aşımı
                                output = subprocess.check_output(command + " 2>&1", shell=True, stderr=subprocess.STDOUT, timeout=10)
                                response = output.decode('utf-8')
                            except subprocess.CalledProcessError as e:
                                response = "Error: {0}".format(e.output.decode('utf-8'))
                            except subprocess.TimeoutExpired:
                                response = "Error: Command timed out."
                            except Exception as e:
                                response = "Unexpected error: {0}".format(str(e))
                            
                            client_socket.sendall(response.encode('utf-8') + b"\n")
                        
                except Exception as e:
                    response = "Error: {0}".format(str(e))
                    client_socket.sendall(response.encode('utf-8') + b"\n")
        
            client_socket.close()

        except Exception as e:
            print("Unexpected error: {0}".format(str(e)))

if __name__ == "__main__":
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # Ignore child process termination signals
    start_telnet_server()
