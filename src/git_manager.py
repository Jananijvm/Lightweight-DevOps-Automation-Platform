import subprocess


def get_current_commit():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError:
        print("Unable to retrieve Git commit.")
        return None


if __name__ == "__main__":
    commit = get_current_commit()

    if commit:
        print("Current Git commit:", commit)