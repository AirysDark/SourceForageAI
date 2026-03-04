import subprocess
import shutil
import json


def _check_ollama():

    """Verify ollama binary exists"""

    if not shutil.which("ollama"):
        raise RuntimeError("Ollama is not installed or not in PATH")


def _model_exists(model):

    """Check if model is installed"""

    try:
        out = subprocess.check_output(
            ["ollama", "list"],
            text=True
        )

        return model in out

    except Exception:
        return False


def call_local_model(
    prompt,
    model="deepseek-coder",
    timeout=300,
    max_chars=20000
):

    """
    Call a local Ollama model and return response text.
    """

    if not prompt:
        return ""

    _check_ollama()

    if not _model_exists(model):

        print(f"Model '{model}' not installed")
        return ""

    # prevent huge prompts
    if len(prompt) > max_chars:
        prompt = prompt[:max_chars]

    try:

        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if proc.returncode != 0:

            print("Local model error:")
            print(proc.stderr.strip())

            return ""

        output = proc.stdout.strip()

        if not output:
            print("Model returned empty response")

        return output

    except subprocess.TimeoutExpired:

        print("Local model timeout")

        return ""

    except Exception as e:

        print("Local model failed:", str(e))

        return ""