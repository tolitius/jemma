try:
    from pyreadline3 import Readline # windows support
    readline = Readline()
except ImportError:
    import readline

from functools import partial
from jemma.tools import color, jemma_say, deploy

def compose_tasks(brain,
                  project_manager,
                  designer,        ## TODO: project_manager should have a designer OR there should be a Team
                  engineer,
                  tasks,
                  args):

    prompt = args.prompt
    sketch = args.sketch

    can_do = {
        'sketch-to-layout': {
            'fn': partial(designer.sketch_to_layout, brain),
            'needs': ['prompt', 'sketch'],
        },
        'sketch-to-spec': {
            'fn': partial(designer.sketch_to_specification, brain),
            'needs': ['prompt', 'sketch'],
        },
        'spec-to-css': {
            'fn': partial(designer.spec_to_css, brain),
            'needs': ['prompt', 'sketch', 'layout', 'spec'],
        },
        'spec-to-html': {
            'fn': partial(designer.spec_to_html, brain),
            'needs': ['prompt', 'sketch', 'layout', 'spec', 'css'],
        },
        'deploy': {
            'fn': partial(deploy),
            'needs': ['css', 'html'],
        },
        'take-feedback': {
            'fn': partial(ask_for_feedback),
            'provide-to': ['spec-to-css', 'spec-to-html'],
        },
        ## 'evaluate': {
        ##     'fn': partial(tester.validate-foo, brain),
        ##     'needs': ['css', 'html'],
        ## }
    }

    # validate all tasks before execution
    unknown_tasks = [task for task in tasks if task not in can_do]
    if unknown_tasks:
        raise Exception(f"don't know how to do this yet: {', '.join(unknown_tasks)}")

    ## handrolling Clojure's threading macro
    memory = {'prompt': prompt, 'sketch': sketch}

    for task in tasks:
        fn = can_do[task]['fn']
        needs = can_do[task].get('needs', [])

        ## if this tasks has "needs" validate that all that is "needed" is in memory
        missing_needs = [need for need in needs if need not in memory]
        if missing_needs:
            raise Exception(f"can't do \"{task}\" without \"{', '.join(missing_needs)}\"")

        if needs:
            jemma_say(f"task \"{task}\" <<< {list(memory.keys())}")
            fact = fn(memory)
        else:
            jemma_say(f"task \"{task}\" <<< [no input]")
            fact = fn()

        ## check that fact is a dict, if not raise an exception
        if not isinstance(fact, dict):
            raise Exception(f"task \"{task}\" did not return a dict, but {type(fact)} instead: {fact}")

        ## if any of fact keys already exist in memory, communicate a warning that they will be overwritten
        existing_facts = [k for k in fact if k in memory]
        if existing_facts:
            jemma_say(f"(!) task \"{task}\" >>> overwriting {', '.join(existing_facts)}")

        jemma_say(f"task \"{task}\" >>> {fact}")
        memory.update(fact)

    return fact

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
                  engineer,
                  args.tasks,
                  args)

    return None
