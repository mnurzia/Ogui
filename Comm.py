#/Library/Frameworks/Python.framework/Versions/3.4/bin/python3i
import pexpect,sys,re
import tkinter as tk

class OgarTerm:
    """Class to communicate with Ogar."""

    def __init__(self,cons):
        self.STATS_REGEX = re.compile(r".*: (?P<online>\d*).(?P<max>\d*).*: *(?P<players>\d*).*: *(?P<bots>\d*).* (?P<uptime>\d*) seconds.*: (?P<mem>[\d.]*).(?P<maxmem>[\d.]*) kb.*: (?P<gamemode>[^\n]*)",flags=re.S)
        self.PLIST_REGEX = re.compile(r"( *(?P<id>\d*) [|] (?P<ip>\S*) *[|] (?P<name>[^|]*)[|] *(?P<cells>\d*) [|] *(?P<score>\d*) [|] *(?P<x>\d*), *(?P<y>\d*)|(?P<donp>.*))")
        self.ogarCL = pexpect.spawn('node Ogar')
        self.cons = cons
        #time.sleep(0.01)
        self.ogarCL.expect('>')

    def insertConsole(self,t,tg):
        self.cons["state"] = tk.NORMAL
        self.cons.insert(tk.END,t,tg)
        self.cons["state"] = tk.DISABLED

    def runComm(self,command):
        self.ogarCL.sendline(command)
        #time.sleep(0.01)
        self.ogarCL.expect('>')

    def addBot(self,n=1):
        print('addbot '+str(n))
        self.insertConsole("[CONSOLE] Adding "+str(n)+" bots\n",("console"))
        self.runComm('addbot '+str(n))

    def board(self,string):
        print('board '+string)
        self.insertConsole("[SERVER ] Setting board text to "+string+'\n',("server"))
        self.runComm('board '+string)

    def boardReset(self,e):
        print('boardreset')
        self.insertConsole("[SERVER ] Resetting board text\n",("server"))
        self.runComm('boardreset')

    def change(self,c,v):
        print('change '+c+' '+v)
        self.insertConsole("[SERVER ] Changing server variable "+c+" to "+v+'\n',("server"))
        self.runComm('change '+c+' '+v)

    def color(self,id,c):
        print('color %s %s %s %s' % (id,c[0],c[1],c[2]))
        self.insertConsole("[CONSOLE] Setting color of cell "+id+" to "+c[0]+","+c[1]+","+c[2]+"\n",("console"))
        self.runComm('color %s %s %s %s' % (id,c[0],c[1],c[2]))

    def oexit(self):
        print('exit')
        self.ogarCL.terminate()

    def food(self,x,y,m):
        print('food %s %s %s' % (str(x),str(y),str(m)))
        self.insertConsole("[CONSOLE] Spawning food at "+str(x)+", "+str(y)+" with mass "+str(m)+"\n",("console"))
        self.runComm('food %s %s %s' % (str(x),str(y),str(m)))

    def kick(self,id):
        print('kick '+str(id))
        self.insertConsole("[CONSOLE] Kicking player "+str(id)+"\n",("console"))
        self.runComm('kick '+str(id))

    def kill(self,id):
        print('kill '+str(id))
        self.insertConsole("[CONSOLE] Killing player "+str(id)+"\n",("console"))
        self.runComm('kill '+str(id))

    def killAll(self):
        print('killall')
        self.insertConsole("[SERVER ] Killing all players...\n",("server"))
        self.runComm('killall')

    def mass(self,id,m):
        print('mass '+str(id)+' '+str(m))
        self.insertConsole("[CONSOLE] Setting mass of player "+str(id)+" to "+str(m)+"\n",("console"))
        self.runComm('mass '+str(id)+' '+str(m))

    def name(self,id,n):
        print('name '+str(id)+' '+str(n))
        self.runComm('name '+str(id)+' '+str(n))

    def pause(self):
        print('pause')
        self.insertConsole("[SERVER ] Pausing server...\n",("server"))
        self.runComm('pause')

    def playerList(self):
        self.runComm('playerlist')
        self.plrd = self.ogarCL.before.decode('utf-8').split('\n')
        self.plrd = self.plrd[4:]
        del self.plrd[-1]
        for player in range(0,len(self.plrd)):
            self.plrd[player] = self.PLIST_REGEX.match(self.plrd[player]).groupdict()
        return self.plrd

    def reloadConfig(self):
        print('reload')
        self.insertConsole("[SERVER ] Reloading config...",("server"))
        self.runComm('reload')
        self.insertConsole(" done.\n",("server"))

    def status(self):
        self.runComm('status')
        return self.STATS_REGEX.match(self.ogarCL.before.decode('utf-8')).groupdict()

    def tp(self,id,x,y):
        print('tp '+str(id)+' %i %i' % (x,y))
        self.insertConsole("[CONSOLE] Teleporting player "+str(id)+ " to "+str(x)+", "+str(y)+"\n",("console"))
        self.runComm('tp '+str(id)+' %i %i' % (x,y))

    def virus(self,x,y,m):
        print('virus %s %s %s' % (str(x),str(y),str(m)))
        self.insertConsole("[CONSOLE] Adding virus at "+str(x)+", "+str(y)+" with mass "+str(m)+"\n",("console"))
        self.runComm('virus %s %s %s' % (str(x),str(y),str(m)))

    def interact(self):
        self.ogarCL.interact()

    def exit():
        self.runComm('exit')

if __name__ == '__main__':
    o = OgarTerm()
    o.addBot(8)
    print(o.playerList())

