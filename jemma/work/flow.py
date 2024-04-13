try:
    from pyreadline3 import Readline # windows support
    readline = Readline()
except ImportError:
    import readline

from functools import partial
from jemma.tools import color, jemma_say

def compose_tasks(brain,
                  project_manager,
                  designer,        ## TODO: project_manager should have a designer OR there should be a Team
                  tasks,
                  args):

    prompt = args.prompt
    sketch = args.sketch

    task_functions = {
        'sketch-to-doc': {
            'fn': partial(project_manager.meet_to_discuss_mockups, brain, designer, prompt, sketch),
            'is_partial': False # this function does not require any more arguments
        },
        'sketch-to-prototype': {
            'fn': partial(project_manager.meet_to_convert_design_to_prototype, brain, designer, sketch),
            'is_partial': True
        }
    }

    # validate all tasks before execution
    unknown_tasks = [task for task in tasks if task not in task_functions]
    if unknown_tasks:
        raise Exception(f"don't know how to do this yet: {', '.join(unknown_tasks)}")

    ## handrolling Clojure's threading macro
    done = None
    for task in tasks:
        fn = task_functions[task]['fn']
        is_partial = task_functions[task]['is_partial']

        if is_partial:
            jemma_say(f"task \"{task}\" <<< {done}")
            done = fn(done)
        else:
            jemma_say(f"task \"{task}\" <<< [no input]")
            done = fn()

        jemma_say(f"task {task} >>> {done}")

    return done

def create_user_stories(brain,
                        project_manager,
                        business_owner,
                        engineer):

    project_manager.meet_to_create_user_stories(brain,
                                                business_owner)

    ## have another business owner to review the stories
    # project_manager.meet_to_review_user_stories(brain,
    #                                            business_owner,
    #                                            stories)

    project_manager.meet_to_refine_user_stories(brain,
                                                engineer,
                                                business_owner)

def build_user_stories(brain,
                       project_manager,
                       business_owner,
                       engineer):
    project_manager.meet_to_create_user_stories(brain,
                                                business_owner)
    # project_manager.meet_to_combine_user_stories(brain,
    #                                              business_owner)
    project_manager.user_stories_to_requirement()
    return project_manager.meet_to_build_prototype(brain,
                                                   engineer)


def ask_for_feedback():

    # make sure the cursor works
    readline.parse_and_bind('set editing-mode emacs')

    while True:
        feedback = input("\n" + color.GREEN + "tell me how to make it better > " + color.END)
        if feedback.strip():
            return feedback
        elif feedback == "":
            return None

def build_prototype(brain,
                    project_manager,
                    designer,
                    business_owner,
                    engineer,
                    prompt = None,
                    sketch = None):

    prototype = None

    if prompt:
        if sketch:
            prototype = project_manager.meet_to_create_mockups(brain,
                                                               designer,
                                                               prompt,
                                                               sketch)
        else:
            project_manager.meet_to_create_requirements(brain,
                                                        business_owner,
                                                        prompt)

    if not prototype:
        prototype = project_manager.meet_to_build_prototype(brain,
                                                            engineer)

    while True:
        feedback = ask_for_feedback()
        if not feedback:
            break

        if sketch:
            project_manager.meet_to_address_feedback(brain,
                                                     designer,
                                                     sketch,
                                                     feedback)

        prototype = project_manager.meet_to_refactor(brain,
                                                     engineer,
                                                     prototype,
                                                     feedback)

    return prototype

def test_prototype(brain,
                   project_manager,
                   tester):
    return project_manager.meet_to_test_prototype(brain,
                                                  tester)

## create a team to encapsulate agents
def compose(brain,
            project_manager,
            designer,
            business_owner,
            engineer,
            tester,
            args):

    compose_tasks(brain,
                  project_manager,
                  designer,
                  args.tasks,
                  args)

    return None
