



How do i create new skills for you?
Completed 2 steps
You can create new skills for me by defining a clear task, packaging instructions or code around it, and then asking me to use that skill when the right kind of request comes up. The most practical way is to make the skill specific enough that it does one job well, like reviewing code, extracting data, or formatting a certain kind of output.

What a skill usually contains
A skill normally includes a short description of what it does, plus any supporting files such as scripts, references, or assets. In the Gemini-style skill model, that means a SKILL.md file with metadata and optional folders like scripts/, references/, and assets/.

How to design one
Start with a narrow, repeatable task you want me to handle the same way every time. Write down the exact inputs, the expected output, and any rules or edge cases, then test it on a few real examples so the instructions are unambiguous.

A simple pattern
For example, you could create a “card-list-cleaner” skill that takes raw trading card notes and turns them into structured fields like name, set, rarity, and condition. The skill would need a clear description, formatting rules, and maybe a small script if the transformation is deterministic.

Best next step
If you want, I can help you draft a skill spec right here: name, purpose, inputs, output format, and trigger examples. Would you like to build one for your trading card app, like OCR cleanup, valuation lookup, or card data normalization?

Review the following code and create a skill file for it.

class PerplexityGodMode:
def __init__(self):
self.system_prompt = """
You are Perplexity's enhanced prompt engineer, operating in God Mode.
Your expertise encompasses:
1. Advanced prompt engineering techniques
2. Multi-step reasoning chains
3. Contextual adaptation across domains
4. Complex instruction following with clarity
5. Creative and analytical thinking at scale

You will generate prompts that:
- Maximize usefulness and quality of responses
- Employ strategy and pattern recognition
- Suggest innovative approaches to complex challenges
- Use frameworks for deep thinking and comprehensive analysis

When generating prompts:
- Always start with context (around 10-20 words)
- Include specific role/character
- Define the precise action or output type
- Add constraints and parameters
- Use strategic examples and methods
- Make it adaptable to different use cases
"""

def generate_powerful_prompt(self, task_type, domain=None, complexity="medium"):
"""
Generate an advanced prompt using multi-layered reasoning and optimization

Args:
task_type: Type of prompt needed (analysis, creative, technical, etc)
domain: Specific domain if applicable
complexity: Level of detail required

Returns:
Enhanced prompt with strategic framework
"""

# Define framework templates based on type
framework_templates = {
"analysis": """
You are a world-class analytical expert specializing in {domain}.
Analyze the following concept through 5 distinct lenses:
1. Historical Context
2. Current Applications
3. Future Implications
4. Critical Assessment
5. Strategic Recommendations
Answer with comprehensive insights for {complexity} complexity.
""",

"creative": """
You are a creative genius expert in {domain}.
Generate 3 innovative solutions to the problem using:
- Analogies from unrelated fields
- Reverse thinking approaches
- Creative constraints-based brainstorming
Present each solution with implementation details and potential challenges.
""",

"technical": """
You are a leading expert in {domain} with deep technical knowledge.
Please explain the concept in 3 levels of detail:
Level 1: High-level overview for general audiences
Level 2: Deep technical breakdown with examples
Level 3: Advanced implementation considerations
Ensure accuracy and clarity throughout.
"""
}

# Select appropriate framework
framework = framework_templates.get(task_type, framework_templates["analysis"])

# Inject domain and complexity
prompt = framework.format(
domain=domain or "multiple domains",
complexity=complexity
)

# Add enhancement layer
enhanced_prompt = f"""
{self.system_prompt}

Your core task:
{prompt}

Format your response in this structure:
[CONTEXT] - Brief relevant background (50 words max)
[ROLE] - Specific expert persona
[ACTION] - Required output type and quality
[METHOD] - Analytical framework or approach
[RESULT] - Well-structured comprehensive answer

Remember: Aim for perfection, clarity, and maximum utility.
"""

return enhanced_prompt

# Example usage
god_mode = PerplexityGodMode()

# Generate different types of prompts
creative_prompt = god_mode.generate_powerful_prompt(
task_type="creative",
domain="AI ethics",
complexity="high"
)

technical_prompt = god_mode.generate_powerful_prompt(
task_type="technical",
domain="machine learning",
complexity="medium"
)

analysis_prompt = god_mode.generate_powerful_prompt(
task_type="analysis",
domain="sustainable development",
complexity="high"
)

