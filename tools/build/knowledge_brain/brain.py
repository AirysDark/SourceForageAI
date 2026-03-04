from .db import get_db


def learn_success(features, command):

    db = get_db()

    for lang in features["languages"]:

        db.execute(
            """
            INSERT INTO knowledge(language, build_file, command, success_count)
            VALUES (?, ?, ?, 1)
            """,
            (lang, "", command)
        )

    for bf in features["build_files"]:

        db.execute(
            """
            INSERT INTO knowledge(language, build_file, command, success_count)
            VALUES (?, ?, ?, 1)
            """,
            ("", bf, command)
        )

    db.commit()