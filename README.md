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
