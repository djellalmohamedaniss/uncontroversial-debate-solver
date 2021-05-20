from sys import exit
from os import path, getcwd

from solver.arg_systems.WAS import WAS
from solver.expert.ExpertWithWAS import ExpertWithWAS as Expert
from solver.utils import WASFileParser as WFP
from solver.utils import BestExpertJsonOutput as Output

import argparse


def main():
    # arguments setup
    parser = argparse.ArgumentParser(description='Welcome to the uncontroversial debate solver console')
    required = parser.add_argument_group('required arguments')
    required.add_argument('--data', '-d', action='store', dest='filename',
                          help='the path to the schema json file', required=True)
    parser.add_argument('--verbose', '-v', action='store_true', default=False, dest='verbose',
                        help='show the \'WAS table\' and detailed prints')
    parser.add_argument('--output', '-o', action='store', nargs='?', const=getcwd(),
                        dest='output_path',
                        help='the directory of the file where the result is stored, default is the current path')

    console_arguments = parser.parse_args()

    filename = console_arguments.filename

    output_path = console_arguments.output_path

    if output_path is not None:
        if not path.isdir(output_path):
            exit(f"{output_path} is not a valid path, please provide a valid input")

    arguments, attacks, topics = WFP.read(filename)

    was = WAS(arguments, attacks)

    pws, experts = was.possible_was_of_experts(Expert.__generator__(topics, expertise_cardinal=2))

    best_experts = experts.best()

    if console_arguments.verbose:
        print("consequences of every potential expert vote\n")

        print(pws.table_possible_was())

        print("\nbest experts to pick are:\n")

        for expert in best_experts:
            print(f"- {expert}")

    else:
        print("{0}".format([expert.expertise for expert in best_experts]))

    if output_path is not None:
        Output.generate(experts, output_path)


if __name__ == "__main__":
    main()
