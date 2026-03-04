
def generate_router(root, report):

    router = root / "core/router.py"

    if router.exists():
        return

    router.parent.mkdir(parents=True, exist_ok=True)

    router.write_text(
"""
from core.Cerebrum import Cerebrum
from core.Cerebellum import Cerebellum
from core.Brainstem import Brainstem

class BrainRouter:

    def __init__(self):
        self.cerebrum = Cerebrum()
        self.cerebellum = Cerebellum()
        self.brainstem = Brainstem()

    def route(self, task):

        if task.get("type") == "analysis":
            return self.cerebrum.process(task)

        if task.get("type") == "execution":
            return self.cerebellum.process(task)

        return self.brainstem.process(task)
"""
    )

    report.append("Generated core/router.py")
