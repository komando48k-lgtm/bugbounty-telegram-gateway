from .db import Finding

def markdown_report(f: Finding) -> str:
    return f"# {f.title}\n\n**Target:** `{f.target}`  \n**Severity:** `{f.severity}`\n\n## Details\n\n{f.details}\n\n## Scope note\n\nThis report is based on information supplied for an authorized bug-bounty target. Validate evidence and program policy before submission.\n"
