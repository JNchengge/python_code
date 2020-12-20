import time
class Player:
    def __init__(self):
        self.playlist={0:['Lose Yourself','Eminem'],
        1:['Natural','Imagine Dragons'],
        2:['No Rain','Doggie']}
        self.now=0
    def play(self):
        print("Playing:",self.playlist[self.now][0],"————",self.playlist[self.now][1]+"......")
    def pause(self):
        print("Pause!")
    def next(self):
        self.now=(self.now+1)%(len(self.playlist))
        print("Playing:",self.playlist[self.now][0],"————",self.playlist[self.now][1]+"......")
    def forward(self):
        self.now=(self.now-1)%(len(self.playlist))
        print("Playing:",self.playlist[self.now][0],"————",self.playlist[self.now][1]+"......")
player=Player()
while True:
    select=int(input("请输入你的选择：1.播放；2.暂停；3.下一首；4.上一首；0.退出\n"))
    if select==1:
        player.play()
    elif select==2:
        player.pause()
    elif select==3:
        player.next()
    elif select==4:
        player.forward()
    elif select==0:
        print("退出！")
        exit(0)
    else:
        print("请重新输入！")