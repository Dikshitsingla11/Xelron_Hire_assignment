# Add json-log-processor: Filter JSON log entries by ERROR severity level

## Description
This PR adds the JSON Log Processor task that filters log entries by severity level, extracting all entries with level "ERROR".

## Test Results

### Oracle Test (1.0)
```bash
$ docker run --rm -v ${PWD}/harbor_tasks/json-log-processor/solution:/workspace/solution -v ${PWD}/harbor_tasks/json-log-processor/tests:/workspace/tests json-log-processor:latest bash -c "bash /workspace/solution/solve.sh && bash /workspace/tests/test.sh"
```

**Output:**
```
Filtered 3 ERROR entries from 10 total logs
Running JSON Log Processor Tests...
==================================
Running JSON Log Processor Tests...
==================================================
PASS: Output file exists
PASS: Output is valid JSON
PASS: All entries have level == 'ERROR'
PASS: Correct number of errors filtered (3)
==================================================
PASS: All tests passed
Successfully filtered 3 ERROR entries
Score: 1.0
==================================
All tests passed!
```

**Score: 1.0** ✅

### NOP Test (0.0)
```bash
$ docker run --rm -v ${PWD}/harbor_tasks/json-log-processor/tests:/workspace/tests json-log-processor:latest bash /workspace/tests/test.sh
```

**Expected Output (without solution):**
```
Running JSON Log Processor Tests...
==================================
FAIL: Output file not found at /app/output/errors.json
==================================
Tests failed!
```

**Score: 0.0** ✅ (Expected failure when no solution is provided)

## Task Details
- **Task ID**: json-log-processor
- **Difficulty**: Easy
- **Memory**: 512 MB
- **Storage**: 1024 MB
- **Timeout**: 300 seconds

## Files Added
- `harbor_tasks/json-log-processor/task.toml` - Task configuration
- `harbor_tasks/json-log-processor/instruction.md` - Task instructions
- `harbor_tasks/json-log-processor/environment/Dockerfile` - Docker environment setup
- `harbor_tasks/json-log-processor/environment/logs.json` - Sample log entries
- `harbor_tasks/json-log-processor/solution/solve.sh` - Solution script
- `harbor_tasks/json-log-processor/tests/test.sh` - Test runner
- `harbor_tasks/json-log-processor/tests/test_outputs.py` - Test suite

