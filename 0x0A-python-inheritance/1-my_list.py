#!/usr/bin/python3
"""Define `1-my_list` module"""


class MyList(list):
    """MyList class - inherites from List"""

    def print_sorted(self):
        """Define method that print sorted list"""

        print(sorted(self))
