import sys
import os

currentdir = os.curdir
import shutil

import git_info


def copy_docs_from_current_project():
    project_name = sys.argv[1]
    tag_name = git_info.get_tag_exact_match()
    print(
        "Copying current docs to grf.farm src dir as",
        "'" + project_name + "/" + tag_name + "'",
    )
    # makes assumption about location of grf.farm relative to projects being "../../"
    common_parent_path = os.path.dirname(os.path.dirname(os.path.abspath(currentdir)))
    grf_farm_path = os.path.join(common_parent_path, "grf.farm", "src", project_name)

    if len(sys.argv) > 2:
        if sys.argv[2] == "--nested-docs-by-grf":
            optional_nested_dir_name = project_name
        else:
            optional_nested_dir_name = ''

    shutil.copytree(
        os.path.join(currentdir, "docs", optional_nested_dir_name), os.path.join(currentdir, tag_name)
    )
    try:
        shutil.move(os.path.join(currentdir, tag_name), grf_farm_path)
    except:
        # clean up local dir if moving failed
        shutil.rmtree(os.path.join(currentdir, tag_name))
        raise


def main():
    # as of July 2021 this module has a single purpose, copying docs from a project to grf.farm location
    copy_docs_from_current_project()


if __name__ == "__main__":
    main()
