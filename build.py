import argparse
import os
import subprocess

platforms = [
    ("linux", "amd64"),
    ("darwin", "amd64"),
    ("windows", "amd64"),
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auxilary build script.")
    parser.add_argument("-v", "--version", default="unspecified",
                        type=str, help="string used as a version when building binaries")
    args = parser.parse_args()
    version = args.version
    for (build_os, build_arch) in platforms:
        ext = ""
        if build_os == "windows":
            ext = ".exe"
        build_env = os.environ.copy()
        build_env["GOOS"] = build_os
        build_env["GOARCH"] = build_arch
        subprocess.run(["go", "build", "-ldflags", "-X main.version=%s" %
                        version, "-o", "bombardier-%s-%s%s" % (build_os, build_arch, ext)], env=build_env)
