from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement = And(AKnight, AKnave)        # statment of A being both Knight and Knave

knowledge0 = And(

    Or(AKnight, AKnave),                # Knight or Knave is true
    Not(And(AKnight, AKnave)),              # but not both

    Implication(AKnave, Not(statement)),    # if knave the statement if false
    Implication(AKnight, statement)             # if knight the statement is true

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement = And(AKnave, BKnave)         # statement of a is knave and b is knave

knowledge1 = And(
    
    Or(AKnight, AKnave),                # Knight or Knave is true
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),              # but not both
    Not(And(BKnight, BKnave)),

    Implication(AKnave, Not(statement)),    # if knave the statement if false
    Implication(AKnight, statement)             # if knight the statement is true

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statementA = Or(And(AKnight, BKnight), And(AKnave, BKnave))
statementB = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    
    Or(AKnight, AKnave),                # Knight or Knave is true
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),              # but not both
    Not(And(BKnight, BKnave)),

    Implication(AKnave, Not(statementA)),    # if knave the statement if false
    Implication(AKnight, statementA),             # if knight the statement is true

    Implication(BKnave, Not(statementB)),
    Implication(BKnight, statementB)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
statementA = Or(AKnight, AKnave)
statementB = And(AKnave, CKnave)
statementC = AKnight

knowledge3 = And(
    
    Or(AKnight, AKnave),                # Knight or Knave is true
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Not(And(AKnight, AKnave)),              # but not both
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Implication(AKnave, Not(statementA)),    # if knave the statement if false
    Implication(AKnight, statementA),             # if knight the statement is true

    Implication(BKnave, Not(statementB)),
    Implication(BKnight, statementB),

    Implication(CKnave, Not(statementC)),
    Implication(CKnight, statementC)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
