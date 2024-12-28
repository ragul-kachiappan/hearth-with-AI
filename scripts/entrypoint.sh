#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


# TODO DB check

# TODO collectstatic
# TODO migrations

exec "$@"