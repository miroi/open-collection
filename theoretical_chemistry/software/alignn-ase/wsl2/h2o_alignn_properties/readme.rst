=====================
H2O ALIGNN properties
=====================

conda activate alignn_dgl2
pip install "torchdata==0.8.0" --no-deps
python -c "import torch, dgl; print(torch.__version__, dgl.__version__)"


pip install alignn --no-deps
pip install ase jarvis-tools pydantic-settings
pip list | grep -i -E "^(torch|dgl|numpy|torchdata) "


pip list 2>/dev/null | grep -i -E "^(torch|dgl|numpy|torchdata|alignn|ase|jarvis-tools) "
python -c "import alignn, dgl, torch; print('ok')"



