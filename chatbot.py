from pyswip import Prolog
import re

def initialize_prolog():
    prolog = Prolog()
    try:
        prolog.consult("relationships.pl")
    except Exception as e:
        return None, f"Error loading Prolog file: {str(e)}"
    return prolog, "Prolog initialized successfully."

def add_fact(prolog, fact):
    try:
        prolog.assertz(fact)

        # Check for contradictions
        contradictions = list(prolog.query("contradiction(Reason)"))
        #print("Contradictions found:", contradictions)  # Debug
        if contradictions:
            # If a contradiction is found, remove fact
            prolog.retract(fact)
            return False
        return True,
    except Exception as e:
        return f"Error: {str(e)}"

def handle_help():
    print("\nStatement Prompts:")
    print("\t___ and ___ are siblings.")
    print("\t___ is a brother of ___.")
    print("\t___ is a sister of ___.")
    print("\t___ is the father of ___.")
    print("\t___ is the mother of ___.")
    print("\t___ is the parent of ___.")
    print("\t___ and ___ are the parents of ___.")
    print("\t___ is a grandmother of ___.")
    print("\t___ is a grandfather of ___.")
    print("\t___ is a child of ___.")
    print("\t___, ___ and ___ are children of ___.")
    print("\t___ is a daughter of ___.")
    print("\t___ is a son of ___.")
    print("\t___ is an uncle of ___.")
    print("\t___ is an aunt of ___.")
    print("\t___ and ___ are cousins.")
    print("\t___ is a male.")
    print("\t___ is a female.")

    print("\nQuestion Prompts:")
    print("\tAre ___ and ___ siblings?")
    print("\tWho are the siblings of ___?")
    print("\tIs ___ a sister of ___?")
    print("\tWho are the sisters of ___?")
    print("\tIs ___ a brother of ___?")
    print("\tWho are the brothers of ___?")
    print("\tIs ___ the mother of ___?")
    print("\tWho is the mother of ___?")
    print("\tIs ___ the father of ___?")
    print("\tWho is the father of ___?")
    print("\tAre ___ and ___ the parents of ___?")
    print("\tWho are the parents of ___?")
    print("\tIs ___ a grandmother of ___?")
    print("\tIs ___ a grandfather of ___?")
    print("\tIs ___ a daughter of ___?")
    print("\tWho are the daughters of ___?")
    print("\tIs ___ a son of ___?")
    print("\tWho are the sons of ___?")
    print("\tIs ___ a child of ___?")
    print("\tWho are the children of ___?")
    print("\tAre ___, ___, and ___ children of ___?")
    print("\tIs ___ an aunt of ___?")
    print("\tIs ___ an uncle of ___?")
    print("\tAre ___ and ___ relatives?\n")

    return "To start, try to input any one of these statements!"

