""" 
This script convert Thorlabs raw data files to a format that can be used with CaImAn: tiff files.

To not conflict with the CaImAn environment, please create a new dedicatedone:

mamba create -n convert_thorlabs python=3.8 tifffile ipykernel -y
mamba activate convert_thorlabs
pip install utils2p

"""
# %% IMPORTS
import os
from pathlib import Path
import tifffile
import utils2p
# %% MAIN
# adjust the path to the raw image file:
raw_image_file_path = "/Users/husker/Workspace/Test Images/Thorlabs RAW/Ch1/Image_0001_0001.raw"


# don't change the following lines:
raw_image_file_path_parent = os.path.dirname(raw_image_file_path)
outdir = os.path.dirname(raw_image_file_path)
tif_filename = os.path.basename(raw_image_file_path).replace('.raw', '.tif')
tif_file_path = os.path.join(outdir, tif_filename)

if Path(raw_image_file_path).suffix != '.raw':
        raise ValueError(f"Unknown file extension (should be .raw, not {Path(raw_image_file_path).suffix})")


path_to_metadata_file = utils2p.find_metadata_file(raw_image_file_path_parent)
metadata = utils2p.Metadata(path_to_metadata_file)

stack = utils2p.load_raw(raw_image_file_path, metadata)[0]
print(f"Shape of the raw image stack: {stack.shape} and type: {stack.dtype}")

# save stack as tiff file:
tifffile.imwrite(tif_file_path, stack)

# %% END