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

try:
    with open (sys.argv[1],'r') as file:
        mol2file = file.read()
        #for gaff, sybyl in gaffdict.items(): 
        #    mol2file = mol2file.replace(gaff, sybyl)
except:
    print("Could not find file {0}".format(sys.argv[1]))
    exit()

try:
    mol = pybel.readstring("mol2", mol2file)
except:
    print("{0} doesn't seem to be even a slightly valid mol2 file".format(sys.argv[1]))
    exit()

# Edit bond length
if len(sys.argv) == 6:
    a1 = a1=mol.OBMol.GetAtom(int(sys.argv[3]))
    a2 = mol.OBMol.GetAtom(int(sys.argv[4]))
    parameter = float(sys.argv[5])
    mol.OBMol.GetBond(a1,a2).SetLength(a1,parameter)

# Edit angle
elif len(sys.argv) == 7:
    a1 = mol.OBMol.GetAtom(int(sys.argv[3]))
    a2 = mol.OBMol.GetAtom(int(sys.argv[4]))
    a3 = mol.OBMol.GetAtom(int(sys.argv[5]))
    parameter = float(sys.argv[6])*math.pi/180
    print("At the moment I can't change angles, because openbabel is a bit silly but still very useful. Sorry!")
    #mol.OBMol.OBAngle(a2,a1,a3).SetAngle(parameter)

elif len(sys.argv) == 8:
    a1=mol.OBMol.GetAtom(int(sys.argv[3]))
    a2=mol.OBMol.GetAtom(int(sys.argv[4]))
    a3=mol.OBMol.GetAtom(int(sys.argv[5]))
    a4=mol.OBMol.GetAtom(int(sys.argv[6]))
    parameter=float(sys.argv[7])*math.pi/180
    mol.OBMol.SetTorsion(a1,a2,a3,a4,parameter)

else:
    print("I need an input file, output file, 2-4 atom indices, and a parameter to change.")

output = mol.write("mol2")

with open (sys.argv[2],'w') as file:
    #for gaff, sybyl in gaffdict.items(): 
    #    output = output.replace(sybyl, gaff)
    file.write(output)