print("=== God Mode Prompts ===")
print("Creativity Prompt:", creative_prompt[:150] + "...")
print("Technical Prompt:", technical_prompt[:150] + "...")
print("Analysis Prompt:", analysis_prompt[:150] + "...")
Completed 3 steps
perplexity-god-mode-skill
PerplexityGodMode Skill
Review
This class is a solid prompt-template generator for three common modes: analysis, creative work, and technical explanation. Its strengths are a simple API, readable template separation, and predictable output structure.

What works well
The framework_templates dictionary makes the behavior easy to extend.

The fallback to analysis prevents total failure on unknown task_type values.

The final response scaffold ([CONTEXT], [ROLE], [ACTION], [METHOD], [RESULT]) gives the generated prompt a consistent shape.

The domain or "multiple domains" fallback is practical and avoids null formatting issues.

Issues to fix
self.system_prompt is written as a broad persona block, but it is inserted into the returned prompt rather than being used as an actual system instruction. That makes the output verbose and can blur the boundary between meta-instructions and task instructions.

The comment says context should be around 10–20 words, but the output format asks for [CONTEXT] - Brief relevant background (50 words max). Those rules conflict.

complexity only changes one interpolated phrase in the templates, so it does not meaningfully affect depth, verbosity, or reasoning strategy.

The method returns a large freeform string, which is harder to validate, test, or post-process than a structured object.

The example code truncates printed output, which is fine for demos, but it does not verify prompt quality or correctness.

There is no input validation for unsupported complexity values or empty task types.

Recommended improvements
Separate system guidance from generated user prompt text.

Replace freeform templates with structured sections assembled from reusable blocks.

Map complexity to explicit behaviors, for example:

low: concise, 3 bullets, limited jargon

medium: balanced depth with one example

high: multi-perspective analysis, tradeoffs, implementation detail

Validate inputs with allowed enums for task_type and complexity.

Return both a raw prompt and metadata, such as selected template, domain, and constraints.

Add an optional output_format parameter like markdown, json, bullets, or table.

Skill file
text
---
name: perplexity-god-mode
version: 1.0.0
description: Generates high-quality prompts for analysis, creative ideation, and technical explanation using a structured prompt-building framework.
triggers:
  - prompt generation
  - improve this prompt
  - write a better AI prompt
  - analysis prompt
  - creative prompt
  - technical prompt
inputs:
  - task_type
  - domain
  - complexity
  - goal
  - constraints
  - output_format
outputs:
  - optimized_prompt
  - rationale
  - suggested_variants
---

# Perplexity God Mode

Use this skill when the user wants a stronger prompt for another AI system, a reusable prompt template, or a domain-adapted instruction set.

## Purpose

Create a polished prompt that is specific, adaptable, and easy to reuse. The skill should turn vague requests into prompts with a clear role, task, method, constraints, and output format.

## Input contract

- `task_type`: one of `analysis`, `creative`, `technical`
- `domain`: optional subject area, default to `general`
- `complexity`: one of `low`, `medium`, `high`
- `goal`: the user's actual task or desired outcome
- `constraints`: optional limits such as word count, audience, tone, or banned content
- `output_format`: optional preferred response shape, such as `markdown`, `json`, `bullets`, `table`

## Behavior

1. Infer missing structure from the user's goal.
2. Select a framework based on `task_type`.
3. Adapt depth and specificity based on `complexity`.
4. Produce one primary optimized prompt.
5. Produce 2 alternative variants when the task could benefit from different strategies.
6. Keep prompts practical, not theatrical; avoid exaggerated claims like “perfect” or “genius” unless the user explicitly wants that tone.

## Frameworks

### Analysis

Use when the user wants evaluation, comparison, diagnosis, planning, or strategic thinking.

Structure the prompt around:
- Context
- Expert role
- Core question
- Analytical lenses
- Constraints
- Output structure

Default analytical lenses:
1. Background
2. Current state
3. Risks and tradeoffs
4. Opportunities
5. Recommendation

### Creative

Use when the user wants brainstorming, storytelling, ideation, naming, concept generation, or unconventional solutions.

Structure the prompt around:
- Context
- Creative role
- Challenge statement
- Idea-generation methods
- Constraints
- Output structure

Default methods:
- Cross-domain analogy
- Reverse thinking
- Constraint-based ideation

### Technical

Use when the user wants explanations, implementation plans, architecture guidance, debugging strategy, or code-oriented outputs.

Structure the prompt around:
- Context
- Technical role
- Problem statement
- Explanation depth levels
- Constraints
- Output structure

