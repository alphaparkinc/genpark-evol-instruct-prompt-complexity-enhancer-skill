# genpark-evol-instruct-prompt-complexity-enhancer-skill

An algorithmic prompt mutation engine implementing the WizardLM Evol-Instruct paradigm. Synthesizes high-complexity training data from simple seed instructions through structured mutation templates.

## Architecture

```mermaid
flowchart TD
    Seed[Seed Instruction] --> Mutator[EvolInstructMutator]
    Mutator --> T1[Deepen Reasoning]
    Mutator --> T2[Add Constraints]
    Mutator --> T3[Concretize]
    Mutator --> T4[Increase Reasoning Steps]
    Mutator --> T5[In-Breadth Evolution]
    T2 --> Evaluator[Complexity Scoring Engine]
    Evaluator --> Mutated[High-Complexity Benchmark Dataset]
```

## Features
- **Deterministic Complexity Scoring**: Quantifies lexical length, logical connectives, and constraints.
- **5 Mutation Vectors**: Deepens reasoning, adds technical constraints, concretizes abstract ideas, expands step count, and expands cross-domain analogies.
- **100% Python Standard Library**: Zero pip dependencies.
- **Model Context Protocol (MCP)**: Native stdio server support.
