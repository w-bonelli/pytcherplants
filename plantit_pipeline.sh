# ilastik pixel segmentation
/opt/ilastik/ilastik-1.4.0b21-gpu-Linux/run_ilastik.sh --headless --project=/opt/pytcher-plants/pitcherplants.ilp --output_format=tiff --output_filename_format=$OUTPUT/{nickname}_segmented.tiff --export_source="Simple Segmentation" $INPUT

# aggregate color analysis and trait measurement
python3 /opt/pytcher-plants/pytcher_plants/base.py process -i $INPUT -o $OUTPUT

# TODO ilastik growth point counting
# TODO ilastik pitcher counting
# TODO pitcher instance segmentation?
# TODO individual pitcher color analysis and trait measurement?
