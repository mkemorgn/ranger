# Compatible with ranger 1.6.0 through 1.7.*
#
# This plugin adds the sorting algorithm called 'random'.  To enable it, type
# ":set sort=random" or create a key binding with ":map oz set sort=random"

from __future__ import (absolute_import, division, print_function)

from ranger.container.directory import Directory
import secrets

Directory.sort_dict['random'] = lambda path: secrets.SystemRandom().random()
