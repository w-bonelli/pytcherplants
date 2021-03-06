import cv2

import pytcherplants.color_analysis
import pytcherplants.color_analysis as ca

plant_path = 'samples/plants/1_14_19.10_30_20.p001.masked.jpg'


def test_get_clusters_default_k_and_no_filters():
    image = cv2.imread(plant_path)
    counts = pytcherplants.color_analysis.get_clusters(image)
    assert len(counts.keys()) == 9
    # assert all(v > 0 for v in counts.values())
    print(counts)


def test_get_clusters_default_k_and_filters():
    image = cv2.imread(plant_path)
    counts = pytcherplants.color_analysis.get_clusters(image, filters=[((0, 38, 40), (39, 255, 255))])  # filter out blues/purples
    assert len(counts.keys()) == 9
    # assert all(v > 0 for v in counts.values())
    print(counts)


def test_get_clusters_custom_k():
    image = cv2.imread(plant_path)
    counts = pytcherplants.color_analysis.get_clusters(image, k=10)
    assert len(counts.keys()) == 9
    assert all(v > 0 for v in counts.values())
    print(counts)


def test_analyze_file():
    df = ca.analyze_file(plant_path)
    print(df)


# TODO: test analyze directory
