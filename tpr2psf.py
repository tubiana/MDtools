import MDAnalysis as mda
import parmed as pmd
import sys

#Requieres MDAnalysis, ParmEd and openmm

def tpr_to_psf(tpr_file, psf_file):
    # Load the TPR file using MDAnalysis
    universe = mda.Universe(tpr_file)

    # Create an empty ParmEd Structure
    structure = pmd.Structure()

    # Add atoms to the ParmEd Structure
    for atom in universe.atoms:
        pmd_atom = pmd.Atom(name=atom.name, type=atom.type)
        pmd_atom.charge = atom.charge
        pmd_atom.mass = atom.mass
        structure.add_atom(pmd_atom, resname=atom.resname, resnum=atom.resnum)

    # Add bonds to the ParmEd Structure
    for bond in universe.bonds:
        structure.bonds.append(pmd.Bond(structure.atoms[bond.atoms[0].index], structure.atoms[bond.atoms[1].index]))

    # Write the PSF file
    structure.save(psf_file, format="psf", overwrite=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("TPR2PSF : Convert TPR file to PSF File")
        print("(mostly usefull to display Martini files in Pymol...)")
        print("Usage: python tpr_to_psf.py input.tpr output.psf")
        sys.exit(1)

    tpr_file = sys.argv[1]
    psf_file = sys.argv[2]

    tpr_to_psf(tpr_file, psf_file)
