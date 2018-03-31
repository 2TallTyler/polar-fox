import shutil
import os
currentdir = os.curdir

import codecs
import global_constants

dist_container_path = global_constants.dist_container_path
dist_package_path = global_constants.dist_package_path

def main():
    print("Preparing files for distribution")
    if os.path.exists(dist_container_path):
        print("Cleaning: removing", dist_container_path)
        shutil.rmtree(dist_container_path)
    os.mkdir(dist_container_path)
    if os.path.exists(dist_package_path):
        print("Cleaning: removing", dist_package_path)
        shutil.rmtree(dist_package_path)
    os.mkdir(dist_package_path)

    dist_file_header = codecs.open(os.path.join(currentdir, 'src', 'dist_file_header.txt'), 'r','utf8').read()
    for filename in ['__init__.py', 'constants.py', 'graphics_units.py', 'pixa.py']:
        src_file = codecs.open(os.path.join(currentdir, 'src', filename), 'r','utf8')
        dist_file = codecs.open(os.path.join(dist_package_path, filename), 'w','utf8')
        dist_file.write(dist_file_header)
        dist_file.write(src_file.read())
        dist_file.close()
    for dir_name in ['cargo_graphics']:
        dist_dir_path =  os.path.join(dist_package_path, dir_name)
        shutil.copytree(os.path.join(currentdir, 'generated', dir_name), dist_dir_path)
        shutil.copy(os.path.join(currentdir, 'src', 'dist_dir_header.txt'), os.path.join(dist_dir_path, '_files_here_are_generated.txt'))
    print("[DONE]")

if __name__ == '__main__':
    main()