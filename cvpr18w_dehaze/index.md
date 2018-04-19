---
layout: default
title: Single Image Dehazing
---

## Image Dehazing by Joint Estimation of Transmittance and Airlight using Bi-Directional Consistency Loss Minimized FCN

#### Ranjan Mondal, Sanchayan Santra, Bhabatosh Chanda
<!-- <div class="row"> -->
<!--    <div class="col-xs-6"> -->
<!--    <img src="{{ site.baseurl }}/public/haze_image/Oberfallenberg_input.jpg" alt="input image"/> -->
<!--    </div> -->
<!--    <div class="col-xs-6"> -->
<!--    <img src="results/Oberfallenberg_our.jpg" alt="output image"/> -->
<!--    </div> -->
   
<!--    <div class="col-xs-6"> -->
<!--    <img src="{{ site.baseurl }}/public/haze_image/fog_on_the_bay_input.jpg" alt="input image"/> -->
<!--    </div> -->
<!--    <div class="col-xs-6"> -->
<!--    <img src="results/fog_on_the_bay_our.jpg" alt="output image"/> -->
<!--    </div> -->
<!-- </div> -->

<center><b>Abstract</b></center>
Very few of the existing image dehazing methods have laid stress on the accurate restoration of color from hazy images, although it is crucial for proper removal of haze. In this paper, we are proposing a Fully Convolutional Neural Network (FCN) based image dehazing method. We have designed a network that jointly estimates scene transmittance and airlight. The network is trained using a custom designed loss, called bi-directional consistency loss, that tries to minimize the error to reconstruct the hazy image from clear image and the clear image from hazy image. Apart from that, to minimize the dependence of the network on the scale of the training data, we have proposed to do both the training and inference in multiple levels. Quantitative and qualitative evaluations show, that the method works comparably with state-of-the-art image dehazing methods.


Accepted in CVPR 18 Workshop NTIRE 2018 <br/>
Preprint paper: Uploading Soon <br/>
Code: [[Github]](https://github.com/ranjan1990/CVPR2018_Dehazing)

**Results:** [Uploading Soon](#)
