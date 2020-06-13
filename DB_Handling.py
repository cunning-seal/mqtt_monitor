from tkinter import *

def on_submit_dbview_callback(event):
    filename = event.widget.master.nametowidget("fname").get()
    if filename == "":
        label = event.widget.master.nametowidget("lbl")['fg'] = "#FF0000"
    else:
        event.widget.master.destroy()
        DatabaseShowView(filename).show()

class DatabaseStartView:
    def __init__(self):
        self.root = Tk()
        self.root.title("Конфигурация пар топик/ключ")

        self.root.geometry("410x200")
        self.root['bg'] = '#E3D3CF'
        filename_label = Label(self.root, text="Введите имя файла конфигурации", name="lbl", bg="#E3D3CF")
        filename_entry = Entry(self.root, name="fname")
        filename_button = Button(self.root, text="Готово")
        filename_label.place(x=90, y=10)
        filename_entry.place(x=100, y=50)
        filename_button.place(x=170, y=100)
        filename_button.bind("<Button-1>", on_submit_dbview_callback)

    def show(self):
        self.root.mainloop()


class DatabaseChangeView:
    def __init__(self, filename):
        self.root = Tk()
        self.root.title("Изменение пар топик/ключ")

        self.root.geometry("410x200")
        self.root['bg'] = '#E3D3CF'

    def show(self):
        self.root.mainloop()

class DatabaseShowView:
    def __init__(self, filename):
        self.root = Tk()
        self.root.title("Табличное представление пар топик/ключ")


        self.root['bg'] = '#E3D3CF'
        x_start = 10
        y_start = 10
        step = 30
        dist = 200

        label1 = Label(self.root, text="Топик", bg='#E3D3CF')
        label2 = Label(self.root, text="Ключ", bg='#E3D3CF')
        label1.place(x=x_start, y=y_start)
        label2.place(x=x_start + dist, y=y_start)
        y_start += step

        with open(filename) as f:
            for row in f:
                data = row.split()
                topic = data[0].strip()
                key = data[1].strip()
                label1 = Label(self.root, text=topic, bg='#E3D3CF', borderwidth=2,relief="ridge", width="20")
                label2 = Label(self.root, text=key,bg='#E3D3CF', borderwidth=2,relief="ridge", width="20")
                label1.place(x=x_start, y=y_start)
                label2.place(x=x_start+dist, y=y_start)
                y_start+=step


        self.root.geometry("420x{}".format(y_start+step))

        # add_button = Button(self.root, text="Добавить пару ключ/топик",width="20")
        # delete_btn = Button(self.root, text="Удалить пару ключ/топик",width="20")
        # add_button.place(x=x_start, y=y_start)
        # delete_btn.place(x=x_start+dist, y=y_start)

    def show(self):
        self.root.mainloop()

def add_pair_callback(event):
    topic = event.widget.master.nametowidget("topic").get()
    key = event.widget.master.nametowidget("key").get()



class DatabaseAddView:
    def __init__(self, filename):
        self.root = Tk()
        self.root.title("Изменение пар топик/ключ")
        self.root['bg'] = '#E3D3CF'
        topic_entry = Entry(self.root, name="topic")
        key_entry = Entry(self.root, name="key")
        btn = Button(self.root, text="Добавить")



if __name__ == '__main__':

    DatabaseStartView().show()