
def safe_read(path):
    try:
        return path.read_text()
    except:
        return ""

def write_repair(outdir, path, text):
    repaired = outdir / path.name
    repaired.write_text(text)
    return repaired

def is_ignored(path, ignore_dirs):
    return any(p in ignore_dirs for p in path.parts)
