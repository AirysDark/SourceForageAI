
import json

def write_reports(report_path, json_path, report, json_data):

    report_path.write_text("\n".join(report))
    json_path.write_text(json.dumps(json_data, indent=2))
