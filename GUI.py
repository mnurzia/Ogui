import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import Comm, Config
import random
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.config = Config.OgarConfig('gameserver.ini')
        self.ocl = None
        self.grid(row=0,column=0)
        self.isexit = False

        root.protocol('WM_DELETE_WINDOW',lambda: self.exit(None))
        #Color defs

        self.BGCOLOR1 = "#222222"
        self.BGCOLOR2 = "#444444"
        self.BGCOLOR3 = "#aaaaaa"
        self.BDCOLOR  = "#000000"
        self.FGCOLOR  = "#00ff00"

        self.crWid()

    def crWid(self): #Creates widgets. By far the longest function I've ever written.
        self.status = tk.LabelFrame(master=root,text="Status",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.status.grid(row=0,column=0,sticky='nsew')

        self.statsv = tk.StringVar()
        self.statslabel = tk.Label(self.status,textvariable=self.statsv,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.statslabel.grid(row=0,column=0,sticky='nsew')

        self.actions = tk.LabelFrame(master=root,text="Actions",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.actions.grid(row=1,column=0,sticky='nsew')

        self.consolef = tk.LabelFrame(master=root,text="Console",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.consolef.grid(row=2,column=0,sticky='nsew')
        self.console = tk.Text(self.consolef,height=20,state=tk.DISABLED,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.console.pack(expand=1,fill=tk.BOTH)

        self.console.tag_config("console",foreground='#dddddd')
        self.console.tag_config("log",foreground='#009bff')
        self.console.tag_config("server",foreground='#cd5c5c')

        self.ocl = Comm.OgarTerm(self.console)

        self.actions.columnconfigure(0,weight=1)
        self.actions.columnconfigure(1,weight=1)
        self.actions.columnconfigure(2,weight=1)
        self.actions.columnconfigure(3,weight=1)
        self.actions.columnconfigure(4,weight=1)
        self.actions.columnconfigure(5,weight=1)
        self.actions.columnconfigure(6,weight=1)

        self.playerlist = ttk.Treeview(self.actions)
        self.plstyle = ttk.Style().configure("Treeview",foreground=self.FGCOLOR,background=self.BGCOLOR1,fieldbackground=self.BGCOLOR1)
        self.playerlist.grid(row=0,column=0,columnspan=7)

        self.playerlist["columns"] = ["#0","#1","#2","#3","#4","#5","#6"]

        self.playerlist.column("#0",width=200)
        self.playerlist.column("#1",width=50)
        self.playerlist.column("#2",width=200)
        self.playerlist.column("#3",width=50)
        self.playerlist.column("#4",width=75)
        self.playerlist.column("#5",width=50)
        self.playerlist.column("#6",width=50)

        self.playerlist.heading("#0",text="Name")
        self.playerlist.heading("#1",text="#")
        self.playerlist.heading("#2",text="IP")
        self.playerlist.heading("#3",text="Cells")
        self.playerlist.heading("#4",text="Score")
        self.playerlist.heading("#5",text="X")
        self.playerlist.heading("#6",text="Y")


        self.kickb = tk.Label(self.actions,text="Kick",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.kickb.bind("<Button-1>",self.kick)
        self.kickb.grid(row=1,column=0,sticky='nsew')

        self.killb = tk.Label(self.actions,text="Kill",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.killb.bind("<Button-1>",self.kill)
        self.killb.grid(row=1,column=1,sticky='nsew')

        self.killallb = tk.Label(self.actions,text="Kill All",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.killallb.bind("<Button-1>",self.killall)
        self.killallb.grid(row=1,column=2,sticky='nsew')

        self.addbot = tk.Label(self.actions,text="Add Bot",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.addbot.bind("<Button-1>",self.addbotf)
        self.addbot.grid(row=1,column=3,sticky='nsew')

        self.pause = tk.Label(self.actions,text="Pause",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.pause.bind("<Button-1>",self.pausef)
        self.pause.grid(row=1,column=4,sticky='nsew')

        self.reload = tk.Label(self.actions,text="Reload",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.reload.bind("<Button-1>",self.reloadf)
        self.reload.grid(row=1,column=5,sticky='nsew')

        self.exitb = tk.Label(self.actions,text="Exit",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.exitb.bind("<Button-1>",self.exit)
        self.exitb.grid(row=1,column=6,sticky='nsew')



        self.boardframe = tk.LabelFrame(self.actions,text="Board",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.boardframe.grid(row=2,column=0,columnspan=4,sticky='nsew')

        self.boardframe.columnconfigure(0,weight=1)
        self.boardb = tk.Label(self.boardframe,text="Board",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.boardb.bind("<Button-1>",self.boardf)
        self.boardb.grid(row=0,column=0,sticky='nsew')

        self.boardframe.columnconfigure(1,weight=1)
        self.boardtv = tk.StringVar()
        self.boardentry = tk.Entry(self.boardframe,textvariable=self.boardtv,width=5,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.boardentry.grid(row=0,column=1,columnspan=2,sticky='nsew')

        self.boardframe.columnconfigure(3,weight=1)
        self.boardr = tk.Label(self.boardframe,text="Reset",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.boardr.bind("<Button-1>",self.ocl.boardReset)
        self.boardr.grid(row=0,column=3,sticky='nsew')



        self.virusframe = tk.LabelFrame(self.actions,text="Virus",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.virusframe.grid(row=2,column=4,columnspan=3,sticky='nsew')

        self.virusframe.columnconfigure(0,weight=1)
        self.virusb1 = tk.Label(self.virusframe,text="Virus",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.virusb1.bind("<Button-1>",lambda event: self.ocl.virus(self.virusx.get(),self.virusy.get(),self.virusm.get()))
        self.virusb1.grid(row=0,column=0,columnspan=3,sticky='nsew')

        self.virusframe.columnconfigure(3,weight=1)
        self.virusx = tk.StringVar()
        self.viruse1 = tk.Entry(self.virusframe,textvariable=self.virusx,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.viruse1.grid(row=0,column=3,sticky='nsew')

        self.virusframe.columnconfigure(4,weight=1)
        self.virusy = tk.StringVar()
        self.viruse2 = tk.Entry(self.virusframe,textvariable=self.virusy,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.viruse2.grid(row=0,column=4,sticky='nsew')

        self.virusframe.columnconfigure(5,weight=1)
        self.virusm = tk.StringVar()
        self.viruse3 = tk.Entry(self.virusframe,textvariable=self.virusm,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.viruse3.grid(row=0,column=5,sticky='nsew')

        self.virusframe.columnconfigure(6,weight=1)
        self.virusb2 = tk.Label(self.virusframe,text="Random",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.virusb2.bind("<Button-1>",lambda event: self.randomvirus())
        self.virusb2.grid(row=0,column=6,columnspan=3,sticky='nsew')



        self.colorframe = tk.LabelFrame(self.actions,text="Color",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.colorframe.grid(row=3,column=0,columnspan=3,sticky='nsew')

        self.colorframe.columnconfigure(0,weight=1)
        self.colorb1 = tk.Label(self.colorframe,text="Set",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.colorb1.bind("<Button-1>",self.setcolor)
        self.colorb1.grid(row=0,column=0,sticky='nsew')

        self.colorframe.columnconfigure(1,weight=1)
        self.colorv = tk.StringVar()
        self.colorv.set("Color")
        self.colorlabel = tk.Label(self.colorframe,textvariable=self.colorv,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.colorlabel.grid(row=0,column=1,sticky='nsew')

        self.colorframe.columnconfigure(2,weight=1)
        self.colorb1 = tk.Label(self.colorframe,text="Get",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.colorb1.bind("<Button-1>",self.getcolor)
        self.colorb1.grid(row=0,column=2,sticky='nsew')




        self.foodframe = tk.LabelFrame(self.actions,text="Food",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.foodframe.grid(row=3,column=4,columnspan=3,sticky='nsew')

        self.foodframe.columnconfigure(0,weight=1)
        self.foodb1 = tk.Label(self.foodframe,text="Food",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.foodb1.bind("<Button-1>",lambda event: self.ocl.food(self.foodx.get(),self.foody.get(),self.foodm.get()))
        self.foodb1.grid(row=0,column=0,columnspan=3,sticky='nsew')

        self.foodframe.columnconfigure(3,weight=1)
        self.foodx = tk.StringVar()
        self.foode1 = tk.Entry(self.foodframe,textvariable=self.foodx,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.foode1.grid(row=0,column=3,sticky='nsew')

        self.foodframe.columnconfigure(4,weight=1)
        self.foody = tk.StringVar()
        self.foode2 = tk.Entry(self.foodframe,textvariable=self.foody,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.foode2.grid(row=0,column=4,sticky='nsew')

        self.foodframe.columnconfigure(5,weight=1)
        self.foodm = tk.StringVar()
        self.foode3 = tk.Entry(self.foodframe,textvariable=self.foodm,width=3,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.foode3.grid(row=0,column=5,sticky='nsew')

        self.foodframe.columnconfigure(6,weight=1)
        self.foodb2 = tk.Label(self.foodframe,text="Random",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.foodb2.bind("<Button-1>",lambda event: self.randomfood())
        self.foodb2.grid(row=0,column=6,columnspan=3,sticky='nsew')



        self.massframe = tk.LabelFrame(self.actions,text="Mass",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.massframe.grid(row=4,column=0,columnspan=2,sticky='nsew')

        self.massframe.columnconfigure(0,weight=1)
        self.massb1 = tk.Label(self.massframe,text="Mass",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.massb1.bind("<Button-1>",lambda event: self.ocl.mass(self.playerlist.selection()[0],self.massv.get()))
        self.massb1.grid(row=0,column=0,sticky='nsew')

        self.massframe.columnconfigure(1,weight=1)
        self.massv = tk.StringVar()
        self.masse1 = tk.Entry(self.massframe,textvariable=self.massv,width=5,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.masse1.grid(row=0,column=1,sticky='nsew')



        self.nameframe = tk.LabelFrame(self.actions,text="Name",padx=5,pady=5,fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.nameframe.grid(row=4,column=4,columnspan=4,sticky='nsew')

        self.nameframe.columnconfigure(0,weight=1)
        self.nameb1 = tk.Label(self.nameframe,text="Name",fg=self.FGCOLOR,bg=self.BGCOLOR1)
        self.nameb1.bind("<Button-1>",lambda event: self.ocl.name(self.playerlist.selection()[0],self.namev.get()))
        self.nameb1.grid(row=0,column=0,sticky='nsew')

        self.nameframe.columnconfigure(1,weight=1)
        self.namev = tk.StringVar()
        self.namee1 = tk.Entry(self.nameframe,textvariable=self.namev,width=20,fg=self.FGCOLOR,bg=self.BGCOLOR1,highlightbackground=self.FGCOLOR,highlightthickness=1,relief=tk.FLAT)
        self.namee1.grid(row=0,column=1,columnspan=3,sticky='nsew')

    def update(self): #What to call after GUI is idle. Auto updating stuff goes here
        if self.isexit == False:
            self.pdata = self.ocl.playerList()
            for p in self.pdata:
                if not p["donp"]:
                    if p["id"] not in self.playerlist.selection():
                        if p["id"] not in self.playerlist.get_children():
                            self.ocl.insertConsole("[  LOG  ] New/regenerating player! (Name "+p["name"]+", ID "+p["id"]+", IP "+p["ip"]+")\n",("log"))
                        if p["id"] in self.playerlist.get_children():
                            self.playerlist.delete(p["id"])
                        self.playerlist.insert("",0,iid=p["id"],text=p["name"],values=(p["id"],p["ip"],p["cells"],p["score"],p["x"],p["y"]))
            self.sdata = self.ocl.status()
            self.statsv.set("Online: %s/%s   Players: %s   Bots: %s   Uptime: %s   Memory: %s/%s kb   Gamemode: %s" % (self.sdata["players"],self.sdata["max"],self.sdata["players"],self.sdata["bots"],self.sdata["uptime"],self.sdata["mem"],self.sdata["maxmem"],self.sdata["gamemode"]))
        if self.isexit == False: #while that other stuff is happening we could have exited
            root.after(1000,self.update)

    def addbotf(self,e):
        self.ocl.addBot()

    def pausef(self,e):
        self.ocl.pause()

    def reloadf(self,e):
        self.ocl.reloadConfig()

    def randomfood(self):
        self.frx = random.randint(int(self.config.getVal('borderleft')),int(self.config.getVal('borderright')))
        self.fry = random.randint(int(self.config.getVal('bordertop')),int(self.config.getVal('borderbottom')))
        self.frm = random.randint(1,5)

        self.foodx.set(str(self.frx))
        self.foody.set(str(self.fry))
        self.foodm.set(str(self.frm))

    def getcolor(self,e):
        (self.rgb,self.hx) = askcolor()
        self.colorv.set(self.hx)

    def setcolor(self,e):
        self.hx = self.hx[1:7]
        self.rhx = (int(self.hx[0:2],16),int(self.hx[2:4],16),int(self.hx[4:6],16))
        self.rhx = (str(self.rhx[0]),str(self.rhx[1]),str(self.rhx[2]))
        self.ocl.color(self.playerlist.selection()[0],self.rhx)

    def randomvirus(self):
        self.rx = random.randint(int(self.config.getVal('borderleft')),int(self.config.getVal('borderright')))
        self.ry = random.randint(int(self.config.getVal('bordertop')),int(self.config.getVal('borderbottom')))
        self.rm = random.randint(0,200)

        self.virusx.set(str(self.rx))
        self.virusy.set(str(self.ry))
        self.virusm.set(str(self.rm))

    def kill(self,e):
        print(self.playerlist.selection()[0])
        self.ocl.kill(self.playerlist.selection()[0])
        self.playerlist.delete(self.playerlist.selection()[0])

    def killall(self,e):
        self.ocl.killAll()
        for i in self.playerlist.get_children():
            self.playerlist.delete(i)

    def kick(self,id):
        self.ocl.kick(self.playerlist.selection()[0])
        self.playerlist.delete(self.playerlist.selection()[0])

    def exit(self,e):
        self.isexit = True
        self.ocl.oexit()
        root.destroy()

    def boardf(self,e):
        self.ocl.board(self.boardtv.get())
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Ogui")
    app = App(master=root)
    app.update()
    app.mainloop()