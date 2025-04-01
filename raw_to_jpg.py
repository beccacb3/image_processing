import rawpy
import imageio
import os
import argparse

in_path = '.'
out_path = '.'

def raw_to_jpg(filename, output_dir):
    status = True
    raw_path = "input.raw"
    output_path = "output.jpg"

    with rawpy.imread(raw_path) as raw:
        rgb_image = raw.postprocess()
        # imageio.imwrite(output_path, rgb_image, format='JPEG', quality=95)
        print("Conversion complete:", output_path)
    return status

def raw_dir():
    status = True
    raw_to_jpg()
    return status

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process input parameters.")
    parser.add_argument('--in_path', type=str, required=True, help='Path of Raw Files')
    parser.add_argument('--out_path', type=str, required=False, help='Path of Raw Files')

    args = parser.parse_args()
    in_path = args.in_path

    if not args.out_path:
        out_path = './jpg_conversion' + '/' + in_path.split('/')[-1] + '/'
        print(f"No output path defined as a parameter, creating path {out_path}")
    else:
        out_path = args.out_path

    os.makedirs(out_path, exist_ok=True)
    print(f"Created path: '{out_path}'")

parse_arguments()


#TODO: run in parallel
#add file error handling 
