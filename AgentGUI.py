from tkinter import *
from tkinter.ttk import Treeview
from subprocess import Popen
import signal
IP_text = "IP"
port_text = "Порт"

proc = None

class BasicWindow:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("410x200")
        self.root['bg'] = '#E3D3CF'

    def show(self):
        self.root.mainloop()


def ip_entry_on_press_callback(event):
    if event.widget.get() == IP_text:
        pass
    event.widget.delete(0, END)

def port_entry_on_press_callback(event):
    if event.widget.get() == port_text:
        pass
    event.widget.delete(0, END)

def refocus_callback(event):
    ip_entry = event.widget.winfo_children()[0]
    if ip_entry.get() == "":
        ip_entry.insert(0, IP_text)
    event.widget.focus()


def start_onclick_callback(event):
    ip = event.widget.master.nametowidget("ip_entry").get()
    port = event.widget.master.nametowidget("port_entry").get()
    config_filename = event.widget.master.nametowidget("filename_entry").get()
    id = event.widget.master.nametowidget("id_entry").get()
    event.widget.master.destroy()
    global proc
    args = ["python3", "bridge_start.py", ip, port, config_filename, id]
    proc = Popen(args, shell=False)
    text = "Агент успешно запущен" if proc is not None else "Произошла ошибка запуска агента: {}".format(Popen.stderr)
    AgentInfoView(text).show()

class AgentStartView(BasicWindow):

    def __init__(self):
        super().__init__("Запуск агента")
        zabbix_label = Label(self.root, text="Настройки MQTT брокера", bg="#E3D3CF")
        ip_entry = Entry(self.root, bg="white", width="20", name="ip_entry")
        port_entry = Entry(self.root, bg="white", width="20", name="port_entry")
        br_label = Label(self.root, text="Настройки конфигурации моста", bg="#E3D3CF")
        br_filename_entry = Entry(self.root, bg="white", width="20", name="filename_entry")
        br_id_entry = Entry(self.root, bg="white", width="20", name="id_entry")
        start_button = Button(self.root, text="Запуск", width="15")
        zabbix_label.place(x=10, y=10)
        ip_entry.place(x=10, y=40)
        port_entry.place(x=210, y=40)
        br_label.place(x=10, y=70)
        br_filename_entry.place(x=10, y=100)
        br_id_entry.place(x=210, y=100)
        start_button.place(x=210, y=150)
        ip_entry.delete(0, END)
        ip_entry.insert(0, IP_text)
        port_entry.delete(0, END)
        port_entry.insert(0, port_text)
        br_filename_entry.delete(0, END)
        br_filename_entry.insert(0, "Файл конфигурации")
        br_id_entry.delete(0, END)
        br_id_entry.insert(0, "ID")
        start_button.bind("<Button-1>", start_onclick_callback)

def ok_button_callback(event):
    proc.send_signal(signal.SIGINT)
    event.widget.master.destroy()


class AgentInfoView(BasicWindow):
    def __init__(self, text):
        super().__init__("Уведомление о запуске агента")

        result_text = Label(self.root, text=text)
        button = Button(self.root, width="15", text="Остановить агент")

        result_text.place(x=175, y=40)
        result_text['bg'] = '#E3D3CF'
        button.place(x=210, y=150)

        button.bind("<Button-1>", ok_button_callback)


class AgentSetupMenu(BasicWindow):
    def __init__(self):
        super().__init__("Меню настройки агента")
        item_list = Label(self.root, text="Список вещей")
        item_list['bg'] = '#E3D3CF'
        item_list_e = Entry(self.root, width="25")
        item_list_b = Button(self.root, text="Выбрать файл", width=12)

        topics_list = Label(self.root, text="Список доступных топиков")
        topics_list['bg'] = '#E3D3CF'
        topics_list_e = Entry(self.root, width="25")
        topics_list_b = Button(self.root, text="Выбрать файл", width=12)

        load_button = Button(self.root, text="Загрузить", width=12)

        item_list.place(x=10, y=10)
        item_list_e.place(x=10, y=35)
        item_list_b.place(x=270, y=37)

        topics_list.place(x=10, y=70)
        topics_list_e.place(x=10, y=95)
        topics_list_b.place(x=270, y=97)

        load_button.place(x=270, y=150)

