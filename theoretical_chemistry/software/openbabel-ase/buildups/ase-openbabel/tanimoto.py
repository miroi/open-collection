#
#  from Google AI, concerning pybel, openbabel-wheel...
#

from openbabel import pybel

mol1 = pybel.readstring("smi", "CCCC")
mol2 = pybel.readstring("smi", "CCCN")

# Calculate fingerprints (default is FP2)
fp1 = mol1.calcfp()
fp2 = mol2.calcfp()

# Calculate Tanimoto coefficient
similarity = fp1 | fp2
print(f"Tanimoto Similarity: {similarity:.4f}")

