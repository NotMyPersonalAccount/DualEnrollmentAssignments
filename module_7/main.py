from tiger import Tiger

tiger_properties = {
    "Amy": 0,
    "Jose": 5,
    "Konnor": 1,
    "Marc": 1,
    "Richard": 7
}
tigers = []
for name, stripes in tiger_properties.items():
    tigers.append(Tiger(name, stripes))
