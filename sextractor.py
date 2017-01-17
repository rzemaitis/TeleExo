#Read lines without comments
with open("filename") as f:
    for line in f:
        line = line.split('#', 1)[0]
        line = line.rstrip()
