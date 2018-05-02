from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='ich bin Label')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='ich bin button', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('ich bin title')
# 主消息循环:
app.mainloop()
