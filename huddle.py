import argparse, os
from dotenv import load_dotenv

from jemma.tools import parse_cli_arguments
from jemma.requirements.feature import Feature
from jemma.team.business_owner import BusinessOwner
from jemma.team.engineer import Engineer
from jemma.team.tester import Tester
from jemma.team.project_manager import ProjectManager
import jemma.work.flow as flow

import jemma.thinker as thinker

def main():

    ## ----------------------------- setup
    env_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path=env_path)

    args = parse_cli_arguments()
    brain = thinker.make_brain(args)

    ## ----------------------------- create a feature
    # read requirements from the file
    requirements = ""
    if args.requirements:
        with open(args.requirements, 'r') as file:
            requirements = file.read()

    feature = Feature(requirements)

    ## ----------------------------- create a team
    business_owner = BusinessOwner("an experienced business owner with attention to detail, "
                                   "focused on building requirements for engineers to build software products")

    engineer = Engineer("an experienced software engineer "
                        "with a focus on full stack development")

    tester = Tester("a professional software tester with a deep expertise is "
                    "understanding business requirements and how they translate into software features")

    project_manager = ProjectManager(feature)

    ## ----------------------------- rock & roll

    if args.user_stories:
        flow.create_user_stories (brain,
                                  project_manager,
                                  business_owner,
                                  engineer)
    if args.build_prototype:
        flow.build_prototype(brain,
                             project_manager,
                             business_owner,
                             engineer,
                             args.prompt,
                             args.sketch)

    if args.build_user_stories:
        flow.build_user_stories(brain,
                                project_manager,
                                business_owner,
                                engineer)
    if args.test_prototype:
        flow.test_prototype(brain,
                            project_manager,
                            tester)

if __name__ == '__main__':
    main()
