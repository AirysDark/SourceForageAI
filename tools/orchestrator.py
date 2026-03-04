
def detect_build_system(path):
    return 'unknown'


def clone_repo(url):
    pass

repo = clone_repo()

intel = analyze_repo(repo)

system = detect_build_system(repo)

plan = synthesize(system)

result = execute(plan)

if failed:
    fix = analyze_failure()
    patch = generate_patch()