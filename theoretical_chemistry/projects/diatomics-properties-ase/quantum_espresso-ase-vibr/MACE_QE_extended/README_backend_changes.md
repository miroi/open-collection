N2 MACE/QE optional-backend update

Changes applied conceptually:
- QE pseudopotential checks are only required for:
    calculator: qe
    calculator: mace+qe
- calculator: mace runs without QE pseudopotentials.
- MACE device accepts cuda/cpu and maps legacy gpu -> cuda.
- Per-molecule calculator selection overrides the global calculator setting.

configure.yaml examples:

calculator: qe

mace:
  model_path: /path/to/mace-mp-0b3-medium.model
  device: cuda

molecules:
  N2:
    calculator: mace