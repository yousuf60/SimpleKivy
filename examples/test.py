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
