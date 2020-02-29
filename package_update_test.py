from pompy import processors

arena_size = 1000
r_sq_max=20;epsilon=0.00001;
N=1e6;box_min=-1*arena_size;
box_max = arena_size;puff_mol_amt=1.

odor_field = processors.ConcentrationValueCalculator(puff_mol_amt)
odor_field1 = processors.ConcentrationValueFastCalculator(box_min,box_max,r_sq_max,epsilon,puff_mol_amt,N,verbose=True)
