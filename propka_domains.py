import os
from propka.run import single
import os 
import numpy as np

spikes = ["SPWT","Epsl","Zeta","Beta", "Alfa","Delt","Kapp","Gamm","Iota","Iot2","Eta1","Ihu1","Omi1","Omi5"]
spike_muts_variants = {'Wild Type': np.array([]),
                         'Epsilon': np.array([ 13, 152, 452, 614]),
                         'Zeta': np.array([ 484,  614, 1176]),
                         'Beta': np.array([ 80, 215, 246, 417, 484, 501, 614, 701]),
                         'Alpha': np.array([ 501,  570,  614,  681,  716,  982, 1118]),
                         'Delta': np.array([158, 452, 478, 614, 681, 950]),
                         'Kappa': np.array([ 154,  484,  614,  681, 1071]),
                         'Gamma': np.array([ 138,  190,  417,  484,  501,  614,  655, 1027]),
                         'Iota1': np.array([  5,  95, 253, 477, 614]),
                         'Iota2': np.array([  5,  95, 253, 484, 614]),
                         'Eta': np.array([ 52,  67, 484, 614, 677, 888]),
                         'Ihu': np.array([  96,  190,  210,  346,  394,  449,  490,  501,  614,  681,  859,
                                 936, 1191]),
                         'Omicron1': np.array([ 67,  95, 142, 212, 339, 371, 373, 375, 417, 440, 446, 477, 478,
                                484, 493, 496, 498, 501, 505, 547, 614, 655, 679, 681, 764, 796,
                                856, 954, 969, 981]),
                         'Omicron5': np.array([142, 213, 339, 371, 373, 375, 376, 405, 408, 417, 440, 452, 477,
                                478, 484, 486, 498, 501, 505, 614, 655, 679, 681, 764, 796, 954,
                                969])
}
spikes = {spike_name: list(spike_muts_variants.keys())[i] for i, spike_name in enumerate(spikes)}

domains = {
"NTD": np.arange(14, 305, 1),
"RBD":  np.arange(331, 527, 1)
}

cwd = os.getcwd()
sep = os.sep
pdb_dir = cwd+sep+"Data"+sep+"PDB"

for domain, residues in domains.items():
    
    pdb_domain_dir = pdb_dir + sep + domain
    resi_to_leave = "{}-{}".format(residues[0], residues[-1])
    if not os.path.isdir(pdb_domain_dir):
        os.mkdir(pdb_domain_dir)
    
    for pdb, variant_name in spikes.items():
    
        pdb_domain_file = pdb_domain_dir + sep + pdb + "_" + domain + ".pdb"
        output = single(pdb_domain_file)
