import os
import shutil

from src.deployment import record_deployment
from src.git_manager import get_current_commit


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prepare_release(version):
    release_path = os.path.join(PROJECT_ROOT, "releases", version)

    try:
        os.makedirs(release_path, exist_ok=True)

        folders_to_copy = ["src", "tests"]
        files_to_copy = ["requirements.txt"]

        for folder in folders_to_copy:
            source = os.path.join(PROJECT_ROOT, folder)
            destination = os.path.join(release_path, folder)

            if os.path.exists(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)

        for file in files_to_copy:
            source = os.path.join(PROJECT_ROOT, file)

            if os.path.exists(source):
                shutil.copy2(source, release_path)

        print(f"Release {version} prepared successfully!")

        commit_id = get_current_commit()

        record_deployment(
            "DevOps Automation Platform",
            version,
            "SUCCESS"
        )

    except Exception as error:
        print("Deployment preparation failed:", error)

        record_deployment(
            "DevOps Automation Platform",
            version,
            "FAILED"
        )


if __name__ == "__main__":
    prepare_release("1.0.2")