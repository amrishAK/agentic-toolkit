# Shared code-quality guidelines

Use these language-neutral principles with the [code-quality workflow](../../implementation/code-quality-workflow.md) and applicable [language-specific guidance](programming-language-matrix.md). They are design heuristics, not language rules, compliance criteria, or rigid metrics; project conventions and language correctness take precedence.

## Choose the smallest complete solution

Before adding code, consider in order:

1. Does the requested behavior need to be added or changed?
2. Can existing project code or an established project pattern meet the need?
3. Can a standard library or supported platform capability meet it?
4. If new code is needed, what is the smallest clear solution that fully satisfies the contract?

Do not add dependencies, abstractions, configuration, or flexibility without a concrete need. Prefer clarity and correctness over a short or clever diff.

## Preserve design quality

- Choose names that convey domain meaning and keep functions and modules cohesive. Single responsibility concerns meaningful reasons for change, not how many steps a function performs.
- Prefer explicit contracts, straightforward control flow, and intentional error handling. Do not impose arbitrary limits on function length, nesting, or parameter counts.
- Keep APIs narrow and dependencies clear. Introduce abstraction where it addresses a demonstrated boundary, reuse, variation, or testability need.
- Open/closed is not a ban on editing code or using branching. Preserve documented contracts for interchangeable implementations; do not strengthen preconditions or weaken postconditions.
- Keep interfaces cohesive and avoid forcing clients to depend on unrelated operations. Dependency inversion is not a mandate to add an interface for every concrete type.
- Share genuinely common concepts without premature DRY abstractions. Avoid speculative frameworks and needless layers.
- Evaluate boolean and output parameters in context rather than treating them as automatic defects.
- Comments explain intent, invariants, ownership, safety, and non-obvious decisions. Accurate public API documentation remains important even when the implementation looks simple.

## Do not trade away safeguards

Simplicity must not remove correctness, security, accessibility, input validation at trust boundaries, error handling needed to prevent data loss, or verification appropriate to the change. Preserve public contracts and account for important edge cases.
