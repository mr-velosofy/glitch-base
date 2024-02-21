set -eux
. /tmp/venv/bin/activate
flask --app myapp run --port $PORT --debug