def handle_statement(prolog, statement):
    statement = statement.strip()
    statement = statement.lower()

    # Handle "X and Y are siblings"
    sibling_match = re.match(r"([a-z]+) and ([a-z]+) are siblings\.", statement)

    if sibling_match:
        # Parse the input
        sib1, sib2 = sibling_match.groups()
        print(sib1, sib2) # DEBUG

        # Add the facts
        add_sibling1 = add_fact(prolog, f"sibling('{sib1}', '{sib2}')")
        add_sibling2 = add_fact(prolog, f"sibling('{sib2}', '{sib1}')")

        # Return appropriate output
        if add_sibling1 and add_sibling2:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a brother of Y"
    brother_match = re.match(r"([a-z]+) is a brother of ([a-z]+)\.", statement)

    if brother_match:
        # Parse the input
        brother, person = brother_match.groups()
        print(brother, person) # DEBUG

        # Add the facts
        add_sibling1 = add_fact(prolog, f"sibling('{brother}', '{person}')")
        add_sibling2 = add_fact(prolog, f"sibling('{person}', '{brother}')")
        add_sex = add_fact(prolog, f"male('{brother}')")

        # Return appropriate output
        if add_sibling1 and add_sibling2 and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a sister of Y"
    sister_match = re.match(r"([a-z]+) is a sister of ([a-z]+)\.", statement)

    if sister_match:
        # Parse the input
        sister, person = sister_match.groups()
        print(sister, person) # DEBUG

        # Add the facts
        add_sibling1 = add_fact(prolog, f"sibling('{sister}', '{person}')")
        add_sibling2 = add_fact(prolog, f"sibling('{person}', '{sister}')")
        add_sex = add_fact(prolog, f"female('{sister}')")

        # Return appropriate output
        if add_sibling1 and add_sibling2 and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is the father of Y"
    father_match = re.match(r"([a-z]+) is the father of ([a-z]+)\.", statement)

    if father_match:
        # Parse the input
        father, child = father_match.groups()
        print(father, child) # DEBUG

        # Add the facts
        add_parent = add_fact(prolog, f"parent('{father}', '{child}')")
        add_child = add_fact(prolog, f"child('{child}', '{father}')")
        add_sex = add_fact(prolog, f"male('{father}')")

        # Return appropriate output
        if add_parent and add_child and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is the mother of Y"
    mother_match = re.match(r"([a-z]+) is the mother of ([a-z]+)\.", statement)

    if mother_match:
        # Parse the input
        mother, child = mother_match.groups()
        print(mother, child) # DEBUG

        # Add the facts
        add_parent = add_fact(prolog, f"parent('{mother}', '{child}')")
        add_child = add_fact(prolog, f"child('{child}', '{mother}')")
        add_sex = add_fact(prolog, f"female('{mother}')")

        # Return appropriate output
        if add_parent and add_child and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is the parent of Y"
    parent_match = re.match(r"([a-z]+) is the parent of ([a-z]+)\.", statement)

    if parent_match:
        # Parse the input
        parent, child = parent_match.groups()
        print(parent, child) # DEBUG

        # Add the facts
        add_parent = add_fact(prolog, f"parent('{parent}', '{child}')")
        add_child = add_fact(prolog, f"child('{child}', '{parent}')")

        # Return appropriate output
        if add_parent and add_child:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."


    # Handle "X and Y are the parents of Z"
    parents_match = re.match(r"([a-z]+) and ([a-z]+) are the parents of ([a-z]+)\.", statement)

    if parents_match:
        # Parse the input
        parent1, parent2, child = parents_match.groups()
        print(parent1, parent2, child) # DEBUG

        # Add the facts
        add_parent1 = add_fact(prolog, f"parent('{parent1}', '{child}')")
        add_parent2 = add_fact(prolog, f"parent('{parent2}', '{child}')")
        add_child1 = add_fact(prolog, f"child('{child}', '{parent2}')")
        add_child2 = add_fact(prolog, f"child('{child}', '{parent2}')")

        # Return appropriate output
        if add_parent1 and add_parent2 and add_child1 and add_child2:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a grandmother of Y"
    grandmother_match = re.match(r"([a-z]+) is a grandmother of ([a-z]+)\.", statement)

    if grandmother_match:
        # Parse the input
        grandmother, grandchild = grandmother_match.groups()
        print(grandmother, grandchild) # DEBUG

        # Add the facts
        add_grandparent = add_fact(prolog, f"grandparent('{grandmother}', '{grandchild}')")
        add_grandchild = add_fact(prolog, f"grandchild('{grandchild}', '{grandmother}')")
        add_sex = add_fact(prolog, f"female('{grandmother}')")

        # Return appropriate output
        if add_grandparent and add_grandchild and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a grandfather of Y"
    grandfather_match = re.match(r"([a-z]+) is a grandfather of ([a-z]+)\.", statement)

    if grandfather_match:
        # Parse the input
        grandfather, grandchild = grandfather_match.groups()
        print(grandfather, grandchild) # DEBUG

        # Add the facts
        add_grandparent = add_fact(prolog, f"grandparent('{grandfather}', '{grandchild}')")
        add_grandchild = add_fact(prolog, f"grandchild('{grandchild}', '{grandfather}')")
        add_sex = add_fact(prolog, f"male('{grandfather}')")

        # Return appropriate output
        if add_grandparent and add_grandchild and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a child of Y"
    child_match = re.match(r"([a-z]+) is a child of ([a-z]+)\.", statement)

    if child_match:
        # Parse the input
        child, parent = child_match.groups()
        print(child, parent) # DEBUG

        # Add the facts
        add_child = add_fact(prolog, f"child('{child}', '{parent}')")
        add_parent = add_fact(prolog, f"parent('{parent}', '{child}')")

        # Return appropriate output
        if add_child and add_parent:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X, Y, and Z are children of W"
    children_match = re.match(r"([a-z]+), ([a-z]+), and ([a-z]+) are children of ([a-z]+)\.", statement)

    if children_match:
        # Parse the input
        child1, child2, child3, parent = children_match.groups()
        print(child1, child2, child3, parent) # DEBUG

        # Add the facts
        add_child1 = add_fact(prolog, f"child('{child1}', '{parent}')")
        add_child2 = add_fact(prolog, f"child('{child2}', '{parent}')")
        add_child3 = add_fact(prolog, f"child('{child3}', '{parent}')")
        add_parent1 = add_fact(prolog, f"parent('{parent}', '{child1}')")
        add_parent2 = add_fact(prolog, f"parent('{parent}', '{child2}')")
        add_parent3 = add_fact(prolog, f"parent('{parent}', '{child3}')")

        # Return appropriate output
        if add_child1 and add_child2 and add_child3 and add_parent1 and add_parent2 and add_parent3:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a daughter of Y"
    daughter_match = re.match(r"([a-z]+) is a daughter of ([a-z]+)\.", statement)

    if daughter_match:
        # Parse the input
        daughter, parent = daughter_match.groups()
        print(daughter, parent) # DEBUG

        # Add the facts
        add_child = add_fact(prolog, f"child('{daughter}', '{parent}')")
        # Commenting out because it adds an extra fact
        add_parent = add_fact(prolog, f"parent('{parent}', '{daughter}')")
        add_sex = add_fact(prolog, f"female('{daughter}')")

        # Return appropriate output

        # Commenting out because it adds an extra fact
        if add_child and add_parent and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a son of Y"
    son_match = re.match(r"([a-z]+) is a son of ([a-z]+)\.", statement)

    if son_match:
        # Parse the input
        son, parent = son_match.groups()
        print(son, parent) # DEBUG

        # Add the facts
        add_child = add_fact(prolog, f"child('{son}', '{parent}')")
        # Commenting out because it adds an extra fact
        add_parent = add_fact(prolog, f"parent('{parent}', '{son}')")
        add_sex = add_fact(prolog, f"male('{son}')")

        # Return appropriate output
        # Commenting out because it adds an extra fact
        if add_child and add_parent and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is an uncle of Y"
    uncle_match = re.match(r"([a-z]+) is an uncle of ([a-z]+)\.", statement)

    if uncle_match:
        # Parse the input
        uncle, person = uncle_match.groups()
        print(uncle, person) # DEBUG

        # Add the facts
        add_uncle = add_fact(prolog, f"uncle('{uncle}', '{person}')")
        add_sex = add_fact(prolog, f"male('{uncle}')")

        # Return appropriate output
        if add_uncle and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is an aunt of Y"
    aunt_match = re.match(r"([a-z]+) is an aunt of ([a-z]+)\.", statement)

    if aunt_match:
        # Parse the input
        aunt, person = aunt_match.groups()
        print(aunt, person) # DEBUG

        # Add the facts
        add_aunt = add_fact(prolog, f"aunt('{aunt}', '{person}')")
        add_sex = add_fact(prolog, f"female('{aunt}')")

        # Return appropriate output
        if add_aunt and add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a male"
    male_match = re.match(r"([a-z]+) is a male\.", statement)

    if male_match:
        # Parse the input
        male = male_match.groups()[0]
        print(male)  # DEBUG

        # Add the facts
        add_sex = add_fact(prolog, f"male('{male}')")

        # Return appropriate output
        if add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Handle "X is a female"
    female_match = re.match(r"([a-z]+) is a female\.", statement)

    if female_match:
        # Parse the input
        female = female_match.groups()[0]
        print(female)  # DEBUG

        # Add the facts
        add_sex = add_fact(prolog, f"female('{female}')")

        # Return appropriate output
        if add_sex:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."
        
    # Handle "X and Y are cousins."
    cousin_match = re.match(r"([a-z]+) and ([a-z]+) are cousins\.", statement)

    if cousin_match:
        # Parse the input
        cousin1, cousin2 = cousin_match.groups()
        print(cousin1, cousin2) # DEBUG

        # Add the facts
        add_cousin1 = add_fact(prolog, f"cousin('{cousin1}', '{cousin2}')")
        add_cousin2 = add_fact(prolog, f"cousin('{cousin2}', '{cousin1}')")

        # Return appropriate output
        if add_cousin1 and add_cousin2:
            return "OK! I learned something."
        else:
            return "Oops! Something went wrong."

    # Unrecognized pattern
    return "I apologize, I do not recognize your statement format."

