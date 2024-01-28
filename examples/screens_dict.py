from simplekivy import SimpleKivy
s = SimpleKivy(title="test app")

screen_manager =s.ScreenManager()
class ScreenI(s.Screen):
    def left(self):
        print("------", self, self.name)
        screen_manager.transition.direction = "right"
        screen_manager.current = screen_manager.previous()

    def right(self):
        print("------", self, self.name)
        screen_manager.transition.direction = "left"
        screen_manager.current = screen_manager.next()

manager = {screen_manager: None}
scr = {}
for i in range(4):
    left = s.SButton(text="left")
    right = s.SButton(text="right")
    screen = ScreenI(name=str(i))
    left.on_press = screen.left
    right.on_press = screen.right
    scr[screen] = [{"orientation":"vertical"},s.SLabel(text=str(i)),[left, right]]

manager[screen_manager] = scr

s + [
    manager
]
