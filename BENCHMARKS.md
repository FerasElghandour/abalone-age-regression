# Reproduction and benchmark scope

The complete retained notebook has been rerun on the real 4,177-row source table through a noninteractive input-aware driver, with source/input hashes, logs and fitted-model export.

## Execute a recorded profile

```sh
python run_reproduction.py --profile checks --output reproduced/checks
```

Use a new output directory for each run. The driver writes command logs, source/input SHA-256 values, versions and an explicit outcome. It does not silently download data or turn generated fixtures into dataset-performance claims.

| Profile | Actual scope | Required inputs |
|---|---|---|
| `checks` | Source parsing only; not model training or behavior verification | None |
| `full-notebook` | Execute retained notebook against an explicitly supplied input; preserves the original experiment protocol | csv |

Supply named paths with `--input name=/absolute/path`. Exact commands are versioned in [reproduction.json](reproduction.json); direct training commands and preparation contracts are below.

## Evidence boundary

The baseline and forest trade-offs remain metric-dependent. The Rings target is not a direct age-in-years measurement.

Keep input acquisition and source credits in [DATA.md](DATA.md). Historical results, new reference runs and small contract fixtures have separate evidential scope.

## Recorded command definitions

### checks

```text
{python} scripts/validate_source.py
```

### full-notebook

```text
{python} reproduce.py --input {input:csv} --output {output}/notebook
```

`{python}` is the current interpreter. `{output}` is the new run directory. `{input:name}` refers to a named absolute input path supplied to the driver. Install declared dependencies in a clean environment before executing. Never execute untrusted serialized models or notebooks.
