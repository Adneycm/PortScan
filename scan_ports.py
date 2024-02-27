import tkinter as tk
import socket
from tkinter import scrolledtext
import json
from graphic_interface import GraphicInterface

class ScanPorts:
    def __init__(self):
        self.interface = GraphicInterface()
        self.well_known_ports = json.load(open('WellKnowPorts.json', 'r'))


    def scan_ports(self):
        host = self.interface.entry_host.get()
        port_range = self.interface.entry_port.get()
        start_port, end_port = map(int, port_range.split('-'))

        self.interface.output.delete('1.0', tk.END)

        for port in range(start_port, end_port + 1):
            try:
                service = self.well_known_ports.get(str(port), "Unknown")
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    self.interface.output.insert(tk.END, f'Port {port} open - {service}\n')
                sock.close()
            except socket.error:
                pass

    def scan(self):
        self.interface.create_interface(command=self.scan_ports)

