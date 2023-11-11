from simplekivy import SimpleKivy
s = SimpleKivy(md_mode = True, title="test app")
dp = s.metrics.dp
print(s.build([]), s.MDLabel)
def pressed(instance):
    if text_input.text:
        label.text = text_input.text

background = """
BoxLayout:
    canvas:
        Color:
            rgba: 0, 0, .9, .7
        Rectangle:
            pos: self.pos
            size: self.size

"""

text_input =  s.STextInput(hint_text="type", size_hint=(.5, None), height=dp(60), pos_hint={"center_x":.5})
btn = s.SButton(text = "click", size_hint=(.4, .2), pos_hint={"center_x":.5, "center_y":.5}, on_press=pressed)
label =  s.SLabel(text = "type")
front = s.build([{"orientation":"vertical"},
                text_input,
                (btn,),
                label
                
])



s + [(background,
front
)
]


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
    scr[screen] = [{"orientation":"vertical"},s.SLabel(text=str(i)),[ left, right]]

manager[screen_manager] = scr

s + [
    manager
]

s + [
    [(s.build({s.Screen():{s.SLabel(text="weg")}}))]
]