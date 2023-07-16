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

box = s.build([s.Label(text="qf47", pos_hint={"center_y": .8})])
floatL = s.build("""
FloatLayout:
    
    Button:
        text:"test"
        size_hint:.3, .2
        pos_hint: {"center_y": .8}
""")
s + [(
    {s.BoxLayout: box,
    s.BoxLayout(size_hint=(None, None)): [s.Label(text="qfe")],
    floatL: s.Label(text="testo testo"),
    },)
]
#as you know for python dict .. key "objects" should be different objects

```

```python

from simplekivy import SimpleKivy
s = SimpleKivy(title="test")
dp = s.metrics.dp
s + [
    (# floatlayout <=> ()
        {"size_hint": (1, None)},#<=> add the floatlayout kwargs
        s.Label(text="ffljwfe", pos_hint={"center_x":.5, "center_y":.5}),
        {"height":  dp(200)}, #kwargs as you want will be added 
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

you can also add kvlang string directly instead of using 
`s.lang.Builder`
or `kivy.lang.Builder` or `s.build`

```python
from simplekivy import SimpleKivy
s = SimpleKivy(title="test app", make_app=True)

def on_enter(instance):
    print(instance.text)
    
def btn_pressed():
    print(ainput.text)


#add a new method to app
s.myapp.btn_pressed = btn_pressed

KV_BTN = """

Button:
    text: "press me"
    size_hint:.4, .2
    pos_hint: {"center_x": .5, "center_y": .5}
    on_press:app.btn_pressed()
"""
ainput = s.TextInput(hint_text="type anything", multiline=False,  size_hint=(1, None),
     height="50dp", pos_hint={"center_x":.5, "center_y":.7})

ainput.bind(on_text_validate=on_enter)

s + [
    [{"orientation":"vertical", "size_hint":(1, .2)},
    s.Label(text="hello world", halign="center"),
    s.Label(text="testo")],
    ({"size_hint":(.4, .4), "pos_hint":{"center_x":.5}},
        ainput 
    ),
    ({"size_hint": (1, .4)},
        KV_BTN),
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
- you can pass to `s.build` a `list, tuple, dict and kivy lang string`
- the more you understand kivy, the more you enjoy its flexibility

----

<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/997481b1-20cb-4571-91f5-fed311f6f7bc" width="300">

<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/9e9e445e-0c6f-45de-9580-cd7fbde1f010" width="300">
