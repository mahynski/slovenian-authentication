Authenticating Slovenian Fruits and Vegetables
---
This repository accompanies the manuscript: [Comparing Machine Learning Models to Chemometric Ones to Detect Food Fraud: A Case Study in Slovenian Fruits and Vegetables](https://dx.doi.org/).

> "We present a method for comparing models used to detect food fraud based on stable isotopes and trace element (SITE) levels. Existing modeling procedures generally do not provide an uncertainty estimate on a model’s performance due to variations in the training data or preprocessing procedures.  Here, we perform a comparison of performance metrics between end-to-end modeling pipelines, enabling hypothesis testing to reveal when differences are statistically significant. When many models have similar performances, the model with the best performance is not always the best to implement in practice due to their complexity or cost. Statistical comparison helps reveal the net benefit of complex models, enabling a better interpretation of their value. We illustrate our approach on six different fruits and vegetables collected in Slovenia from 2018-2022.  Models in this study include state-of-the-art machine learning models for tabular data, such as Random Forests (RF), and modern one-class classifiers, such as DD-SIMCA."

Datasets are also available on [HuggingFace](https://huggingface.co/collections/mahynski/food-authenticity-66fb5fa3ecfbd9538190f2f8):
1. [Apple](https://huggingface.co/datasets/mahynski/slovenian-site-apple)
2. [Asparagus](https://huggingface.co/datasets/mahynski/slovenian-site-asparagus)
3. [Cherry](https://huggingface.co/datasets/mahynski/slovenian-site-cherry)
4. [Garlic](https://huggingface.co/datasets/mahynski/slovenian-site-garlic)
5. [Persimmon](https://huggingface.co/datasets/mahynski/slovenian-site-persimmon)
6. [Strawberry](https://huggingface.co/datasets/mahynski/slovenian-site-strawberry)

Final models, trained on the complete datasets listed above, are also available on [HuggingFace](https://huggingface.co/collections/mahynski/food-authenticity-66fb5fa3ecfbd9538190f2f8):
1. [Apple](https://huggingface.co/mahynski/slovenian-site-apple)
2. [Asparagus](https://huggingface.co/mahynski/slovenian-site-asparagus)
3. [Cherry](https://huggingface.co/mahynski/slovenian-site-cherry)
4. [Garlic](https://huggingface.co/mahynski/slovenian-site-garlic)
5. [Persimmon](https://huggingface.co/mahynski/slovenian-site-persimmon)
6. [Strawberry](https://huggingface.co/mahynski/slovenian-site-strawberry)

Citation
---
Please cite the associated manuscript as follows:

~~~code
@article{Mahynski_Strojnik_Shen_Ogrinc_2025, 
    title={Comparing Machine Learning Models to Chemometric Ones to Detect Food Fraud: A Case Study in Slovenian Fruits and Vegetables}, 
    volume={}, 
    journal={}, 
    author={Mahynski, Nathan A. and Strojnik, Lidija and Shen, Vincent K. and Ogrinc, Nives}, 
    year={2025}, 
    pages={},
    doi={}
} 
~~~

Installation
---
To reproduce the calculations performed in this work, first set up the conda environment for this project.
~~~code
$ conda env create -f conda-env.yml
$ conda activate test-slo
$ python -m ipykernel install --user --name=test-slo
~~~

Acknowledgements
---
The Slovenian Forestry and Food, Administration for Food Safety, Veterinary Sector and Plant Protection under GA no. C2337-18–000044, C2337-19–000033, and C2337-20–000048, C2337-21-000062 and C2337-22-000066 are gratefully acknowledged. Financial support was also provided from the Slovenian Research and Innovation Agency by P1-0143 and the IAEA project “Authenticity of High-Quality Slovenian Food Products Using Advanced Analytical Techniques” (Contract No. 23362). 

Certain equipment, instruments, software, or materials, commercial or non-commercial, are identified in this paper to specify the experimental procedure adequately. Such identification is not intended to imply recommendation or endorsement of any product or service by NIST, nor is it intended to imply that the materials or equipment identified are necessarily the best available for the purpose. Contribution of the National Institute of Standards and Technology, not subject to US Copyright.
