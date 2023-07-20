# SimpleKivy

```bash
pip install simplekivy
```

### Perfect versions:
-------
* [kivy==2.2.1]("https://pypi.org/project/Kivy/2.2.1/") 
* python >= 3.7


simplekivy is built with kivy to write quickly simple codes

you can write kvlang and creat your own classes and widgets as kivy is flexible

the widgets are added only once via simpleKivyObject + [

#kv_widgets

]

and you can build simplekivy way using `s.build`

### Examples to test:
-----

```python
from simplekivy import SimpleKivy
s = SimpleKivy(title="test app")
dp = s.metrics.dp

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

text_input =  s.TextInput(hint_text="type", size_hint=(.5, None), height=dp(60), pos_hint={"center_x":.5})
btn = s.Button(text = "click", size_hint=(.4, .2), pos_hint={"center_x":.5, "center_y":.5}, on_press=pressed)
label =  s.Label(text = "type")

# you don't really need to build here and can just pass the list .. 
# but iam showing you how to get objets using s.build
# so you may need it somewhere else
front = s.build([{"orientation":"vertical"},
                text_input,
                (btn,),
                label            
])

s + [(background,
front
)
]

```

```python

from simplekivy import SimpleKivy
s = SimpleKivy(title="test app")
screen_manager = s.ScreenManager()

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
    left = s.Button(text="left")
    right = s.Button(text="right")
    screen = ScreenI(name=str(i))
    left.on_press = screen.left
    right.on_press = screen.right
    scr[screen] = [{"orientation":"vertical"},s.Label(text=str(i)),[ left, right]]

manager[screen_manager] = scr
s + [
    manager
]

```
### Hints
------

- list => BoxLayout
- tuple => FloatLayout
- set `make_app` to `False` if you do not want to run the kivy App 
```python
s = SimpleKivy(make_app=False)
```
- to reach the main App object do `s.myapp`
- you can pass to `s.build` a `list, tuple, dict, set and kivy lang string`
- the more you understand kivy, the more you enjoy its flexibility

----


<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/5905a746-8278-4471-b1e3-d85b7eb5eec6" width="400">


<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/f2abb219-55c1-4e9e-a9e9-e46346d6176f" width="400">