#PREPROCESSING: USE IT BEFORE RUNNING THIS SCRIPT
# remove chain B+C

import pymol
from pymol import cmd
import numpy as np 

domains = {
"NTD": np.arange(14, 305, 1),
#"CT0": np.arange(306, 330, 1),
"RBD":  np.arange(331, 527, 1),
#"CT1": np.arange(528, 590, 1),
#"CT2": np.arange(591, 685, 1),
#"S2S2'": np.arange(686, 815, 1),
#"FP": np.arange(816, 885, 1),
#"FPR": np.arange(886, 911, 1),
#"HR1": np.arange(912, 984, 1),
#"CH": np.arange(985, 1034, 1),
#"CD": np.arange(1035, 1080, 1),
#"CD1": np.arange(1081, 1147, 1),
}
    
cmd.do("remove hetatm")
cmd.do("hide licorice")

residues_str = "14-527"
cmd.do("hide surface")
#cmd.do("show surface, (prepared01)")
cmd.do("show surface, (prepared01 and resi {})".format(residues_str))
cmd.do("hide cartoon, (run01)")

pdb_dir = "E:\\SARSCoV2_variants_PCN\\Data\\PDB\\"
variant = list(cmd.get_object_list(selection='all'))[0]
pdb = pdb_dir + variant + ".pdb"
cmd.do("load {}, {}1".format(pdb, variant)) #1 is important
cmd.do("hide surface, {}1".format(variant))
cmd.do("show cartoon, {}1".format(variant))
cmd.do("hide everything, {}".format(variant)) #without 1

chains = "A+B+C"
line = "color green, ({}1 and chain {})".format(variant, chains)
cmd.do(line)
line = "set cartoon_transparency, 0.8, ({}1 and chain {})".format(variant,chains)
cmd.do(line)
cmd.do("hide licorice")


cmd.do("save Figures\EP\{}_ep_session.pse".format(variant))