def handle_question(prolog, question):
    question = question.strip()
    question = question.lower()

    # Handle "Are X and Y siblings?"
    sibling_question_match = re.match(r"are ([a-z]+) and ([a-z]+) siblings\?", question)
    if sibling_question_match:
        # Parse the input
        sib1, sib2 = sibling_question_match.groups()
        print(sib1, sib2) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"sibling('{sib1}', '{sib2}')")) else "No!"
    
    # Handle "Who are the siblings of X?"
    siblings_question_match = re.match(r"who are the siblings of ([a-z]+)\?", question)
    if siblings_question_match:
        # Parse the input
        person = siblings_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        siblings = list(prolog.query(f"sibling(X, '{person}')"))
        return ", ".join([s['X'].capitalize() for s in siblings]) if siblings else "No siblings found."

    # Handle "Is X a sister of Y?"
    sister_question_match = re.match(r"is ([a-z]+) a sister of ([a-z]+)\?", question)
    if sister_question_match:
        # Parse the input
        sister, person = sister_question_match.groups()
        print(sister, person) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"sister('{sister}', '{person}')")) else "No!"

    # Handle "Who are the sisters of X?"
    sisters_question_match = re.match(r"who are the sisters of ([a-z]+)\?", question)
    if sisters_question_match:
        # Parse the input
        person = sisters_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        sisters = list(prolog.query(f"sister(X, '{person}')"))
        return ", ".join([s['X'].capitalize() for s in sisters]) if sisters else "No sisters found."

    # Handle "Is X a brother of Y?"
    brother_question_match = re.match(r"is ([a-z]+) a brother of ([a-z]+)\?", question)
    if brother_question_match:
        # Parse the input
        brother, person = brother_question_match.groups()
        print(brother, person) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"brother('{brother}', '{person}')")) else "No!"

    # Handle "Who are the brothers of X?"
    brothers_question_match = re.match(r"who are the brothers of ([a-z]+)\?", question)
    if brothers_question_match:
        # Parse the input
        person = brothers_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        brothers = list(prolog.query(f"brother(X, '{person}')"))
        return ", ".join([s['X'].capitalize() for s in brothers]) if brothers else "No brothers found."

    # Handle "Is X the mother of Y?"
    mother_question_match = re.match(r"is ([a-z]+) the mother of ([a-z]+)\?", question)
    if mother_question_match:
        # Parse the input
        mother, child = mother_question_match.groups()
        print(mother, child) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"mother('{mother}', '{child}')")) else "No!"

    # Handle "Who is the mother of X?"
    mother_of_question_match = re.match(r"who is the mother of ([a-z]+)\?", question)
    if mother_of_question_match:
        # Parse the input
        child = mother_of_question_match.group(1)
        print(child) # DEBUG

        # Return appropriate output
        mothers = list(prolog.query(f"mother(X, '{child}')"))
        return mothers[0]['X'].capitalize() if mothers else "No mother found."

    # Handle "Is X the father of Y?"
    father_question_match = re.match(r"is ([a-z]+) the father of ([a-z]+)\?", question)
    if father_question_match:
        # Parse the input
        father, child = father_question_match.groups()
        print(father, child) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"father('{father}', '{child}')")) else "No!"

    # Handle "Who is the father of X?"
    father_of_question_match = re.match(r"who is the father of ([a-z]+)\?", question)
    if father_of_question_match:
        # Parse the input
        child = father_of_question_match.group(1)
        print(child) # DEBUG

        # Return appropriate output
        fathers = list(prolog.query(f"father(X, {child})"))
        return f"The father of {child} is {fathers[0]['X']}." if fathers else "No father found."

    # Handle "Are X and Y the parents of Z?"
    parents_question_match = re.match(r"are ([a-z]+) and ([a-z]+) the parents of ([a-z]+)\?", question)
    if parents_question_match:
        # Parse the input
        parent1, parent2, child = parents_question_match.groups()
        print(parent1, parent2, child) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"father('{parent1}', '{child}')")) and list(prolog.query(f"mother('{parent2}', '{child}')")) else "No!"

    # Handle "Who are the parents of X?"
    parents_of_question_match = re.match(r"who are the parents of ([a-z]+)\?", question)
    if parents_of_question_match:
        # Parse the input
        person = parents_of_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        parents = list(prolog.query(f"parent(X, '{person}')"))
        return ", ".join([s['X'].capitalize() for s in parents]) if parents else "No parents found."
    
    # Handle "Is X a grandmother of Y?"
    grandmother_question_match = re.match(r"is ([a-z]+) a grandmother of ([a-z]+)\?", question)
    if grandmother_question_match:
        # Parse the input
        grandmother, grandchild = grandmother_question_match.groups()
        print(grandmother, grandchild) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"grandmother('{grandmother}', '{grandchild}')")) else "No!"

    # Handle "Is X a grandfather of Y?"
    grandfather_question_match = re.match(r"is ([a-z]+) a grandfather of ([a-z]+)\?", question)
    if grandfather_question_match:
        # Parse the input
        grandfather, grandchild = grandfather_question_match.groups()
        print(grandfather, grandchild) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"grandfather('{grandfather}', '{grandchild}')")) else "No!"

    # Handle "Is X a daughter of Y?"
    daughter_question_match = re.match(r"is ([a-z]+) a daughter of ([a-z]+)\?", question)
    if daughter_question_match:
        # Parse the input
        daughter, parent = daughter_question_match.groups()
        print(daughter, parent) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"daughter('{daughter}', '{parent}')")) else "No!"
    # Handle "Who are the daughters of X?"
    daughters_of_question_match = re.match(r"who are the daughters of ([a-z]+)\?", question)
    if daughters_of_question_match:
        # Parse the input
        person = daughters_of_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        daughters = list(prolog.query(f"daughter(X, '{person}')"))
        return ", ".join(set([s['X'].capitalize() for s in daughters])) if daughters else "No daughters found."
    
    # Handle "Is X a son of Y?"
    son_question_match = re.match(r"is ([a-z]+) a son of ([a-z]+)\?", question)
    if son_question_match:
        # Parse the input
        son, parent = son_question_match.groups()
        print(son, parent) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"son('{son}', '{parent}')")) else "No!"
    # Handle "Who are the sons of X?"
    sons_of_question_match = re.match(r"who are the sons of ([a-z]+)\?", question)
    if sons_of_question_match:
        # Parse the input
        person = sons_of_question_match.group(1)
        print(person) # DEBUG

        # Return appropriate output
        sons = list(prolog.query(f"son(X, '{person}')"))
        return ", ".join(set([s['X'].capitalize() for s in sons])) if sons else "No sons found."

    # Handle "Is X a child of Y?"
    child_question_match = re.match(r"is ([a-z]+) a child of ([a-z]+)\?", question)
    if child_question_match:
        # Parse the input
        child, parent = child_question_match.groups()
        print(child, parent) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"child('{child}', '{parent}')")) else "No!"
    # Handle "Who are the children of X?"
    children_of_question_match = re.match(r"who are the children of ([a-z]+)\?", question)
    if children_of_question_match:
        # Parse the input
        person = children_of_question_match.group(1)
        print(person)  # DEBUG

        # Return appropriate output
        children = list(prolog.query(f"child(X, '{person}')"))
        return ", ".join(set([s['X'].capitalize() for s in children])) if children else "No children found."

    # Handle "Are X, Y, and Z children of P?"
    childrens_question_match = re.match(r"are ([a-z]+), ([a-z]+), and ([a-z]+) children of ([a-z]+)\?", question)
    if childrens_question_match:
        # Parse the input
        child1, child2, child3,parent = childrens_question_match.groups()
        print(child1, child2, child3, parent) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"child('{child1}', '{parent}')")) and list(prolog.query(f"child('{child2}', '{parent}')")) and list(prolog.query(f"child('{child3}', '{parent}')")) else "No!"

    # Handle "Is X an aunt of Y?"
    aunt_question_match = re.match(r"is ([a-z]+) an aunt of ([a-z]+)\?", question)
    if aunt_question_match:
        # Parse the input
        aunt, person = aunt_question_match.groups()
        print(aunt, person) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"aunt('{aunt}', '{person}')")) else "No!"

    # Handle "Is X an uncle of Y?"
    uncle_question_match = re.match(r"is ([a-z]+) an uncle of ([a-z]+)\?", question)
    if uncle_question_match:
        # Parse the input
        uncle, person = uncle_question_match.groups()
        print(uncle, person) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"uncle('{uncle}', '{person}')")) else "No!"

    # Handle "Are X and Y relatives?"
    relatives_question_match = re.match(r"are ([a-z]+) and ([a-z]+) relatives\?", question)
    if relatives_question_match:
        # Parse the input
        person1, person2 = relatives_question_match.groups()
        print(person1, person2) # DEBUG

        # Return appropriate output
        return "Yes!" if list(prolog.query(f"relative('{person1}', '{person2}')")) else "No!"

    return "I apologize, I do not understand the question."

def main():
    prolog, message = initialize_prolog()
    if prolog is None:
        print(message)
        return

    print("\nFamGPT: Welcome to FamGPT, the Family Relationship Chatbot!")

    while True:
        user_input = input("\n> ")
        if user_input.lower() in ["exit", "quit"]:
            print("FamGPT: See you again!")
            break
        elif "help" in user_input:
            response = handle_help()
        elif "?" in user_input:
            response = handle_question(prolog, user_input)
        elif "." in user_input:
            response = handle_statement(prolog, user_input)
        else:
            response = "Unrecognized input format."

        print("FamGPT:", response)

if __name__ == "__main__":
    main()
