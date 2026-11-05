import os
import json


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACTIVE_RELEASE_FILE = os.path.join(PROJECT_ROOT, "active_release.json")


def activate_release(version):
    release_path = os.path.join(PROJECT_ROOT, "releases", version)

    if not os.path.isdir(release_path):
        print(f"Release {version} does not exist.")
        return

    release_data = {
        "active_version": version,
        "release_path": release_path
    }

    with open(ACTIVE_RELEASE_FILE, "w") as file:
        json.dump(release_data, file, indent=4)

    print(f"Release {version} activated successfully!")


if __name__ == "__main__":
    activate_release("1.0.2")