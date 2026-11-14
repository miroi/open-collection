=====================
H2O ALIGNN properties
=====================

conda activate alignn_dgl2
pip install "torchdata==0.8.0" --no-deps
python -c "import torch, dgl; print(torch.__version__, dgl.__version__)"

python -c "import alignn, dgl, torch; from alignn.pretrained import get_prediction; print('ok')"
python h2o_alignn.pypython -c "import alignn, dgl, torch; from alignn.pretrained import get_prediction; print('ok')"
python h2o_alignn.py





