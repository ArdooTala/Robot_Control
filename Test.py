from libxmp.utils import file_to_dict
import os


def copyXMP(path):
    with open(path+'/meta.txt', 'w') as txt_file:

        for root, dirs, files in os.walk(path):
            for file in files:
                if not file.endswith('jpg'): continue
                print(file)
                file = os.path.join(root, file)
                txt_file.write(file)
                txt_file.write('\n')
                xmp = file_to_dict(file)
                for x, y in xmp.items():
                    for z in y:
                        txt_file.write(z[0])
                        txt_file.write(' : ')
                        txt_file.write(z[1])
                        txt_file.write('\n')

                txt_file.write("-"*30)
                txt_file.write('\n')



copyXMP('/home/ardoo/Desktop/JPGS/')