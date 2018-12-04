import re
tottal = 0

with open('fabric.txt', 'r+') as f:
    text = [linia.rstrip() for linia in f]

for size in text:
    structure = r"(\d{1,2})x(\d{1,2})x(\d{1,2})"
    m = re.search(structure, size)
    if m:
        l = m.group(1)
        w = m.group(2)
        h = m.group(3)
        if int(l)*int(w) <= int(w)*int(h) <= int(h)*int(l) or int(l)*int(w) <= int(h)*int(l) <= int(w)*int(h):
            surface = (2*int(l)*int(w)) + (2*int(w)*int(h)) + (2*int(h)*int(l)) + int(l)*int(w)
            tottal += surface
        elif int(w)*int(h) <= int(l)*int(w) <= int(h)*int(l) or int(w)*int(h) <= int(h)*int(l) <= int(l)*int(w):
            surface = (2*int(l)*int(w)) + (2*int(w)*int(h)) + (2*int(h)*int(l)) + int(w)*int(h)
            tottal += surface
        elif int(h)*int(l) <= int(l)*int(w) <= int(w)*int(h) or int(h)*int(l) <= int(w)*int(h) <= int(l)*int(w):
            surface = (2*int(l)*int(w)) + (2*int(w)*int(h)) + (2*int(h)*int(l)) + int(h)*int(l)
            tottal += surface

print(tottal)
