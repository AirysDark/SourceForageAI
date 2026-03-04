from .db import get_db


def predict_command(features):

    db = get_db()

    candidates = {}

    for lang in features["languages"]:

        rows = db.execute(
            """
            SELECT command, success_count
            FROM knowledge
            WHERE language=?
            """,
            (lang,)
        ).fetchall()

        for cmd, score in rows:

            candidates[cmd] = candidates.get(cmd, 0) + score


    for bf in features["build_files"]:

        rows = db.execute(
            """
            SELECT command, success_count
            FROM knowledge
            WHERE build_file=?
            """,
            (bf,)
        ).fetchall()

        for cmd, score in rows:

            candidates[cmd] = candidates.get(cmd, 0) + score


    if not candidates:
        return None


    best = sorted(
        candidates.items(),
        key=lambda x: x[1],
        reverse=True
    )[0]

    return best[0]