# Copyright 2017 Taylor DeHaan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module is the entry point for dir_ascii.

Example:
    In order to run dir_ascii, use this command::

        $ python -m dir_ascii
"""

from .directory_explorer import DirectoryExplorer
from .tree_printer import TreePrinter


def main():
    """Builds a directory tree and then prints it."""
    explorer = DirectoryExplorer()
    tree = explorer.build_tree()
    printer = TreePrinter(tree)
    printer.print_tree()


if __name__ == "__main__":
    main()
