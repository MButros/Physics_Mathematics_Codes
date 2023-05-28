# This script formats the answer to a specific number of significant figures The calculation in this example is for the rest energy E of an electron

# mass of electron (in kilograms)
m = 9.11e-31 

# speed of light
c = 2.99792458e+8

# Compute the rest energy
E = m*c**2
print('The rest energy is', end="")
print('E =% .3g' % E)

 