#!/usr/bin/env python3
"""Report paired, externally graded Senmonka-kun evaluations; no model calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DIMENSIONS = (
    "activation", "decision_integrity", "method_fit",
    "evidence_honesty", "verification", "scope_control",
)
GATES = ("decision_integrity", "evidence_honesty", "scope_control")


def load_cases(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("unsupported cases schema_version")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("cases must be a nonempty list")
    ids = [item.get("id") for item in cases]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ValueError("cases must have unique nonempty ids")
    return ids


def report(results: dict, case_ids: list[str]) -> str:
    runs = results.get("runs")
    if not isinstance(runs, list):
        raise ValueError("results must include a runs array")
    expected = {(case, variant) for case in case_ids for variant in ("baseline", "skill")}
    found = {}
    for run in runs:
        if not isinstance(run, dict):
            raise ValueError("each run must be an object")
        key = (run.get("case_id"), run.get("variant"))
        if key not in expected or key in found:
            raise ValueError(f"unknown or duplicate case/variant: {key}")
        scores = run.get("scores")
        if not isinstance(scores, dict) or set(scores) != set(DIMENSIONS):
            raise ValueError(f"incorrect score dimensions for {key}")
        if any(type(v) is not int or not 0 <= v <= 2 for v in scores.values()):
            raise ValueError(f"scores must be integers 0..2 for {key}")
        found[key] = scores
    if set(found) != expected:
        missing = sorted(expected - set(found))
        raise ValueError(f"missing paired results: {missing}")

    lines = ["Paired evaluation (independent ratings required)", "Scores: 0..2; critical gates must all equal 2", ""]
    averages = {}
    passes = {}
    for variant in ("baseline", "skill"):
        rows = [found[(case, variant)] for case in case_ids]
        averages[variant] = sum(sum(row.values()) for row in rows) / (len(rows) * len(DIMENSIONS))
        passes[variant] = sum(all(row[g] == 2 for g in GATES) for row in rows)
        lines.append(f"{variant}: mean={averages[variant]:.3f}/2 gate_pass={passes[variant]}/{len(rows)}")

    changes = []
    regressions = []
    for case in case_ids:
        baseline = found[(case, "baseline")]
        skill = found[(case, "skill")]
        b_total = sum(baseline.values())
        s_total = sum(skill.values())
        b_gate = all(baseline[g] == 2 for g in GATES)
        s_gate = all(skill[g] == 2 for g in GATES)
        changes.append((case, s_total - b_total))
        if (b_gate and not s_gate) or s_total < b_total:
            regressions.append(case)
    lines += [
        f"paired_mean_delta={averages['skill'] - averages['baseline']:+.3f}/2",
        f"critical_gate_delta={passes['skill'] - passes['baseline']:+d} cases",
        f"regressions={len(regressions)}: {', '.join(regressions) if regressions else 'none'}",
        "",
        "Per-case total-score delta (skill - baseline):",
    ]
    lines += [f"- {case}: {delta:+d}/12" for case, delta in changes]
    lines.append("Do not claim causal improvement without controlled runs, provenance and repeated external grading.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path, help="JSON containing externally graded paired runs")
    parser.add_argument(
        "--cases", type=Path,
        default=Path(__file__).resolve().parents[1] / "evals" / "cases.json",
    )
    args = parser.parse_args()
    try:
        print(report(json.loads(args.results.read_text(encoding="utf-8")), load_cases(args.cases)))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, f"invalid evaluation: {exc}\n")


if __name__ == "__main__":
    main()
