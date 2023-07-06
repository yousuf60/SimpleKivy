# SimpleKivy

```bash
pip install simplekivy
```

### Perfect versions:
-------
* [kivy==2.2.1]("https://pypi.org/project/Kivy/2.2.1/") 
* python >= 3.7


simplekivy is built on kivy to write simple code faster

you can write kvlang and creat your own classes and widgets as kivy is flexible

the widgets are added only once via simpleKivyObject + [

#kv_widgets

]

### Examples to test:
-----

```python

from simplekivy import SimpleKivy
s = SimpleKivy(title="test")
dp = s.metrics.dp
s + [
    (# floatlayout <=> ()
        {"size_hint": (1, 1)},#<=> add the floatlayout kwargs
        s.Label(text="ffljwfe", pos_hint={"center_x":.5, "center_y":.5}),
        {"height":  dp(100)}, #kwargs
    ),
    [ #boxlayout <=> []
        {"size_hint": (1, .5)},
        s.Button(text="gdddg"),
        s.Button(text="gdgdd")
    ],
    
 
]


```


```python
from simplekivy import SimpleKivy

s = SimpleKivy(title="test app")

dp = s.metrics.dp
inp1 = s.TextInput(size_hint=(.5, None), height=dp(50), pos_hint={"center_x":.5})
inp1_button = s.Button(text="click", on_press=lambda x:print(inp1.text),
                    size_hint=(.5, None), height=dp(50),
                    pos_hint={"center_x":.5})

s + [
    (#floatlayout
        {"size_hint":(1, 1)},
        [#boxlayout
            {"orientation":"vertical", "size_hint":(1, None), "height":dp(200),
            "spacing":"60dp","pos_hint":{"center_y":.5}},
            inp1, 
            inp1_button])
]

```



```python
from simplekivy import SimpleKivy
def on_enter(instance):
    print(instance.text)
    
s = SimpleKivy(title="test app")

ainput = s.TextInput(multiline=False,  size_hint=(1, None),
     height="50dp", pos_hint={"center_x":.5, "center_y":.7})

ainput.bind(on_text_validate=on_enter)

s + [
    [{"orientation":"vertical", "size_hint":(1, .4)},
    s.Label(text="hello world", halign="center"),
    s.Label(text="testo")],
    ({"size_hint":(.4, .6), "pos_hint":{"center_x":.5}},
        ainput
    )
]
```
<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/997481b1-20cb-4571-91f5-fed311f6f7bc" width="500">



you can also add kvlang string directly instead of using 
`s.lang.Builder`
or `kivy.lang.Builder`

```python
from simplekivy import SimpleKivy
s = SimpleKivy(title="test app")

def on_enter(instance):
    print(instance.text)
    
def btn_pressed():
    print(ainput.text)


#add a new method to app
s.myapp.btn_pressed = btn_pressed

KV_BTN = """

Button:
    text: "press me"
    size_hint:.4, .1
    pos_hint: {"center_x": .5}
    on_press:app.btn_pressed()
"""
ainput = s.TextInput(hint_text="type anything", multiline=False,  size_hint=(1, None),
     height="50dp", pos_hint={"center_x":.5, "center_y":.7})

ainput.bind(on_text_validate=on_enter)

s + [
    [{"orientation":"vertical", "size_hint":(1, .4)},
    s.Label(text="hello world", halign="center"),
    s.Label(text="testo")],
    ({"size_hint":(.4, .4), "pos_hint":{"center_x":.5}},
        ainput 
    ),
    ({"size_hint": (1, .2)},
        KV_BTN),
]

```

<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/9e9e445e-0c6f-45de-9580-cd7fbde1f010" width="500">

### Hints
------

- list => BoxLayout
- tuple => FloatLayout
- the more you understand kivy, the more you enjoy its flexibility