Default explanation levels:
1. Plain-language overview
2. Detailed technical breakdown
3. Implementation considerations

## Complexity mapping

### Low
- Keep the prompt compact.
- Ask for concise output.
- Limit response to essentials.
- Prefer plain language.

### Medium
- Ask for balanced depth.
- Include one example or concrete scenario.
- Include tradeoffs where relevant.

### High
- Ask for multi-step reasoning.
- Require assumptions, tradeoffs, edge cases, and implementation detail.
- Encourage multiple perspectives or alternatives.

## Output template

Return results in this format:

### Optimized prompt
[final prompt text]

### Why this works
- Role clarity
- Task specificity
- Chosen framework
- Constraint handling
- Output formatting logic

### Variants
- Variant A: more concise
- Variant B: more exploratory

## Prompt assembly rules

Every generated prompt should include:
- A short context opener
- A clear role
- An explicit task
- A method or framework
- Relevant constraints
- A specified output format

Avoid:
- Empty hype
- Contradictory constraints
- Overly long persona descriptions
- Vague verbs like “discuss” when “compare”, “diagnose”, or “design” would be better

## Example invocation

Input:
- `task_type`: `technical`
- `domain`: `machine learning`
- `complexity`: `medium`
- `goal`: `Explain overfitting and how to reduce it for a junior developer`
- `constraints`: `Use one practical example and avoid advanced math`
- `output_format`: `markdown`

Output:

### Optimized prompt
You are an experienced machine learning engineer. Explain overfitting to a junior developer using clear language and one practical example. Structure the answer in three parts: a plain-language definition, why it happens in real projects, and concrete ways to reduce it in implementation. Avoid advanced math, define technical terms briefly, and format the answer in markdown with short sections and bullet points where useful.

Open perplexity-god-mode-skill
I reviewed the code and created a reusable skill file as a downloadable Markdown artifact. The review notes that the class has a clean template-based structure, but it mixes persona text with task output, uses complexity too weakly, and has a few conflicting instructions that should be normalized before production use .

Main findings
The strongest part of the code is its simple prompt-builder pattern: template selection by task_type, fallback behavior, and consistent final sections make it easy to extend . The main weakness is that it generates a large meta-prompt blob instead of a more testable structured result, which makes validation, reuse, and downstream parsing harder .

What’s in the skill
The skill file includes:

A concise code review.

A proposed skill spec with front matter.

Inputs, outputs, behavior rules, framework selection, and complexity mapping.

An example invocation rewritten into a cleaner, more practical prompt pattern .

Recommended direction
For your use case, I’d treat this less like “God Mode” and more like a prompt-orchestration skill with strict enums, predictable output sections, and optional JSON output for app integration . That would fit well with your development workflow if you want to plug prompt generation into a FastAPI or React toolchain .

So take it, fix the weak points, re write it, review it, and build upon it. Re write that, review, build, until it is a God Mode level.
Completed 3 steps
perplexity_god_mode_v2_review
Perplexity God Mode v2
Overview
This rewrite upgrades the original class from a themed prompt string generator into a more robust prompt-construction engine. The new version adds typed enums, structured request and response models, stronger complexity handling, richer frameworks, better validation, and reusable diagnostics.

What was fixed
Structural problems removed
The original version mixed persona text and task instructions into one oversized prompt blob.

The rewrite separates identity, framework selection, complexity rules, constraints, examples, and output structure.

The result is easier to test, extend, and embed in an application.

Weak complexity handling fixed
The original code only interpolated the word complexity into a sentence. The rewrite maps each complexity level to distinct behavior for depth, reasoning style, and scope.

Input safety improved
The rewrite validates the request, uses enums for task_type and complexity, and uses dataclasses so the contract is explicit.

New capabilities added
Added strategy and debug task types.

Added audience, constraints, examples, and output_format.

Added prompt variants for concise, exploratory, and execution-focused outputs.

Added rationale and diagnostics metadata.

Review of the rewrite
Strengths
The API is now much more production-friendly.

The generated prompt is cleaner and more reusable.

The system can support app-level orchestration because it returns metadata instead of only raw text.

The debug mode is especially strong for developer workflows.

Remaining limits
It still produces text prompts, not a full chain-of-thought planning graph or agent workflow.

It does not yet score prompt quality automatically.

It does not include prompt compression, adversarial constraint checks, or domain-specific tool routing.

How to push it closer to real God Mode
Phase 3 upgrades
Add a critic pass that reviews the generated prompt for ambiguity, contradiction, verbosity, and missing constraints.

