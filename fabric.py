import re
total = 0
ribon = 0

with open('fabric.txt', 'r+') as f:
    text = [linia.rstrip() for linia in f]

for size in text:
    structure = r"(\d{1,2})x(\d{1,2})x(\d{1,2})"
    m = re.search(structure, size)
    if m:
        l = int(m.group(1))
        w = int(m.group(2))
        h = int(m.group(3))
        equation = (2 * l * w) + (2 * w * h) + (2 * h * l)
        if l*w <= w*h <= h*l or l*w <= h*l <= w*h:
            total += equation + l*w
            ribon += 2*l + 2*w + l*w*h

        elif w*h <= l*w <= h*l or w*h <= h*l <= l*w:
            total += equation + w*h
            ribon += 2 * w + 2 * h + l*w*h
        elif h*l <= l*w <= w*h or h*l <= w*h <= l*w:
            total += equation + h*l
            ribon += 2 * h + 2 * l + l*w*h

print(total)
print(ribon)

