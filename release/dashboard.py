import json
from pathlib import Path

def load(path="data/release.json"):
    return json.loads(Path(path).read_text())

def gates(d):
    return {"critical_defects_clear":d["critical_defects"]==0,
            "requirements_coverage":d["requirements_coverage"]>=0.95,
            "rollback_ready":d["rollback_ready"],
            "deployment_validation_ready":d["deployment_validation_ready"],
            "test_pass_rate":d["tests"]["passed"]/d["tests"]["total"]>=0.95}

def report(d):
    g=gates(d); return {"release":d["release"],"gates":g,"blockers":[k for k,v in g.items() if not v],"decision":"GO" if all(g.values()) else "NO-GO"}

if __name__=="__main__":
    print(json.dumps(report(load()),indent=2))
