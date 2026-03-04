
def generate_orchestrator(root, report):

    orch = root / "orchestrator/orchestrator.py"

    if orch.exists():
        return

    orch.parent.mkdir(parents=True, exist_ok=True)

    orch.write_text(
"""
class Orchestrator:

    def __init__(self):
        self.modules = []

    def register(self,module):
        self.modules.append(module)

    def run(self):

        for m in self.modules:

            try:
                if hasattr(m,'run'):
                    m.run()
            except Exception:
                pass
"""
    )

    report.append("Generated orchestrator/orchestrator.py")
