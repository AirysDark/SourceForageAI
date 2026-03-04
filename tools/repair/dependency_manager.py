
import subprocess

def install_dependencies(missing_imports, safe_pip, report):

    for dep in missing_imports:

        if dep not in safe_pip:
            continue

        try:
            subprocess.run(["pip","install",dep])
            report.append(f"Installed dependency {dep}")
        except:
            report.append(f"Failed installing {dep}")
