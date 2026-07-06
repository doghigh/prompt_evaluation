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
