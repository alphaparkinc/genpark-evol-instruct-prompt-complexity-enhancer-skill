"""Evol-Instruct Prompt Complexity Enhancer.
100% Python Standard Library.
"""

import re

class EvolInstructMutator:
    """Evolutionary prompt mutation algorithm adding constraints and deepening reasoning."""
    MUTATION_TEMPLATES = {
        "deepen_reasoning": "Analyze the underlying theoretical principles and explain the chain of thought step-by-step: {prompt}",
        "add_constraints": "{prompt}. In your response, ensure: 1) Strict standard library only, 2) Complete error handling, 3) Time complexity under O(N log N).",
        "concretize": "Provide an end-to-end practical real-world scenario illustrating: {prompt}",
        "increase_reasoning_steps": "Break down the following problem into at least 4 discrete sequential phases with verification checks at each phase: {prompt}",
        "in_breadth_evolution": "Create an analogous problem in a different domain that shares the identical mathematical structure as: {prompt}"
    }

    @classmethod
    def evaluate_complexity(cls, prompt: str) -> dict:
        words = re.findall(r'\b\w+\b', prompt)
        word_count = len(words)
        connectors = ["if", "because", "given", "moreover", "however", "assuming", "constraint", "therefore", "unless", "furthermore"]
        connector_count = sum(1 for w in words if w.lower() in connectors)
        has_numbered_list = bool(re.search(r'\b\d+[\.\)]\s', prompt))
        
        score = 1.0 + min(word_count / 15.0, 4.0) + min(connector_count * 0.8, 3.0) + (1.5 if has_numbered_list else 0.0)
        return {
            "word_count": word_count,
            "connector_count": connector_count,
            "has_numbered_list": has_numbered_list,
            "complexity_score": round(min(score, 10.0), 2)
        }

    @classmethod
    def mutate(cls, prompt: str, mutation_type: str = "deepen_reasoning") -> dict:
        template = cls.MUTATION_TEMPLATES.get(mutation_type, cls.MUTATION_TEMPLATES["deepen_reasoning"])
        mutated_prompt = template.format(prompt=prompt)
        orig_comp = cls.evaluate_complexity(prompt)
        new_comp = cls.evaluate_complexity(mutated_prompt)
        return {
            "original_prompt": prompt,
            "mutation_type": mutation_type,
            "mutated_prompt": mutated_prompt,
            "original_complexity": orig_comp["complexity_score"],
            "new_complexity": new_comp["complexity_score"],
            "complexity_gain": round(new_comp["complexity_score"] - orig_comp["complexity_score"], 2)
        }
