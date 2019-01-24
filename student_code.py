import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        #if asserted fact is a Fact and not already in facts, add it to facts
        if(isinstance(fact,Fact) and (fact not in self.facts)):
            self.facts.append(fact)
            fact.asserted = True


    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))

        #instantiate a list of bindings
        b = ListOfBindings()
        #iterate through facts in kb, add bindings that match asked fact
        for i in self.facts:
            if(match(i.statement,fact.statement) != False):
                b.add_bindings(match(i.statement,fact.statement))
        #return list of bindings if it exists, else return false
        return b if b else False
