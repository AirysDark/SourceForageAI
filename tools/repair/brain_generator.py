
def generate_brain(root, report):

    templates = {
        "core/Cerebrum.py": "class Cerebrum:\n    def process(self,task): return {'status':'analysis','task':task}\n",
        "core/Cerebellum.py": "class Cerebellum:\n    def process(self,task): return {'status':'execution','task':task}\n",
        "core/Brainstem.py": "class Brainstem:\n    def process(self,task): return {'status':'system','task':task}\n"
    }

    for file, code in templates.items():

        path = root / file

        if not path.exists():

            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(code)

            report.append(f"Generated brain component {file}")
