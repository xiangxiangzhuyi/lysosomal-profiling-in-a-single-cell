# lysosomal profiling in a single cell

![Picture1](https://user-images.githubusercontent.com/15710573/227761493-1b825e38-ff8b-4c6e-8874-721478fc808f.png)
The single-cell lysosomal profiling tool is a user-friendly and straightforward Python-based tool that offers a comprehensive analysis of lysosomes in individual cells. The tool involves four main steps, starting with the segmentation of lysosomes and the cell membrane from the background. This critical step enables accurate analysis of lysosomes in subsequent steps.

After segmenting the lysosomes and cell membrane, the tool calculates the area of each lysosome and the maximum, mean, and standard deviation of pixel values in the region of each lysosome. These measurements offer valuable insight into the content and function of lysosomes.

The third step involves calculating the distance between each lysosome and the cell membrane. This information is useful in understanding lysosomal distribution and location within the cell.

Next, the lysosomes are marked, and the marked number is added to the image. The images are then saved in a separate folder for future reference. Finally, all information about each lysosome is saved to an Excel file for easy data management and further analysis.

Image file name	Component id	Area	Maximum intensity value	Average intensity value	Intensity value standard deviation	Distance to cell membrane
1.png	1	0.09	63	45.44444444	9.82187028	2.828427125
1.png	2	0.15	82	55.26666667	18.53453234	6.356099433
1.png	3	0.15	84	51.33333333	20.46351767	7.736924454
1.png	4	0.73	172	99.32876712	47.3442811	1.264911064
1.png	5	0.25	99	60.72	22.65483613	4.10487515
1.png	6	0.45	205	102.8222222	54.158323	2.121320344
1.png	7	0.24	104	67.45833333	21.16203197	0.854400375
1.png	8	0.27	107	64.18518519	24.54178151	3.818376618
1.png	9	0.23	105	62.91304348	26.57869864	3.46554469
1.png	10	0.18	118	59.83333333	30.06890236	0.141421356
1.png	11	0.22	255	119.8636364	69.78883439	1.923538406
![image](https://user-images.githubusercontent.com/15710573/227761507-d7fccda6-3ae3-4fa8-a1dd-f35698fc728b.png)


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
in the `main.py`, to set the configuration based on your data.
```bash
parser.add_argument('--file_path', dest='file_path', default='./control/', nargs='+', help='the path of storing your image file')
parser.add_argument('--output_path', dest='output_path', default='./saved_control/', nargs='+', help='the path of saving the marked image')
parser.add_argument('--pixel_width', dest='pixel_width', type=float, default=0.1, help='the width of pixel in the real space')
parser.add_argument('--threshold', dest='threshold', type=float, default=20, help='the threshold of pixel value to extract the component')
```

## run the tool
```bash
python main.py
```
