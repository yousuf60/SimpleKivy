from simplekivy import SimpleKivy
s = SimpleKivy(title="Hello world")

s + [
    s.SLabel(text="hello world!", color=(0,0,0,1))
]