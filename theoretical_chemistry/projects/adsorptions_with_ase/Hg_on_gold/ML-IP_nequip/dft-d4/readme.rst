=============================
Hg@Au111 with NequIP & DFT-D4
=============================

pip install dftd4

https://chat.deepseek.com/share/vc7rpext1514npzq2o


Your --d4 results show severe overbinding (\(E_{\text{ads}} \approx -3.38\text{ eV}\) and \(a_{\text{Au}} = 3.8639\text{ \AA}\)) because your NequIP foundation model already includes dispersion—adding DFTD4 caused double-counting.

Why This Happened

1. Double-Counting Dispersion: Your model hash (039e5620...) is NequIP-OAM-L (trained on OMat24 + sAlex + MPTrj). While MPTrj is pure PBE, OMat24/sAlex datasets or the specific multi-fidelity training target already capture significant attractive van der Waals interactions, or dftd4's default periodic cutoff/three-body ATM terms on dense 64-atom metallic Au slabs add massive artificial attraction (~ -4.7 eV/atom to bulk Au, shifting \(E_{\text{bulk}}\) from -3.27 eV/atom to -7.99 eV/atom).
2. Physical Breakdown:
	• Bulk Au lattice constant: Collapsed from \(4.1733\text{ \AA}\) (pure NequIP) to \(3.8639\text{ \AA}\) (far below the experimental value of \(4.078\text{ \AA}\)).
	• Adsorption energy (\(E_{\text{ads}}\)): Jumped from -0.3460 eV to -3.3833 eV—unphysical for Hg on Au(111), where experimental/DFT-D3 adsorption energies are around -0.5 to -0.7 eV.

• Do not use --d4 with this model. Stick to the pure NequIP model (python hg_on_gold_nequip.py without --d4), which gives physically reasonable lattice parameters, bond heights (\(2.422\text{ \AA}\)), and site ordering (fcc > hcp > bridge > ontop).
