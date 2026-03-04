def analyze(log):

    if "Python.h" in log:
        return {
            "type":"missing_dependency",
            "package":"python-dev"
        }

    if "ModuleNotFoundError" in log:
        return {
            "type":"missing_python_package"
        }