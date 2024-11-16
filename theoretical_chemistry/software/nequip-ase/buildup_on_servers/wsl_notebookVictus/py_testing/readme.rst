===================
nequip self testing
===================

miroi@MIRO:~/work/software/nequip/.pytest tests/unit/model/test_nequip_model.py
================================================= test session starts ==================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/miroi/work/software/nequip
collected 578 items

tests/unit/model/test_nequip_model.py ..............................................s...........s...........s... [ 12%]
........s.......................s...........s...........s...........s...........s...........s...........s....... [ 32%]
....s...................................s...........s.......................s...........s....................... [ 51%]
.....................................s...........s...........s...........s.......................s...........s.. [ 70%]
.........s...........s...........s...........s...........s...........s...................................s...... [ 90%]
.....s.......................s...........s..............                                                         [100%]

=================================================== warnings summary ===================================================
../../../.local/lib/python3.10/site-packages/nequip/__init__.py:20
  /home/miroi/.local/lib/python3.10/site-packages/nequip/__init__.py:20: UserWarning: !! PyTorch version 2.5.1 found. Upstream issues in PyTorch versions 1.13.* and 2.* have been seen to cause unusual performance degredations on some CUDA systems that become worse over time; see https://github.com/mir-group/nequip/discussions/311. The best tested PyTorch version to use with CUDA devices is 1.11; while using other versions if you observe this problem, an unexpected lack of this problem, or other strange behavior, please post in the linked GitHub issue.
    warnings.warn(

tests/unit/model/test_nequip_model.py::TestNequIPModel::test_jit[float32-device0-config0-base_config0]
tests/unit/model/test_nequip_model.py::TestNequIPModel::test_jit[float64-device0-config0-base_config0]
  /home/miroi/.local/lib/python3.10/site-packages/nequip/data/_dataset/_ase_dataset.py:231: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
    datas = [torch.load(d) for d in datas]

tests/unit/model/test_nequip_model.py: 48 warnings
  /home/miroi/.local/lib/python3.10/site-packages/nequip/utils/unittests/model_tests.py:108: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
    load_dat = torch.load(tmpdir + "/dat.pt")

tests/unit/model/test_nequip_model.py::TestNequIPModel::test_init[float64-config0-device0-base_config0]
tests/unit/model/test_nequip_model.py::TestNequIPModel::test_submods[float64]
  /home/miroi/.local/lib/python3.10/site-packages/nequip/utils/_global_options.py:95: UserWarning: Do NOT manually set PYTORCH_JIT_USE_NNC_NOT_NVFUSER=0 unless you know exactly what you're doing!
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================== 546 passed, 32 skipped, 53 warnings in 348.95s (0:05:48) ===============================
miroi@MIRO:~/work/software/nequip/.


