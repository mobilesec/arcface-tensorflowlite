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

from arcface.lib.models import ArcFaceModel
import arcface
from arcface.lib.utils import l2_norm
import tensorflow as tf
import numpy as np
import cv2
import os
import requests
from astropy.utils.data import download_file

class ArcFace():
    def __init__(self): 
        tflite_path = download_file("https://cloud.ins.jku.at/index.php/s/g2YDT8Zn9RkzsEy/download", cache=True) 
        
        self.interpreter = tf.lite.Interpreter(model_path=tflite_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def calc_emb(self, imgs):
        """Calculates the embedding from an (array of) images. These images can be cv2-image-files or a path to a file.
        Parameters:
            imgs (str|list): either a list of images or the image itself. The image can be a cv2-image or a path to a file. The images should already be aligned!
        Returns:
            ndarray: 512-d embedding of the supplied image(s)
        Example:
            calc_emb("~/Downloads/test.jpg")
        """
        if isinstance(imgs, list):
            return self._calc_emb_list(imgs)
        return self._calc_emb_single(imgs)


    def get_distance_embeddings(self, emb1, emb2):
        """Calculates the distance (L2 norm) between two embeddings. Larger values imply more confidence that the two embeddings are from different people.
        Parameters:
            emb1 (ndarray): embedding of a person (e.g. generated by calc_emb(...))
            emb2 (ndarray): embedding of a person (e.g. generated by calc_emb(...))
        Returns:
            int: distance between emb1 and emb2
        Example:
            get_distance_embeddings(calc_emb("person1.jpg"), calc_emb("person2.jpg"))
        """
        diff = np.subtract(emb1, emb2)
        dist = np.sum(np.square(diff))
        return dist
        
    def _calc_emb_list(self, imgs):
        embs = []
        for img in imgs:
            embs.append(self._calc_emb_single(img))
        return embs

    def _calc_emb_single(self, img):
        if isinstance(img, str):
            img = cv2.imread(img)
            if img is None:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), img)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (112, 112))
        img = img.astype(np.float32) / 255.
        if len(img.shape) == 3:
            img = np.expand_dims(img, 0)
        self.interpreter.set_tensor(self.input_details[0]['index'], img)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])

        emb = l2_norm(output_data)
        return emb[0]
