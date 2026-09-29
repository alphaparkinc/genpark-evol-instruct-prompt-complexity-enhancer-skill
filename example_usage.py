from client import EvolInstructMutator

prompt = "Write a function to sort a list of numbers"
res = EvolInstructMutator.mutate(prompt, "add_constraints")
print("Original:", res["original_prompt"])
print("Mutated:", res["mutated_prompt"])
print("Complexity Gain:", res["complexity_gain"])
