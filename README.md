# SimpleKivy

### requirements:
-------
* [kivy]("https://github.com/kivy/kivy") 


you are using kivy but via simplekivy to write simple python code faster

you can build kvlang and creat your own classes and widgets

the widgets are added only ones via simpleKivyObject + [

]

example code:
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
    [s.Button(text="third button"), s.Button(text="third button")],
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
    s.Button(text="gdddg"),
    s.Button(text="gdgdd")
    ],
    
 
]

```


list => BoxLayout
tuple => FloatLayout