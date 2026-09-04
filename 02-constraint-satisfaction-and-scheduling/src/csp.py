class CSP:

    def __init__(
        self,
        variables,
        domains,
        constraints,
    ):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        
    def validate(self):
        for variable in self.variables:
            if variable not in self.domains:
                raise ValueError(
                    f"No domain for {variable}"
                )
                
    def get_domains_copy(self):
        return {
            variable:list(values)
            for variable, values
            in self.domains.items()
        }
        
    def is_consistent(
        self,
        assignment,
    ):
        for constraint in self.constraints:
            if not constraint.is_satisfied(
                assignment
            ):
                return False

        return True