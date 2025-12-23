# JSON Log Processor Task

## Objective
Filter JSON log entries by severity level and extract all entries with level "ERROR".

## Task Description
You are given a JSON file containing log entries. Each entry has a `level` field that indicates the severity level (e.g., "ERROR", "INFO", "WARNING"). Your task is to:

1. Read the input file from `/app/input/logs.json`
2. Filter all entries where `level == "ERROR"`
3. Write the filtered results to `/app/output/errors.json` as a JSON array
4. The output should be valid JSON format with proper indentation

## Input Format
The input file contains a JSON array of log entries. Each entry is an object with various fields, including a `level` field.

Example entry:
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "message": "Database connection failed",
  "service": "api-server"
}
```

## Output Format
The output file should be a JSON array containing only the entries with `level == "ERROR"`.

## Requirements
- Read from `/app/input/logs.json`
- Write to `/app/output/errors.json`
- Output must be valid JSON
- Only include entries where `level` field equals "ERROR" (case-sensitive)

## Testing
Run the test suite with:
```bash
bash /workspace/tests/test.sh
```

The tests will verify:
- Output file exists
- Output is valid JSON
- All entries have `level == "ERROR"`
- Correct number of entries were filtered

