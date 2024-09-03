# Start a Jupyter Notebook server with no password so we can easily access it
source /opt/conda/etc/profile.d/conda.sh
conda activate test-slo
jupyter notebook --port 8501 --ip='*' --NotebookApp.token='' --NotebookApp.password=''
