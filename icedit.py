import sys,math
from openbabel import pybel
from openbabel import openbabel

gaffdict = {
    "ca  ":"C.ar",
    "c   ":"C.2 ",
    "ha  ":"H   ",
    "n   ":"N.am",
    "o   ":"O.2 ",
    "se  ":"Se  "
}

with open (sys.argv[1],'r') as file:
    mol2file = file.read()
    #for gaff, sybyl in gaffdict.items(): 
    #    mol2file = mol2file.replace(gaff, sybyl)

mol = pybel.readstring("mol2", mol2file)

a1=mol.OBMol.GetAtom(int(sys.argv[3]))
a2=mol.OBMol.GetAtom(int(sys.argv[4]))
a3=mol.OBMol.GetAtom(int(sys.argv[5]))
a4=mol.OBMol.GetAtom(int(sys.argv[6]))
tors=float(sys.argv[7])*math.pi/180

mol.OBMol.SetTorsion(a1,a2,a3,a4,tors)

output = mol.write("mol2")

with open (sys.argv[2],'w') as file:
    #for gaff, sybyl in gaffdict.items(): 
    #    output = output.replace(sybyl, gaff)
    file.write(output)