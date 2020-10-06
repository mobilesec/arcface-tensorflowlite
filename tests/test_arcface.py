# Licensed under the EUPL.

import pytest
import numpy as np
import cv2

from arcface.ArcFace import ArcFace

@pytest.fixture
def arcface():
    return ArcFace()



def test_file_path(arcface):
	emb = arcface.calc_emb("arcface/data/test-image-gates.png")
	print(emb.shape)
	assert emb.shape == (512,)
	assert type(emb) is np.ndarray

def test_multiple_file_paths(arcface):
	emb = arcface.calc_emb(["arcface/data/test-image-gates.png", "arcface/data/test-image-gates2.png"])
	assert type(emb) is list
	assert len(emb) == 2

def test_cv2_image(arcface):
	img = cv2.imread("arcface/data/test-image-gates.png")
	emb = arcface.calc_emb(img)
	assert emb.shape == (512,)
	assert type(emb) is np.ndarray

def test_multiple_cv2_image(arcface):
	img1 = cv2.imread("arcface/data/test-image-gates.png")
	img2 = cv2.imread("arcface/data/test-image-gates2.png")
	emb = arcface.calc_emb([img1, img2])
	assert type(emb) is list
	assert len(emb) == 2

def test_distance_same_image(arcface):
	emb1 = arcface.calc_emb("arcface/data/test-image-gates.png")
	emb2 = arcface.calc_emb("arcface/data/test-image-gates.png")

	dist = arcface.get_distance_embeddings(emb1, emb2)
	assert dist == 0.0

def test_distance_different_image_same_person(arcface):
	emb1 = arcface.calc_emb("arcface/data/test-image-gates.png")
	emb2 = arcface.calc_emb("arcface/data/test-image-gates2.png")

	dist = arcface.get_distance_embeddings(emb1, emb2)
	assert dist > 0
	assert dist < 1.5

def test_distance_different_image_different_person(arcface):
	emb1 = arcface.calc_emb("arcface/data/test-image-gates.png")
	emb2 = arcface.calc_emb("arcface/data/test-image-2.png")

	dist = arcface.get_distance_embeddings(emb1, emb2)
	assert dist > 1.5