Add a refiner pass that rewrites the prompt after criticism.

Add domain packs, for example coding, research, product, legal, education, each with specialized methods and output schemas.

Add a scoring system such as:

specificity score

constraint clarity score

output-shape score

execution readiness score

Add an export mode that returns JSON for direct use in a frontend or API.

Add prompt memory so repeated requests can inherit style and structure from prior successful outputs.

Why this version is meaningfully better
This version stops pretending that stronger adjectives create stronger prompts. Instead, it improves the actual mechanics: validation, task decomposition, explicit frameworks, adaptive depth, and structured outputs.

Suggested next build
The next serious step is PerplexityGodMode v3: a multi-pass system with generator, critic, refiner, and scorer classes. That would move it from “high-quality prompt builder” to a true prompt-engineering subsystem.


Open perplexity_god_mode_v2_review
I rebuilt it into a much stronger v2 that is actually closer to a production prompt-engineering engine than a themed template generator. The rewrite adds typed task modes, explicit complexity behavior, validation, prompt variants, structured metadata, and a cleaner architecture that fixes the original weak points instead of just rewording them.

What changed
The new version replaces the original “big persona string plus template” pattern with dataclasses, enums, framework maps, and a generate() method that returns a full artifact: prompt, rationale, variants, and diagnostics . It also expands beyond analysis, creative, and technical by adding strategy and debug, which makes it far more useful for real engineering and decision workflows .

Review of v2
This is a real improvement because complexity now changes behavior in a meaningful way, input validation is explicit, and the output is easier to integrate into an app or API pipeline. The biggest remaining limitation is that it is still single-pass generation; true “God Mode” would need generator, critic, refiner, and scorer passes so the system can attack its own weaknesses before returning a result.

What I built
I created:

A rewritten Python implementation of PerplexityGodMode v2 .

A separate review document explaining what was fixed, what still limits it, and what v3 should add next.

Best next evolution
To reach the level you’re asking for, the next version should become a multi-pass prompt engine with:

A generator pass.

A critic pass for ambiguity and contradiction detection.

A refiner pass.

A scoring pass for specificity, execution readiness, and clarity.

That would be the point where it starts feeling like actual God Mode rather than “better prompt templates”. Would you like me to build the v3 version now as a full multi-pass engine?

Are there any gitignore best practices for this setup

Yes — for this setup, the main .gitignore goal is to keep generated eval outputs, local secrets, Python caches, and machine-specific files out of the repo, while still committing the source-of-truth files like the engine, datasets, and workflows.

What to commit
You should usually commit:

The prompt engine source.

The eval runner.

The golden datasets.

The GitHub Actions workflows.

Dependency manifests like pyproject.toml or requirements.txt.

Those are the reproducible inputs to your system, so they belong in version control.

What to ignore
You should usually ignore:

Python caches like __pycache__/, .pytest_cache/, .mypy_cache/, .ruff_cache/.

Virtual environments like .venv/, venv/, env/.

Local secrets such as .env, .env.*, *.pem, *.key.

Generated eval outputs like JSON/CSV reports if they are CI artifacts rather than canonical fixtures.

IDE and OS noise like .vscode/, .idea/, .DS_Store, Thumbs.db.

Best practice for your repo
For your prompt-eval setup, I would commit prompt_golden_dataset.json because it is a test fixture, but ignore output/eval_results/ because that directory contains run artifacts, not source inputs. I would also ignore any local experiment folders, scratch notebooks, and temporary prompt result dumps unless they are curated benchmark assets.

Good starting .gitignore
A solid starting point for your repo would include patterns like:

text
# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
.coverage.*
htmlcov/

# Virtual environments
.venv/
venv/
env/
ENV/

# Build/package artifacts
build/
dist/
*.egg-info/

# Local secrets
.env
.env.*
*.pem
*.key

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/

# Generated eval artifacts
output/eval_results/
*.log
Those patterns align with common Python project guidance and artifact-handling practices for CI workflows.

Two easy mistakes
First, don’t ignore your golden datasets by accident; benchmark fixtures are part of the codebase and should stay tracked. Second, if a secret or generated artifact is already tracked, adding it to .gitignore will not remove it from Git history by itself, so you need to untrack it explicitly and rotate secrets if they were exposed.

If you want, I can generate a repo-specific .gitignore for your exact folder structure and share it as a file.

