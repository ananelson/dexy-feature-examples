import json

with open("example.json", "w") as f:
    json.dump({"foo" : "bar"}, f)
