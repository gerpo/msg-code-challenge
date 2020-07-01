import Constants
from Solver import SolverInterface
from Solver.GeneticAlgSolver import GeneticAlgSolver
from Solver.LKHSolver import LKHSolver
from Solver.OrToolsSolver import OrToolsSolver


class InvalidSolverType(Exception):
    pass


class SolverBuilder:
    @staticmethod
    def build(calculator_type: str) -> SolverInterface:
        switcher = {
            Constants.MLROSE_SOLVER: GeneticAlgSolver,
            Constants.LKH_SOLVER: LKHSolver,
            Constants.ORTOOLS_SOLVER: OrToolsSolver,
        }
        try:
            return switcher[calculator_type]()
        except KeyError:
            raise InvalidSolverType from None