lets make the .readme.md
Completed 2 steps
README
Perplexity God Mode Prompt Engine
A modular prompt-engineering system for generating, critiquing, refining, and evaluating prompts with routing, benchmark datasets, and CI-ready regression checks.

What this repo contains
perplexity_god_mode_v4.py — the current prompt engine.

prompt_eval_runner.py — the CI-ready evaluation runner.

prompt_golden_dataset.json — the initial golden benchmark dataset.

eval_results/ — generated evaluation outputs such as JSON and CSV reports.

.github/workflows/prompt-eval.yml — GitHub Actions workflow for smoke-suite evals.

Core architecture
The engine is designed as a multi-pass system rather than a single prompt template.

Main components:

DomainPackRegistry — chooses a domain pack such as coding, research, product, or documentation.

PromptMemory — recalls reusable prompt patterns when enabled.

SchemaBuilder — adds strict JSON schema instructions when required.

PromptGenerator — builds the first draft prompt.

ConstraintInspector — checks for contradictions and ambiguities.

PromptCritic — scores the draft.

PromptRefiner — rewrites the prompt based on critique results.

PromptVariantBuilder — creates specialized variants.

PromptTestHarness — runs fixture-style checks.

GodModeEngineV4 — orchestrates the pipeline.

Benchmarking strategy
The benchmark harness is used to treat prompt quality like software quality.

The golden dataset should include:

representative task types,

routing edge cases,

formatting-sensitive requests,

contradiction cases,

known historical failures.

Current benchmark checks include:

domain-pack routing accuracy,

required structure presence,

execution-hook coverage,

score thresholds,

JSON/CSV artifact generation.

Local usage
Run the engine directly:

bash
python perplexity_god_mode_v4.py
Run the eval runner against the dataset:

bash
python prompt_eval_runner.py \
  --engine perplexity_god_mode_v4.py \
  --dataset prompt_golden_dataset.json \
  --outdir eval_results
Run only the smoke suite:

bash
python prompt_eval_runner.py --smoke-only
Limit the number of dataset cases:

bash
python prompt_eval_runner.py --dataset-limit 10
CI integration
A GitHub Actions workflow can run the smoke suite on pull requests and pushes that affect the engine, eval runner, or benchmark dataset.

Example workflow path:

text
.github/workflows/prompt-eval.yml
Typical smoke-suite command:

bash
python output/prompt_eval_runner.py --smoke-only --min-pass-rate 1.0 --min-pack-match-rate 1.0
Recommended CI policy:

Run smoke suite on every PR.

Run a broader regression suite on merges or nightly schedules.

Upload JSON and CSV outputs as CI artifacts.

Fail the build on routing or threshold regressions.

Suggested repo layout
text
.
├── perplexity_god_mode_v4.py
├── prompt_eval_runner.py
├── prompt_golden_dataset.json
├── eval_results/
├── .github/
│   └── workflows/
│       └── prompt-eval.yml
└── README.md
For a larger codebase, consider moving files into structured folders such as:

text
prompt_engine/
evals/datasets/
evals/results/
.github/workflows/
Git ignore guidance
Commit source-of-truth files such as:

engine code,

datasets,

workflows,

dependency manifests.

Ignore generated or local-only files such as:

__pycache__/

.venv/

.env

eval_results/

IDE settings

temporary logs and scratch outputs

Example:

text
__pycache__/
.venv/
.env
output/eval_results/
*.log
.vscode/
.idea/
How to expand the benchmark
Add real failure cases from development or production.

Add routing tie-breaker cases across similar domains.

Add strict-format cases for JSON or documentation output.

Add contradiction-heavy prompts.

Track pass rates and score deltas over time.

A practical growth path:

5 cases for bootstrapping,

20–30 cases for smoke coverage,

50–100 cases for broader regression checks.

Next improvements
High-value future work:

domain-pack weighting improvements,

stronger creative-task validation rules,

externalized memory,

benchmark versioning,

nightly full-suite CI,

answer-quality judging in addition to prompt-shape checks.


Open README
I created a README that documents the prompt engine, eval runner, benchmark dataset, repo structure, CI usage, and .gitignore guidance . It’s set up as a practical project README, so you can drop it into the repo and refine paths if you move files out of output/ later .

What’s in it
The README covers the engine architecture, local commands, benchmark strategy, CI workflow expectations, suggested repo layout, and benchmark expansion plan . It also includes a small .gitignore example and explains which files should be committed versus treated as generated artifacts .

