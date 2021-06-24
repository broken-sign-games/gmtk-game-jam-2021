from PIL import Image
with Image.open(input("Enter Filename")) as im:
    width, height = im.size
    obstr = ""
    legendstr = "image = "
    levelstr =("."*(width // 5) + "\n")*(height//5)
    rulestr = "[x0y0" + ("|" * ((width//5)-1)) + "] -> [" + "".join(map(lambda x: "x" + str(x) + "y0|",range(width//5)))[:-1] + "]\n"
    for x in range(width // 5):
        rulestr += "[x" + str(x) + "y0" + ("|" * ((height//5)-1)) + "] -> ["
        for y in range(height // 5):
            rulestr += "x" + str(x) + "y" + str(y) + "|"
            local = im.crop((5*x,5*y,5*(x+1),5*(y+1)))
            colors = []
            area = []
            data = list(local.getdata())
            for color in data:
                if color in colors:
                    area.append(colors.index(color))
                else:
                    if len(colors) == 10:
                        area.append(0)
                    else:
                        colors.append(color)
                        area.append(len(colors) - 1)
            obstr += "x" + str(x) + "y" + str(y) + "\n"
            for color in colors:
                obstr += "#" + "".join(map(lambda x: hex(x)[2:],color[:-1])) + " "
            obstr += "\n"
            for i in range(5):
                obstr += "".join(map(str,area[5*i : 5 * (i+1)])) + "\n"
            obstr += "\n"
            legendstr += "x" + str(x) + "y" + str(y) + " or "
        rulestr = rulestr[:-1] + "]\n"
    legendstr = legendstr[:-4] + "\n"

    print( obstr, legendstr, levelstr, rulestr)
        
