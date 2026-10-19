# Python benchmark HTML reporting

Python is the analysis/presentation layer, not the native measurement harness. Reuse the project's Python environment and dependency policy; add packages only when justified. Start with standard-library JSON/CSV processing and simple escaped HTML; use an existing template/chart library where it improves maintainability.

## Input and analysis

- Preserve original runner outputs. Define a documented normalized format with scenario identity, units, workload parameters, artifact/configuration, instrumentation, sample/trial identity, summaries, and result/failure status.
- Validate required fields, units, finite numbers, identities, and comparison compatibility. Reject malformed input explicitly; show missing or failed measurements rather than replacing them with zero or silently dropping them.
- Keep runner-specific adapters small. Do not treat unlike sample formats as interchangeable or recalculate uncertainty without an appropriate supported method.
- State formulas and metric direction. Do not divide by zero or infer per-request percentiles from aggregate data.
- Keep units consistent in tables/charts and label any conversions. Make generation deterministic for the same input except explicitly recorded report metadata.

## HTML presentation

- Prefer offline, self-contained HTML with embedded/local chart assets and no CDN, analytics, or remote uploads.
- Escape all data rendered into HTML; enable template autoescaping when using Jinja2. Embed JSON with context-appropriate safe encoding, not raw string interpolation into script tags.
- Prefer static tables and charts unless interaction materially helps. Do not add Jinja2, Matplotlib, and Plotly together by default; choose the smallest adequate existing solution.
- Include the measurement question, scenario definitions, baseline/candidate identity, commands, environment, real dependencies, run counts, uncertainty, and known limitations.
- Provide readable tables: scenario, metric/unit, baseline, candidate, relative change, variation/uncertainty, and conclusion.
- Display failed, skipped, missing, incomparable, and inconclusive scenarios explicitly. Do not communicate outcomes through color alone.
- Accompany the report with raw artifacts or safe relative links. Redact credentials, sensitive command arguments, paths, and payloads; avoid rendering untrusted active content.

## Verification

- Test parsing/conversion/comparison with known fixtures, including missing values, incompatible units/configurations, zero baselines, and hostile HTML strings.
- Generate the report from a real small run and verify its numbers against raw inputs. Validate that all expected scenarios are represented and errors remain visible.
- Check the report renders offline using available local tools; visually inspect where feasible. Report if rendering was not checked.
- Write artifacts to explicit project-owned output paths, preserving prior results unless replacement is intended. Do not generate invented measurements merely to fill a chart.
