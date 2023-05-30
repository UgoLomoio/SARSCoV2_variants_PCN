from pymol import cmd

mutations = [67, 95, 142, 212, 339, 371, 373, 375, 417, 440, 446, 477, 478, 484, 493, 496, 498, 501, 505, 547, 614, 655, 679, 681, 764, 796, 856, 954, 969, 981]
chains = ["A", "B", "C"]
for mutation in mutations:
    for chain in chains:
        cmd.do("set sphere_color, red")
        line = "show spheres, (resi "+ str(mutation) + " and chain "+ chain + " and name CA)"
        cmd.do(line)