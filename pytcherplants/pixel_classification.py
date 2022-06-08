from os.path import join
from pathlib import Path
import subprocess

import numpy as np
import cv2


def renormalize(image: np.ndarray) -> np.ndarray:
    img = image.copy()
    img[img > 1] = 0
    img[img == 1] = 255
    return img


def ilastik_classify(input_file_path: str, output_directory_path: str):
    command = f"/opt/ilastik/ilastik-1.4.0b21-gpu-Linux/run_ilastik.sh --headless " + \
              "--project=/opt/pytcherplants/pytcherplants.ilp " + \
              "--output_format=tiff " + \
              f"--output_filename_format={output_directory_path}/" + "{nickname}.segmented.tiff " + \
              "--export_source='Simple Segmentation'" + \
              f" {input_file_path}"
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)


def postprocess(
        input_file_path: str,
        mask_file_path: str,
        output_directory_path: str):
    """
    Post-processes the results of ilastik pixel segmentation.
    Converts [1-2] masks to [0-255] and applies mask to original image to segment foreground.

    :param input_file_path: The input image path
    :param mask_file_path: The path to the mask file produced by ilastik pixel classification
    :param output_directory_path: The output directory path
    :return: A 2-tuple containing 1) the post-processed mask and 2) segmented original image with the mask applied
    """

    orig_img = cv2.imread(input_file_path).copy()
    mask_img = cv2.imread(mask_file_path).copy()

    # ilastik pixel segmentation returns [1, 2], with 1=foreground & 2=background
    # we want to convert this to 0=background, 255=foreground
    mask = renormalize(mask_img)
    cv2.imwrite(join(output_directory_path, f"{Path(mask_file_path).stem}.mask.jpg"), mask)

    # apply the mask to the original image
    masked = cv2.bitwise_and(orig_img, mask)
    cv2.imwrite(join(output_directory_path, f"{Path(input_file_path).stem}.masked.jpg"), masked)

    return mask, masked
