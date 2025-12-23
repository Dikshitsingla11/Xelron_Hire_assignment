#!/bin/bash

set -e

echo "Running JSON Log Processor Tests..."
echo "=================================="

python3 /workspace/tests/test_outputs.py

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "=================================="
    echo "All tests passed!"
else
    echo "=================================="
    echo "Tests failed!"
fi

exit $exit_code