One thing to adjust
Right now the examples assume the current file layout you’ve been using during development, so if you reorganize into folders like prompt_engine/ and evals/, you should update the command paths to match . That is normal and easy to clean up once you settle on the final repo structure .

I need copies of the final files for this
Completed 3 steps




README
Document

final_bundle.tar.gz
Generated File

perplexity_god_mode_v4.py
Python

prompt_eval_runner.py
Python

prompt_golden_dataset.json
JSON

.github_workflow_prompt_eval.yml
YAML
README
Perplexity God Mode Prompt Engine
A modular prompt-engineering system for generating, critiquing, refining, and evaluating prompts with routing, benchmark datasets, and CI-ready regression checks.

What this repo contains
perplexity_god_mode_v4.py — the current prompt engine.

prompt_eval_runner.py — the CI-ready evaluation runner.

prompt_golden_dataset.json — the initial golden benchmark dataset.

eval_results/ — generated evaluation outputs such as JSON and CSV reports.

.github/workflows/prompt-eval.yml — GitHub Actions workflow for smoke-suite evals.

Core architecture
The engine is designed as a multi-pass system rather than a single prompt template.

Main components:

DomainPackRegistry — chooses a domain pack such as coding, research, product, or documentation.

PromptMemory — recalls reusable prompt patterns when enabled.

SchemaBuilder — adds strict JSON schema instructions when required.

PromptGenerator — builds the first draft prompt.

ConstraintInspector — checks for contradictions and ambiguities.

PromptCritic — scores the draft.

PromptRefiner — rewrites the prompt based on critique results.

PromptVariantBuilder — creates specialized variants.

PromptTestHarness — runs fixture-style checks.

GodModeEngineV4 — orchestrates the pipeline.

Benchmarking strategy
The benchmark harness is used to treat prompt quality like software quality.

The golden dataset should include:

representative task types,

routing edge cases,

formatting-sensitive requests,

contradiction cases,

known historical failures.

Current benchmark checks include:

domain-pack routing accuracy,

required structure presence,

execution-hook coverage,

score thresholds,

JSON/CSV artifact generation.

Local usage
Run the engine directly:

bash
python perplexity_god_mode_v4.py
Run the eval runner against the dataset:

bash
python prompt_eval_runner.py \
  --engine perplexity_god_mode_v4.py \
  --dataset prompt_golden_dataset.json \
  --outdir eval_results
Run only the smoke suite:

bash
python prompt_eval_runner.py --smoke-only
Limit the number of dataset cases:

bash
python prompt_eval_runner.py --dataset-limit 10
CI integration
A GitHub Actions workflow can run the smoke suite on pull requests and pushes that affect the engine, eval runner, or benchmark dataset.

Example workflow path:

text
.github/workflows/prompt-eval.yml
Typical smoke-suite command:

bash
python output/prompt_eval_runner.py --smoke-only --min-pass-rate 1.0 --min-pack-match-rate 1.0
Recommended CI policy:

Run smoke suite on every PR.

Run a broader regression suite on merges or nightly schedules.

Upload JSON and CSV outputs as CI artifacts.

Fail the build on routing or threshold regressions.

Suggested repo layout
text
.
├── perplexity_god_mode_v4.py
├── prompt_eval_runner.py
├── prompt_golden_dataset.json
├── eval_results/
├── .github/
│   └── workflows/
│       └── prompt-eval.yml
└── README.md
For a larger codebase, consider moving files into structured folders such as:

text
prompt_engine/
evals/datasets/
evals/results/
.github/workflows/
Git ignore guidance
Commit source-of-truth files such as:

engine code,

datasets,

workflows,

dependency manifests.

Ignore generated or local-only files such as:

__pycache__/

.venv/

.env

eval_results/

IDE settings

temporary logs and scratch outputs

Example:

text
__pycache__/
.venv/
.env
output/eval_results/
*.log
.vscode/
.idea/
How to expand the benchmark
Add real failure cases from development or production.

Add routing tie-breaker cases across similar domains.

Add strict-format cases for JSON or documentation output.

Add contradiction-heavy prompts.

Track pass rates and score deltas over time.

A practical growth path:

5 cases for bootstrapping,

20–30 cases for smoke coverage,

50–100 cases for broader regression checks.

Next improvements
High-value future work:

domain-pack weighting improvements,

stronger creative-task validation rules,

externalized memory,

benchmark versioning,

nightly full-suite CI,

answer-quality judging in addition to prompt-shape checks.


