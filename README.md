Authenticating Slovenian Fruits and Vegetables
---
This repository accompanies the manuscript: [Comparing Machine Learning Models to Chemometric Ones to Detect Food Fraud: A Case Study in Slovenian Fruits and Vegetables](https://dx.doi.org/).

> "We present a method for comparing models used to detect food fraud based on stable isotopes and trace element (SITE) levels. These features are often the preferred choice for traceability systems when determining geographic origin. Existing modeling procedures generally do not provide an uncertainty estimate on the model’s performance due to variations in the training set and preprocessing procedures.  Our method enables statistical comparison of performance metrics between end-to-end modeling pipelines, enabling hypothesis testing to reveal when differences are statistically significant. When many models have similar performances, the model with the best performance is not always the best to implement in practice.  Complex models whose predictions are difficult to explain, and therefore legally justify, and models which require many SITE levels to be measured can be cumbersome in practice.  Statistical comparison helps reveal the net benefit of complex models, enabling a better interpretation of their value. We illustrate our approach using data from six different fruits and vegetables collected in Slovenia from 2018-2022.  These represent challenging commodities to model, and our approach can be transferred to other commodities of interest which may show entirely different patterns of discrimination.  Models in this study include state-of-the-art machine learning models for tabular data, such as random forests (RF), and modern one-class classifiers, such as DD-SIMCA.  For the specific food matrices we investigated here, we found that RF models usually performed the best but were not significantly superior to DD-SIMCA; moreover, simple decision trees often revealed surprising general scientific trends, such as the overall significance of Strontium across most foods, yet often did not statistically underperform the best model."

Citation
---
Please cite the associated manuscript as follows:

~~~code
@article{
    INSERT FORMATTED BITEX
}
~~~

[CREATE ZENODO DOI](https://zenodo.org/account/settings/github/). See the CITATION.cff file for how to cite this repository.

Installation
---
Set up the conda environment for this project.
~~~code
$ conda env create -f conda-env.yml
$ conda activate test-slo
$ python -m ipykernel install --user --name=test-slo
~~~

Contributors
---
Update the CITATION.cff file to enable appropriate citations.  
