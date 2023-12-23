#!/usr/bin/env python3

import subprocess

def RunConan(build_type: str):
    subprocess.run(
        [
            "conan",
            "install",
            ".",
            "--build",
            "missing",
            "--output-folder=./dependencies",
            f"--settings=build_type={build_type}",
        ]
    )

def RunPremake():
    subprocess.run(
        [
            "premake5",
            "gmake2",
        ]
    )


if __name__ == "__main__":
    RunConan("Debug")
    RunConan("Release")

    RunPremake()

