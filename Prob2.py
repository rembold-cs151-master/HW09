##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import random


class Rabbit(object):
    # Any class variables here

    def __init__(self, mom=None, dad=None):
        '''
        Creates an instance of a Rabbit. Gender is always randomly assigned,
        while color is assigned randomly only if no parents are given. If
        parents are given, the color is based off the coloring of the 
        parents, according to get_offspring_color.

        Inputs:
            - mom (Rabbit): female parent
            - dad (Rabbit): male parent
        
        Should have 5 attributes:
            - self.color (string, color of the rabbits fur)
            - self.gender (string, gender of rabbit)
            - self.mom (Rabbit, female parent determined by input)
            - self.dad (Rabbit, male parent determined by input)
            - self.rid (integer, unique rabbit id number, from class variable)
        '''
        pass

    def __repr__(self):
        '''
        Textual representation of the Rabbit object. Include at least self.rid
        for easy of understanding and debugging. '''
        pass

    def get_rabbit_color(self):
        '''
        Getter function to return the current color of the rabbit.

        Outputs:
            - self.color (string): the color of the rabbit
        '''
        pass

    def get_offspring_color(self, mate):
        '''
        Parses the colors of both parents and determines what the resulting color
        of the offspring should be. Offspring coloring will either be Black, White,
        or Gray.

        Input:
            - mate (Rabbit): the other rabbit to breed with
        Output:
            - (string): color of the rabbit that would be born to both parents
        '''
        pass

    def attempt_mating(self, potential_mate):
        '''
        Rabbits in general are chosen randomly to potentially mate. As such,
        it needs to be determined if the rabbits are: 1) not the same rabbit,
        and 2) of opposite genders. If they are, then a new Rabbit object is
        returned. Nothing is returned otherwise.

        Input:
            - potential_mate (Rabbit): rabbit to attempt to mate with self
        Output:
            - (Rabbit): new instance of a baby rabbit. Should have both its
                parents provided as arguments.
        '''
        pass

    def __eq__(self, other):
        '''
        Checks if two rabbits are equal by comparing their self.rid values.
        '''
        pass

    def get_parents(self):
        '''
        Getter function to return tuple of both parents.

        Outputs:
            - (tuple of Rabbit): tuple of both parent rabbit objects
        '''
        pass

    def get_ancestors(self):
        '''
        Constructs a list of all rabbit objects that are direct ancestors of
        self. No duplicates should be included in the returned list (or they
        should be removed prior to being returned). Can be approached either
        recursively or through looping.

        Output:
            - (list of Rabbit objects): list of all Rabbit objects which were
                direct ancestors to self.
        '''
        pass


class Rabbit_Population:

    def __init__(self, years, initial_n):
        '''
        Creates an initial population of rabbits of size initial_n and then
        breeds those rabbits for "years" generations to get a rabbit population.
        The other methods in this class may help in creating this population.

        Inputs:
            - years (integer): The number of years or generation the rabbits
                should breed to yield the final population.
            - initial_n (integer): The initial number of rabbits that should be
                present in the population to base the first generation's breeding
                from.

        Should have a single attribute:
            - self.population (list of Rabbit objects, created from initial
                population of rabbits and then the desired number of years
                of breeding.)
        '''
        pass

    def create_init_rabbit_pop(self, n):
        '''
        Creates a list populated by n Rabbit objects. None of these initial
        rabbits should have parents.

        Input:
            - n (integer): desired number of Rabbit objects in list
        Output:
            - (list of Rabbit objects)
        '''
        pass

    def advance_year(self):
        '''
        Simulates the interactions of the group of rabbits over a single generation.
        Each generation, the number of potential rabbit breedings is equal to the
        number of initial rabbits in self.pop at the start of that generation.
        Each potential breeding selects two rabbits at random from self.pop
        and attempts to breed them. Any child rabbits created should be added to 
        self.pop upon the conclusion of a generation.

        Output:
            - None, but updates the value of self.pop
        '''
        pass



# If you have any testing code you want to run with the program
# insert it in the if statement below.
if __name__ == '__main__':
    pass
