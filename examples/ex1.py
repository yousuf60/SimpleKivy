from simplekivy import SimpleKivy
s = SimpleKivy(title="Hello world")

s + [
    s.Label(text="hello world!", color=(0,0,0,1)),
    s.Button()
]