from PIL import Image
import glob
import os


def phoToGif(path, new_path):
    fileList = os.listdir(path)
    frames = []
    duration = int(input("duration:(second)"))
    #find the files with same name
    detect = os.listdir(path)[0][:os.listdir(path)[0].find('(')]
    d = 0
    for i in fileList:
        print('processing in '+i)

        #create a gif when meet photo with not same name
        if detect not in i:
            frames[0].save(new_path + os.sep + detect + '.gif', format='GIF',
                           append_images=frames[1:],
                           save_all=True,
                           duration=duration*1000, loop=0)
            detect = i[:i.find('(')]
            frames.clear()
            d=0

        #add a photo to frame
        if 'jpg' in i or 'png' in I:
            frames.append(Image.open(path + os.sep + i))
            d += 1

    #create gif for the photos still in the frame
    frames[0].save(new_path + os.sep + detect + '.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=duration*1000, loop=0)
    print("done")

#get the path and create a new folder for gif
path = input('path：')
fileList = os.listdir(path)
new_path = path + '-save'
os.makedirs(new_path)

phoToGif(path, new_path)

a= input("any key to exit")
