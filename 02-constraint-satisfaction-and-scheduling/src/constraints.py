from abc import ABC, abstractmethod


class Constraint(ABC):

    @abstractmethod
    def is_satisfied(
        self,
        assignment
    ):
        pass
    
class BinaryConstraint(Constraint):

    def __init__(
        self,
        var1,
        var2,
    ):
        self.var1 = var1
        self.var2 = var2


    def is_satisfied(
        self,
        assignment,
    ):

        if (
            self.var1 not in assignment
            or
            self.var2 not in assignment
        ):
            return True

        return (
            assignment[self.var1]
            !=
            assignment[self.var2]
        )