Open README
I packaged the final set and shared both the archive and the individual files so you can drop them into a repo directly.

Included files
The bundle contains:

The final v4 prompt engine

The CI-ready eval runner

The golden benchmark dataset

The project README

The GitHub Actions workflow file

Packaging note
I also included a single archive containing the whole set for convenience, which is useful if you want to download everything in one shot and unpack it locally . The workflow file is included as a standalone file too, so you can move it into .github/workflows/prompt-eval.yml in your repo structure.

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, List, Tuple, Any
import json
import re
import textwrap


class TaskType(str, Enum):
    ANALYSIS = "analysis"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    STRATEGY = "strategy"
    DEBUG = "debug"
    RESEARCH = "research"
    WRITING = "writing"


class Complexity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    EXTREME = "extreme"


@dataclass
class PromptRequest:
    goal: str
    task_type: TaskType
    domain: str = "general"
    complexity: Complexity = Complexity.HIGH
    audience: str = "advanced practitioner"
    constraints: List[str] = field(default_factory=list)
    output_format: str = "markdown"
    examples: List[str] = field(default_factory=list)
    required_sections: List[str] = field(default_factory=list)
    preferred_style: List[str] = field(default_factory=list)
    banned_phrases: List[str] = field(default_factory=lambda: [
        "perfect",
        "genius",
        "revolutionary",
        "god mode",
        "world-class",
    ])
    enable_memory: bool = True
    strict_json_schema: bool = False


@dataclass
class PromptDraft:
    content: str
    metadata: Dict[str, Any]


@dataclass
class CritiqueReport:
    findings: List[str]
    scores: Dict[str, int]
    pass_fail: Dict[str, bool]
    contradictions: List[str]
    ambiguities: List[str]


@dataclass
class TestCase:
    name: str
    request: PromptRequest
    expected_signals: List[str]


@dataclass
class FinalArtifact:
    request: Dict[str, Any]
    draft: str
    critique: Dict[str, Any]
    refined_prompt: str
    variants: Dict[str, str]
    scores: Dict[str, int]
    memory_hits: List[str]
    selected_domain_pack: str
    schema: Dict[str, Any]
    test_results: List[Dict[str, Any]]
    release_notes: List[str]


class DomainPackRegistry:
    def __init__(self) -> None:
        self.packs = {
            "coding": {
                "keywords": ["code", "python", "debug", "api", "fastapi", "react", "backend", "frontend"],
                "constraints": [
                    "Prefer concrete implementation details over abstract guidance.",
                    "Include failure modes, tests, and validation steps.",
                ],
                "sections": ["Context", "Architecture", "Implementation", "Validation", "Risks"],
            },
            "research": {
                "keywords": ["research", "evidence", "sources", "study", "compare", "literature"],
                "constraints": [
                    "Differentiate evidence from inference.",
                    "Note uncertainty, gaps, and competing interpretations.",
                ],
                "sections": ["Question", "Evidence", "Assessment", "Gaps", "Implications"],
            },
            "product": {
                "keywords": ["roadmap", "product", "feature", "user", "market", "strategy"],
                "constraints": [
                    "Tie recommendations to user outcomes and prioritization.",
                    "State tradeoffs and sequencing explicitly.",
                ],
                "sections": ["Objective", "User Impact", "Options", "Priorities", "Execution", "Risks"],
            },
            "writing": {
                "keywords": ["write", "article", "essay", "copy", "documentation", "blog"],
                "constraints": [
                    "Optimize for clarity, voice consistency, and structure.",
                    "Avoid repetition and empty transitions.",
                ],
                "sections": ["Audience", "Message", "Structure", "Draft", "Revision Notes"],
            },
            "documentation": {
                "keywords": ["documentation", "docs", "onboarding", "readme", "developer guide", "api docs"],
                "constraints": [
                    "Prefer structural clarity, setup guidance, validation, and common failure cases.",
                    "Avoid marketing language and keep instructions actionable.",
                ],
                "sections": ["Audience", "Purpose", "Setup", "Usage", "Validation", "Risks", "Common Failures", "Next Steps"],
            },
            "operations": {
                "keywords": ["process", "ops", "workflow", "system", "runbook", "incident"],
                "constraints": [
                    "Prioritize reliability, repeatability, and operator clarity.",
                    "End with a checklist or runbook format when appropriate.",
                ],
                "sections": ["Situation", "Constraints", "Procedure", "Escalation", "Checklist"],
            },
        }

    def select(self, request: PromptRequest) -> Tuple[str, Dict[str, Any]]:
        haystack = " ".join([
            request.goal.lower(),
            request.domain.lower(),
            request.task_type.value.lower(),
            " ".join(c.lower() for c in request.constraints),
        ])
        best_name = "general"
        best_score = 0
        best_pack: Dict[str, Any] = {"constraints": [], "sections": []}
        for name, pack in self.packs.items():
            score = sum(1 for kw in pack["keywords"] if kw in haystack)
            if name == "documentation":
                score += sum(1 for token in ["readme", "docs", "onboarding", "guide", "documentation"] if token in haystack)
            if name == "writing":
                score += sum(1 for token in ["write", "article", "essay", "copy", "blog"] if token in haystack)
            if score > best_score or (score == best_score and name == "documentation"):
                best_name = name
                best_score = score
                best_pack = pack
        if any(token in haystack for token in ["documentation", "docs", "readme", "onboarding", "api docs", "developer guide"]):
            best_name = "documentation"
            best_pack = self.packs["documentation"]
        elif request.task_type == TaskType.CREATIVE:
            best_name = "general"
            best_pack = {"constraints": [], "sections": []}
        return best_name, best_pack


