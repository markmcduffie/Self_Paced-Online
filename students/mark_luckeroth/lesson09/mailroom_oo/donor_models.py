#!/usr/bin/env python3

"""
A class-based system for managing donor information
"""

class Donor():

    def __init__(self, first, last, amount):
        self.first_name = first
        self.last_name = last
        self.donations = [amount]

    def add_donation(self, amount):
        self.donations.append(amount)

    @property
    def total(self):
        return sum(self.donations)

    @property
    def count(self):
        return len(self.donations)

    @property
    def average(self):
        return self.total/self.count


class DonorCollection():

    def __init__(self, donor_list=None):
        self.donorlist = donor_list

    def add_donor(self, first, last, amount):
        if self.donorlist == None:
            self.donorlist = [Donor(first, last, amount)]
        else:
            self.donorlist.append(Donor(first, last, amount))

    def load_donors(self, filename='donor_list.txt'):
        pass

    def save_donors(self, filename='donor_list.txt'):
        pass

    def find_donor(self, first=None, last=None):
        pass


