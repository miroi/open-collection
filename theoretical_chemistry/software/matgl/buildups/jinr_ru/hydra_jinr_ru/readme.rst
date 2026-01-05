=======================
MatGL on hydra.jinr.ru
=======================

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/.module add Python/v3.10.13
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/.python -m venv venv


milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/projects/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/hydra_jinr_ru/.source /zfs/scratch/HybriLITWorkshop2025/milias/software/venv/bin/activate

add modules
~~~~~~~~~~~
(venv) milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/projects/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/hydra_jinr_ru/.module add Python/v3.10.13  openmpi/v5.0.7_gcc1230  CMake/v3.29.2

pip installation
~~~~~~~~~~~~~~~~
(venv) milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/projects/open-collection/theoretical_chemistry/software/matgl/buildups/jinr_ru/hydra_jinr_ru/.pip install matgl

pip install spglib wheel
pip install bibtexparser

Building wheels for collected packages: bibtexparser
  Building wheel for bibtexparser (pyproject.toml) ... done
  WARNING: Building wheel for bibtexparser failed: [Errno 2] No such file or directory: '/lustre/home/user/m/milias/.cache/pip/wheels/31/9c/e2/471fa4752a2d99ddca152d75b53a2eaf38675145ba1d26ac0f/tmp3cf39no9/bibtexparser-1.4.3-py3-none-any.whl'
Failed to build bibtexparser
error: failed-wheel-build-for-install




