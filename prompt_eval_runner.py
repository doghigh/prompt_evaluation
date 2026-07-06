import argparse
import csv
import importlib.util
import json
import sys
from pathlib import Path

def load_module(path):
    spec = importlib.util.spec_from_file_location('pgm_v4', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    parser = argparse.ArgumentParser(description='Run prompt evaluation benchmarks for GodModeEngineV4')
    parser.add_argument('--engine', default='/home/user/output/perplexity_god_mode_v4.py')
    parser.add_argument('--dataset', default='/home/user/output/prompt_golden_dataset.json')
    parser.add_argument('--outdir', default='/home/user/output/eval_results')
    parser.add_argument('--smoke-only', action='store_true')
        parser.add_argument('--dataset-limit', type=int, default=0, help='Limit number of cases')
    parser.add_argument('--fail-pack-mismatch', action='store_true', default=True)
    parser.add_argument('--min-pass-rate', type=float, default=1.0)
    parser.add_argument('--min-pack-match-rate', type=float, default=1.0)
    args = parser.parse_args()

    engine_mod = load_module(args.engine)
    engine = engine_mod.GodModeEngineV4()
    dataset = json.loads(Path(args.dataset).read_text())
    if args.smoke_only:
        dataset = dataset[:min(5, len(dataset))]

    results = []
    total_tests = 0
    passed_tests = 0
    pack_matches = 0

    for case in dataset:
        req = engine_mod.PromptRequest(
            goal=case['goal'],
            task_type=engine_mod.TaskType(case['task_type']),
            domain=case['domain'],
            complexity=engine_mod.Complexity.EXTREME if case['task_type'] in ['debug', 'research', 'strategy'] else engine_mod.Complexity.HIGH,
            audience=case.get('audience', 'experienced developer'),
            constraints=case.get('constraints', []),
            output_format=case.get('output_format', 'markdown'),
            examples=case.get('examples', []),
            required_sections=case.get('required_sections', []),
            preferred_style=case.get('preferred_style', []),
            enable_memory=case.get('enable_memory', False),
            strict_json_schema=case.get('strict_json_schema', False),
        )
        artifact = engine.run(req)
        test_passed = all(t['passed'] for t in artifact.test_results)
        pack_match = artifact.selected_domain_pack == case['expected_pack']
        total_tests += len(artifact.test_results)
        passed_tests += sum(1 for t in artifact.test_results if t['passed'])
        pack_matches += int(pack_match)
        results.append({
            'id': case['id'],
            'expected_pack': case['expected_pack'],
            'selected_pack': artifact.selected_domain_pack,
            'pack_match': pack_match,
            'all_tests_passed': test_passed,
            'scores': artifact.scores,
            'test_results': artifact.test_results,
            'memory_hits': artifact.memory_hits,
        })

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    json_path = outdir / 'eval_results.json'
    csv_path = outdir / 'eval_results.csv'

    summary = {
        'cases': len(dataset),
        'pack_match_rate': pack_matches / max(1, len(dataset)),
        'test_pass_rate': passed_tests / max(1, total_tests),
        'pack_matches': pack_matches,
        'passed_tests': passed_tests,
        'total_tests': total_tests,
        'results': results,
    }
    json_path.write_text(json.dumps(summary, indent=2))

    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'expected_pack', 'selected_pack', 'pack_match', 'all_tests_passed', 'specificity', 'constraint_clarity', 'output_shape', 'execution_readiness', 'anti_hype'])
        writer.writeheader()
        for r in results:
            row = {
                'id': r['id'],
                'expected_pack': r['expected_pack'],
                'selected_pack': r['selected_pack'],
                'pack_match': r['pack_match'],
                'all_tests_passed': r['all_tests_passed'],
                'specificity': r['scores']['specificity'],
                'constraint_clarity': r['scores']['constraint_clarity'],
                'output_shape': r['scores']['output_shape'],
                'execution_readiness': r['scores']['execution_readiness'],
                'anti_hype': r['scores']['anti_hype'],
            }
            writer.writerow(row)

    failures = []
    if summary['test_pass_rate'] < args.min_pass_rate:
        failures.append(f"test_pass_rate {summary['test_pass_rate']:.2f} < {args.min_pass_rate:.2f}")
    if args.fail_pack_mismatch and summary['pack_match_rate'] < args.min_pack_match_rate:
        failures.append(f"pack_match_rate {summary['pack_match_rate']:.2f} < {args.min_pack_match_rate:.2f}")

    print(json.dumps({'summary': summary, 'json_path': str(json_path), 'csv_path': str(csv_path)}, indent=2))
    if failures:
        print('EVAL FAILURE: ' + '; '.join(failures), file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()



