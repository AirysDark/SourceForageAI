
def analyze_symbols(definitions, references, report, json_data):

    for file, calls in references.items():

        defs = definitions.get(file, [])

        for name in calls:

            if name not in defs and not name.startswith("_"):

                report.append(f"Undefined symbol {name} in {file}")
                json_data["undefined_symbols"].append(name)
