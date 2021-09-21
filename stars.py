"""
Print n rows with stars.

The number of stars in row i should be i.

For example, for 5 stars:

python stars.py
*
**
***
****
*****

"""


def print_star():
    print('*')


max_stars = 5

for row_index in range(max_stars):
    num_stars = row_index
    for star_index in range(num_stars):
        print_star()
    print()
