# Perplexity God Mode Prompt Engine

A modular prompt-engineering system for generating, critiquing, refining, and evaluating prompts with routing, benchmark datasets, and CI-ready regression checks.

## What this repo contains

- `perplexity_god_mode_v4.py` — the current prompt engine.
- `prompt_eval_runner.py` — the CI-ready evaluation runner.
- `prompt_golden_dataset.json` — the initial golden benchmark dataset.
- `eval_results/` — generated evaluation outputs such as JSON and CSV reports.
- `.github/workflows/prompt-eval.yml` — GitHub Actions workflow for smoke-suite evals.

## Core architecture

The engine is designed as a multi-pass system rather than a single prompt template.

Main components:
- `DomainPackRegistry` — chooses a domain pack such as coding, research, product, or documentation.
- `PromptMemory` — recalls reusable prompt patterns when enabled.
- `SchemaBuilder` — adds strict JSON schema instructions when required.
- `PromptGenerator` — builds the first draft prompt.
- `ConstraintInspector` — checks for contradictions and ambiguities.
- `PromptCritic` — scores the draft.
- `PromptRefiner` — rewrites the prompt based on critique results.
- `PromptVariantBuilder` — creates specialized variants.
- `PromptTestHarness` — runs fixture-style checks.
- `GodModeEngineV4` — orchestrates the pipeline.

## Benchmarking strategy

The benchmark harness is used to treat prompt quality like software quality.

The golden dataset should include:
- representative task types,
- routing edge cases,
- formatting-sensitive requests,
- contradiction cases,
- known historical failures.

Current benchmark checks include:
- domain-pack routing accuracy,
- required structure presence,
- execution-hook coverage,
- score thresholds,
- JSON/CSV artifact generation.

## Local usage

Run the engine directly:

```bash
python perplexity_god_mode_v4.py
```

Run the eval runner against the dataset:

```bash
python prompt_eval_runner.py \
  --engine perplexity_god_mode_v4.py \
  --dataset prompt_golden_dataset.json \
  --outdir eval_results
```

Run only the smoke suite:

```bash
python prompt_eval_runner.py --smoke-only
```

Limit the number of dataset cases:

```bash
python prompt_eval_runner.py --dataset-limit 10
```

## CI integration

A GitHub Actions workflow can run the smoke suite on pull requests and pushes that affect the engine, eval runner, or benchmark dataset.

Example workflow path:

```text
.github/workflows/prompt-eval.yml
```

Typical smoke-suite command:

```bash
python output/prompt_eval_runner.py --smoke-only --min-pass-rate 1.0 --min-pack-match-rate 1.0
```

Recommended CI policy:
- Run smoke suite on every PR.
- Run a broader regression suite on merges or nightly schedules.
- Upload JSON and CSV outputs as CI artifacts.
- Fail the build on routing or threshold regressions.

## Suggested repo layout

```text
.
├── perplexity_god_mode_v4.py
├── prompt_eval_runner.py
├── prompt_golden_dataset.json
├── eval_results/
├── .github/
│   └── workflows/
│       └── prompt-eval.yml
└── README.md
```

For a larger codebase, consider moving files into structured folders such as:

```text
prompt_engine/
evals/datasets/
evals/results/
.github/workflows/
```

## Git ignore guidance

Commit source-of-truth files such as:
- engine code,
- datasets,
- workflows,
- dependency manifests.

Ignore generated or local-only files such as:
- `__pycache__/`
- `.venv/`
- `.env`
- `eval_results/`
- IDE settings
- temporary logs and scratch outputs

Example:

```gitignore
__pycache__/
.venv/
.env
output/eval_results/
*.log
.vscode/
.idea/
```

## How to expand the benchmark

1. Add real failure cases from development or production.
2. Add routing tie-breaker cases across similar domains.
3. Add strict-format cases for JSON or documentation output.
4. Add contradiction-heavy prompts.
5. Track pass rates and score deltas over time.

A practical growth path:
- 5 cases for bootstrapping,
- 20–30 cases for smoke coverage,
- 50–100 cases for broader regression checks.

## Next improvements

High-value future work:
- domain-pack weighting improvements,
- stronger creative-task validation rules,
- externalized memory,
- benchmark versioning,
- nightly full-suite CI,
- answer-quality judging in addition to prompt-shape checks.
