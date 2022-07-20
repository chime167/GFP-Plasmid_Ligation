#!usr/bin/env python3


def get_complement(dna):
    return ''.join([{"A": "T", "T": "A", "C": "G", "G": "C"}[i] for i in dna])


input_file = input()
with open(input_file) as file:
    plasmid = file.readline().rstrip()
    plasmid_r_site = file.readline().rstrip()
    gfp = file.readline().rstrip()
    gfp_r_sites = file.readline().rstrip().split()


def cut_plasmid(strand, restriction_site):
    strand_complement = get_complement(strand)
    restriction_complement = get_complement(restriction_site)
    cut1 = strand.replace(restriction_site, f'{restriction_site[0]} {restriction_site[1:]}', 1)
    cut2 = strand_complement.replace(restriction_complement, f'{restriction_complement[:-1]} '
                                                             f'{restriction_complement[-1]}', 1)
    plasmid_cuts = cut1.split() + cut2.split()
    return plasmid_cuts


def cut_gfp(strand, restriction_sites):
    complement_strand = get_complement(strand)

    complement_restriction_sites = [get_complement(strand) for strand in restriction_sites]
    cut1_index = strand.find(restriction_sites[0]) + 1
    cut2_index = strand.find(restriction_sites[1]) + 1
    cut3_index = complement_strand.find(complement_restriction_sites[0]) + 5
    cut4_index = complement_strand.find(complement_restriction_sites[1]) + 5

    first_strand = strand[cut1_index:cut2_index]
    second_strand = complement_strand[cut3_index:cut4_index]

    return first_strand, second_strand


def ligate(plasmids, gfp_cuts):
    ligated_one = plasmids[0] + gfp_cuts[0] + plasmids[1]
    ligated_two = plasmids[2] + gfp_cuts[1] + plasmids[3]
    return ligated_one, ligated_two


plasmid_ends = cut_plasmid(plasmid, plasmid_r_site)
gfp_ends = cut_gfp(gfp, gfp_r_sites)

completed_ligation = ligate(plasmid_ends, gfp_ends)
print(completed_ligation[0])
print(completed_ligation[1])
