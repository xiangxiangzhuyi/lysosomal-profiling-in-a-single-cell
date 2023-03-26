# lysosomal profiling in a single cell

The single-cell lysosomal profiling tool is a user-friendly and straightforward Python-based tool that offers a comprehensive analysis of lysosomes in individual cells. The tool involves four main steps, starting with the segmentation of lysosomes and the cell membrane from the background. This critical step enables accurate analysis of lysosomes in subsequent steps.

After segmenting the lysosomes and cell membrane, the tool calculates the area of each lysosome and the maximum, mean, and standard deviation of pixel values in the region of each lysosome. These measurements offer valuable insight into the content and function of lysosomes.

The third step involves calculating the distance between each lysosome and the cell membrane. This information is useful in understanding lysosomal distribution and location within the cell.

Next, the lysosomes are marked, and the marked number is added to the image. The images are then saved in a separate folder for future reference. Finally, all information about each lysosome is saved to an Excel file for easy data management and further analysis.

Overall, this tool provides researchers with a comprehensive analysis of lysosomes in single cells and can be a valuable resource for studying lysosomal dynamics and function.

## Required python packages
- cv2
- numpy
- argparse
- pandas
- matplotlib

## Prepare your data
- put all images that need to be processed to a specific folder
- in each image, the lysosome in the green color, and the cell membrane in the white color.
- create a folder to storage the marked image and the excel file.

## set configuration
in the `bash main.py`, to set the configuration based on your data.
```bash
parser.add_argument('--file_path', dest='file_path', default='./control/', nargs='+', help='the path of storing your image file')
parser.add_argument('--output_path', dest='output_path', default='./saved_control/', nargs='+', help='the path of saving the marked image')
parser.add_argument('--pixel_width', dest='pixel_width', type=float, default=0.1, help='the width of pixel in the real space')
parser.add_argument('--threshold', dest='threshold', type=float, default=20, help='the threshold of pixel value to extract the component')
```
