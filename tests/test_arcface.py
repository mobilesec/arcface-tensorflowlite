# Copyright (C) 2020  Johannes Kepler University Linz, Institute of Networks and Security
# Copyright (C) 2020  CDL Digidow <https://www.digidow.eu/>
#
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
# the European Commission - subsequent versions of the EUPL (the "Licence").
# You may not use this work except in compliance with the Licence.
# 
# You should have received a copy of the European Union Public License along
# with this program.  If not, you may obtain a copy of the Licence at:
# <https://joinup.ec.europa.eu/software/page/eupl>
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence.

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
