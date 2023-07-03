# SimpleKivy

### Perfect versions:
-------
* [kivy==2.2.1]("https://pypi.org/project/Kivy/2.2.1/") 


simplekivy is built on kivy to write simple code faster

you can write kvlang and creat your own classes and widgets as kivy is flexible

the widgets are added only once via simpleKivyObject + [

#kv_widgets

]

### Examples to test:
-----


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
<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/03157293-fb68-4d2f-8234-807ffa9df560" width="500">


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
<img src="https://github.com/yousuf60/SimpleKivy/assets/64571068/3eded17a-e691-4b5f-9597-eaca67bba5d0" width="500">




```python
from simplekivy import SimpleKivy
s = SimpleKivy(title="test")
s + [[ # boxlayout <=> list  []
        s.Button(text="gdddg"),
        s.Button(text="gdgdd")],
    (# floatlayout <=> tuple  ()
        s.Label(text="ffljwfe", pos_hint={"center_x":.1, "center_y":.5}),
        s.Label(text="ffljwfe", pos_hint={ "center_y":.5}),),
        [s.Button(text="third button"), s.Label(text="third button")],
        [s.Button(text="third button"), s.Button(text="third button")
    ],
]

```

```python

from simplekivy import SimpleKivy
s = SimpleKivy(title="test")
dp = s.metrics.dp
s + [
    (# floatlayout <=> ()
        {"size_hint": (1, None)},#<=> add the floatlayout kwargs
        s.Label(text="ffljwfe", pos_hint={"center_x":.1, "center_y":.5}),
        {"height":  dp(100)}, #kwargs
    ),
    [ #boxlayout <=> []
        {"size_hint": (.5, .4)},
        s.Button(text="gdddg"),
        s.Button(text="gdgdd")
    ],
    
 
]


```

### Hints
------

- list => BoxLayout
- tuple => FloatLayout
- the more you understand kivy, the more you enjoy its flexibility

