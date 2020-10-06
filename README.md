# ArcFace face recognition
Implementation of the [https://openaccess.thecvf.com/content_CVPR_2019/html/Deng_ArcFace_Additive_Angular_Margin_Loss_for_Deep_Face_Recognition_CVPR_2019_paper.html](ArcFace face recognition algorithm). It includes a pre-trained model based on [https://arxiv.org/abs/1512.03385](ResNet50).

The code is based on[https://github.com/peteryuX/arcface-tf2](peteryuX's) implementation. Instead of using full Tensorflow for the inference, the model has been converted to a Tensorflow light model using `tf.lite.TFLiteConverter` which increased the speed of the inference by ~25%.

## Installation
You can install the package through pip:
```
pip install arcface
```

## Quick-Start

The following example illustrates the ease of use of this package:
```python
>>> from arcface import ArcFace
>>> face_rec = ArcFace.ArcFace()
>>> emb1 = face_rec.calc_emb("~/Downloads/test.jpg")
>>> print(emb1)
array([-1.70827676e-02, -2.69084200e-02, -5.85994311e-02,  3.33652040e-03,
        9.58345132e-04,  1.21807214e-02, -6.81217164e-02, -1.33364811e-03,
       -2.12905575e-02,  1.67165045e-02,  3.52908894e-02, -5.26051633e-02,
	   ...
       -2.11241804e-02,  2.22553015e-02, -5.71946353e-02, -2.33468022e-02],
      dtype=float32)
>>> emb2 = face_rec.calc_emb("~/Downloads/test2.jpg")
>>> face_rec.get_distance_embeddings(emb1, emb2)
0.78542
```
You can feed the `calc_emb` function either a single image or an array of images. Furthermore, you can supply the image as (absolute or relative) path, or an cv2-image. To make it more clear, hear are the four possibilities:

1. (Absolute or relative) path to a single image: `face_rec.calc_emb("test.jpg")`
2. Array of images: `face_rec.calc_emb(["test1.jpg", "test2.png"])`
3. Single cv2-image: `face_rec.calc_emb(cv2.imread("test.png"))`
4. Array of cv2-images: `face_rec.calc_emb([cv2.imread("test1.jpg"), cv2.imread("test2.png")])`

The face recognition tool returns (an array of) 512-d embedding(s) as a numpy array.

> Notice! This package does neither perform face detection nor face alignment! It assumes that the images are already pre-processsed!

## License
Licensed under the [https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%20EN.txt](EUPL).
