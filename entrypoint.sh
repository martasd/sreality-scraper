#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

flask db upgrade

flask seed_db

flask run --host=0.0.0.0 --port=8080
