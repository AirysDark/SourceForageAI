#!/usr/bin/env python3

import sys
from pathlib import Path

from ai_config import MAX_ATTEMPTS, BUILD_CMD, BUSYBOX_HINT
from ai_repo import get_repo_tree, get_recent_diff, tail_build_log
from ai_build import run_build
from ai_llm import call_llm
from ai_patch import extract_unified_diff, apply_patch

# build intelligence
from build.detect import detect_build_type
from build.knowledge import record
from build.websearch import search_build_fix

# universal build detection
from build.universal_engine import detect_build_system

# repository intelligence scanner
from build.repo_intelligence import predict_build

# self-training memory
from ai_memory.memory import store_failure, store_fix, search_memory

# successful build reference memory
from ai_memory.success_memory import store_success, search_success


PROJECT_ROOT = Path(".")


PROMPT = """
You are an automated build fixer working in a Git repository.

Goal:
Fix build failures by editing files.

Detected build system:
{build_type}

Repository files:
{repo_tree}

Recent git diff:
{recent_diff}

Build command:
{build_cmd}

Build log:
{build_tail}

Project notes:
{project_hint}

Web hint (if available):
{web_hint}

Rules:
- Return ONLY a unified diff
- Start with --- and +++
- Minimal safe edits
- Prefer fixing configuration or build scripts
"""


# ---------------------------------------------------
# Extract useful error from build log
# ---------------------------------------------------

def extract_first_error(log):

    if not log:
        return ""

    lines = log.split("\n")

    for line in reversed(lines):

        l = line.lower()

        if "error" in l or "failed" in l:
            return line.strip()

    return lines[-1].strip() if lines else ""


# ---------------------------------------------------
# Determine build system
# ---------------------------------------------------

def resolve_build_system():

    try:

        system = detect_build_system(PROJECT_ROOT)

        if system:
            return system

    except Exception:
        pass

    try:
        return detect_build_type(PROJECT_ROOT)
    except Exception:
        return "unknown"


# ---------------------------------------------------
# Determine build command
# ---------------------------------------------------

def resolve_build_command():

    try:

        predicted = predict_build()

        if predicted:

            print(f"Predicted build command: {predicted}")

            return predicted

    except Exception:
        pass

    return BUILD_CMD


# ---------------------------------------------------
# Attempt to reuse successful build references
# ---------------------------------------------------

def try_success_memory():

    try:

        repo_tree = get_repo_tree()

        success = search_success(repo_tree)

        if success:

            print("Found successful build reference")

            cmd = success.get("build_command")

            if cmd:
                print(f"Using stored command: {cmd}")
                return cmd

    except Exception:
        pass

    return None


# ---------------------------------------------------
# AI repair loop
# ---------------------------------------------------

def main():

    print("== AI Autobuilder ==")

    repo_tree = get_repo_tree()

    # ------------------------------------------------
    # Detect build system
    # ------------------------------------------------

    build_type = resolve_build_system()

    print(f"Detected build system: {build_type}")

    # ------------------------------------------------
    # Try success memory
    # ------------------------------------------------

    build_cmd = try_success_memory()

    # ------------------------------------------------
    # Predict command if memory not found
    # ------------------------------------------------

    if not build_cmd:

        build_cmd = resolve_build_command()

    print(f"Using build command: {build_cmd}")

    # ------------------------------------------------
    # First build attempt
    # ------------------------------------------------

    code = run_build(build_cmd)

    log_tail = tail_build_log()

    try:
        record(build_type, code == 0, log_tail)
    except Exception:
        pass

    # ------------------------------------------------
    # If build already works
    # ------------------------------------------------

    if code == 0:

        print("Build already works.")

        try:

            store_success(
                repo_tree,
                build_cmd,
                build_type,
                log_tail
            )

        except Exception:
            pass

        return 0

    # ------------------------------------------------
    # Store failure for training
    # ------------------------------------------------

    try:
        store_failure(build_type, log_tail)
    except Exception:
        pass

    attempts = 0

    # ------------------------------------------------
    # AI Fix Attempts
    # ------------------------------------------------

    while attempts < MAX_ATTEMPTS:

        attempts += 1

        print(f"\nAttempt {attempts}/{MAX_ATTEMPTS}")

        log_tail = tail_build_log()

        diff = None

        # ------------------------------------------------
        # Try memory fixes first
        # ------------------------------------------------

        try:
            mem_patch = search_memory(log_tail)
        except Exception:
            mem_patch = None

        if mem_patch:

            print("Found matching fix in local memory.")

            diff = mem_patch

        else:

            web_hint = ""

            # --------------------------------------------
            # Web hint search
            # --------------------------------------------

            try:

                err = extract_first_error(log_tail)

                if err:

                    print("Searching web for hint...")

                    web_hint = search_build_fix(err)

            except Exception:
                pass

            # --------------------------------------------
            # Build AI prompt
            # --------------------------------------------

            prompt = PROMPT.format(
                build_type=build_type,
                repo_tree=repo_tree,
                recent_diff=get_recent_diff(),
                build_cmd=build_cmd,
                build_tail=log_tail,
                project_hint=BUSYBOX_HINT if build_type == "busybox" else "",
                web_hint=web_hint
            )

            # --------------------------------------------
            # Call AI model
            # --------------------------------------------

            try:

                llm_out = call_llm(prompt)

            except Exception as e:

                print("AI call failed:", e)

                break

            if not llm_out:

                print("AI returned empty response")

                break

            diff = extract_unified_diff(llm_out)

        # ------------------------------------------------
        # Validate patch
        # ------------------------------------------------

        if not diff:

            print("No valid patch returned.")

            break

        print("\nPatch preview:\n")

        print(diff[:1500])

        # ------------------------------------------------
        # Apply patch
        # ------------------------------------------------

        if not apply_patch(diff):

            print("Patch failed to apply.")

            break

        # ------------------------------------------------
        # Save patch
        # ------------------------------------------------

        try:
            store_fix(diff)
        except Exception:
            pass

        # ------------------------------------------------
        # Rebuild
        # ------------------------------------------------

        code = run_build(build_cmd)

        log_tail = tail_build_log()

        try:
            record(build_type, code == 0, log_tail)
        except Exception:
            pass

        # ------------------------------------------------
        # If build fixed
        # ------------------------------------------------

        if code == 0:

            print("Build fixed!")

            try:

                store_success(
                    repo_tree,
                    build_cmd,
                    build_type,
                    log_tail
                )

            except Exception:
                pass

            return 0

    print("Still failing.")

    return 1


if __name__ == "__main__":

    sys.exit(main())