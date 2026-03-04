
def generate_scheduler(root, report):

    scheduler = root / "scheduler/scheduler.py"

    if scheduler.exists():
        return

    scheduler.parent.mkdir(parents=True, exist_ok=True)

    scheduler.write_text(
"""
import time

class Scheduler:

    def __init__(self):
        self.tasks = []

    def add(self,fn):
        self.tasks.append(fn)

    def run(self):

        while True:

            for t in self.tasks:
                try:
                    t()
                except Exception:
                    pass

            time.sleep(5)
"""
    )

    report.append("Generated scheduler/scheduler.py")