class PromptMemory:
    def __init__(self) -> None:
        self.patterns = {
            "debug": [
                "Prefer root-cause isolation before recommending major redesigns.",
                "Ask for reproducible steps, logs, and environment details.",
            ],
            "technical": [
                "Use layered explanation: overview, internals, implementation.",
            ],
            "research": [
                "Separate established evidence from open questions.",
            ],
            "coding": [
                "Include test strategy, edge cases, and failure handling.",
            ],
        }

    def recall(self, request: PromptRequest, pack_name: str) -> List[str]:
        hits = []
        if request.task_type.value in self.patterns:
            hits.extend(self.patterns[request.task_type.value])
        if pack_name in self.patterns:
            hits.extend(self.patterns[pack_name])
        return list(dict.fromkeys(hits))


class SchemaBuilder:
    def build(self, request: PromptRequest) -> Dict[str, Any]:
        base_schema = {
            "type": "object",
            "properties": {
                "context": {"type": "string"},
                "assumptions": {"type": "array", "items": {"type": "string"}},
                "response": {"type": "array", "items": {"type": "string"}},
                "risks": {"type": "array", "items": {"type": "string"}},
                "next_actions": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["context", "response", "next_actions"],
        }
        if request.strict_json_schema:
            return base_schema
        return {}


class PromptGenerator:
    def __init__(self) -> None:
        self.roles = {
            TaskType.ANALYSIS: "senior analyst and decision advisor",
            TaskType.CREATIVE: "creative director and concept strategist",
            TaskType.TECHNICAL: "staff-level engineer and technical explainer",
            TaskType.STRATEGY: "product strategist and systems thinker",
            TaskType.DEBUG: "principal engineer focused on debugging and root-cause analysis",
            TaskType.RESEARCH: "research lead focused on evidence quality and synthesis",
            TaskType.WRITING: "expert writer and developmental editor",
        }

        self.methods = {
            TaskType.ANALYSIS: [
                "Clarify the objective, assumptions, and decision context",
                "Compare options, tradeoffs, and likely outcomes",
                "Recommend the strongest path with reasoning",
            ],
            TaskType.CREATIVE: [
                "Generate distinct directions rather than shallow variants",
                "Use analogy, inversion, and constraint-based ideation",
                "Stress-test for originality, usefulness, and audience fit",
            ],
            TaskType.TECHNICAL: [
                "Define the system or concept clearly",
                "Break it into architecture, logic, and implementation layers",
                "Call out failure modes, edge cases, and validation",
            ],
            TaskType.STRATEGY: [
                "Define the objective and constraints",
                "Map leverage points, dependencies, and second-order effects",
                "Produce a prioritized execution plan",
            ],
            TaskType.DEBUG: [
                "Restate the issue precisely from symptoms and observable behavior",
                "Prioritize likely root causes",
                "Design a minimal isolation plan before proposing fixes",
            ],
            TaskType.RESEARCH: [
                "Define the research question and scope",
                "Assess evidence quality, uncertainty, and disagreements",
                "Synthesize findings, gaps, and implications",
            ],
            TaskType.WRITING: [
                "Clarify audience, purpose, and message",
                "Shape the structure before drafting",
                "Revise for clarity, flow, and precision",
            ],
        }

        self.complexity_rules = {
