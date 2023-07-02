# SimpleKivy

### Requirements:
-------
* [kivy]("https://github.com/kivy/kivy") 


you are using kivy but via simplekivy to write simple python code faster

you can build kvlang and creat your own classes and widgets

the widgets are added only once via simpleKivyObject + [

#kv_widgets

]

### Examples to test:
-----
```python
from simplekivy import SimpleKivy
s = SimpleKivy(title="test")
s + [[ # boxlayout <=> list[]
        s.Button(text="gdddg"),
        s.Button(text="gdgdd")],
    (# floatlayout <=> tuple()
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
    (# floatlayout <=> tuple
        {"size_hint": (1, None)},#<=> add the floatlayout kwargs
        s.Label(text="ffljwfe", pos_hint={"center_x":.1, "center_y":.5}),
        {"height":  dp(100)}, #kwargs
    ),
    [ #boxlayout
        {"size_hint": (.5, .4)},
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


### Hints
------

- list => BoxLayout
- tuple => FloatLayout
- the more you understand kivy, the more you enjoy its flexibility


