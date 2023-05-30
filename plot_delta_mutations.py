from pymol import cmd

mutations = [158, 452, 478, 614, 681, 950]
chains = ["A", "B", "C"]
for mutation in mutations:
    for chain in chains:
        cmd.do("set sphere_color, red")
        line = "show spheres, (resi "+ str(mutation) + " and chain "+ chain + " and name CA)"
        cmd.do(line)