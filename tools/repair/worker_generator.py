
def generate_worker_pool(root, report):

    worker = root / "workers/worker_pool.py"

    if worker.exists():
        return

    worker.parent.mkdir(parents=True, exist_ok=True)

    worker.write_text(
"""
class WorkerPool:

    def __init__(self):
        self.jobs = []

    def submit(self,job):
        self.jobs.append(job)

    def run(self):

        for j in self.jobs:

            try:
                j()
            except Exception:
                pass
"""
    )

    report.append("Generated workers/worker_pool.py")
