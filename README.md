# icedit
icedit is a simple tool to modify internal coordinates of a structure.

It currently reads and writes to a SYBYL mol2 file, although nonstandard atom types (eg GAFF atom types) work fine, albeit with complaints from openbabel.
It takes as arguments an input file, output file, 2-4 atom indices (which define the type of internal coordinate, 2=bond, 3=angle, 4=dihedral) and a value for the internal coordinate (in angstroms or degrees).

e.g. $ icedit input.mol2 output.mol2 1 2 11 12 80.0
will set the dihedral defined by atoms 1, 2, 11 and 12 to 80 degrees.