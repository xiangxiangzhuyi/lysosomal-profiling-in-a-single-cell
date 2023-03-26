import argparse
import lysosomal_profiling as lypro
import pandas as pd
import matplotlib.pyplot as plt

# set configuration
parser = argparse.ArgumentParser()
parser.add_argument('--file_path', dest='file_path', default='./control/', nargs='+', help='the path of storing your image file')
parser.add_argument('--output_path', dest='output_path', default='./saved_control/', nargs='+', help='the path of saving the marked image')
parser.add_argument('--pixel_width', dest='pixel_width', type=float, default=0.1, help='the width of pixel in the real space')
parser.add_argument('--threshold', dest='threshold', type=float, default=20, help='the threshold of pixel value to extract the component')
parser = parser.parse_args()

# read image files
img_li = lypro.read_iamges(parser.file_path)

# processing
all_info = []
for img in img_li:
    cm_mask, cm_mask_edg, ls_mask, ls_mask_edg, ls_labels, ls_labels_edg, info_li = lypro.get_info(img[1], parser.pixel_width, parser.threshold)
    te_img = lypro.add_text(img[1], ls_labels)
    all_info += [[img[0]] + x for x in info_li]
    plt.imsave(parser.output_path + img[0], te_img)

# save as Excel file
df = pd.DataFrame(all_info, columns=['Image file name', 'Component id', 'Area', 'Maximum intensity value', 'Average intensity value', 'Intensity value standard deviation', 'Distance to cell membrane'])
df.to_excel(parser.output_path + 'information.xlsx')