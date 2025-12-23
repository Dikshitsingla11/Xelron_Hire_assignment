#!/usr/bin/env python3
import json
import os
import sys

def test_output_exists():
    """Test that the output file exists"""
    output_path = '/app/output/errors.json'
    if not os.path.exists(output_path):
        print(f"FAIL: Output file not found at {output_path}")
        return False
    print("PASS: Output file exists")
    return True

def test_valid_json():
    """Test that the output is valid JSON"""
    output_path = '/app/output/errors.json'
    try:
        with open(output_path, 'r') as f:
            data = json.load(f)
        print("PASS: Output is valid JSON")
        return True, data
    except json.JSONDecodeError as e:
        print(f"FAIL: Output is not valid JSON: {e}")
        return False, None

def test_all_errors():
    """Test that all entries have level == 'ERROR'"""
    output_path = '/app/output/errors.json'
    with open(output_path, 'r') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        print("FAIL: Output is not a JSON array")
        return False
    
    non_errors = [entry for entry in data if entry.get('level') != 'ERROR']
    if non_errors:
        print(f"FAIL: Found {len(non_errors)} entries that are not ERROR level")
        return False
    
    print("PASS: All entries have level == 'ERROR'")
    return True

def test_correct_count():
    """Test that the correct number of errors were filtered"""
    # Count errors in input
    input_path = '/app/input/logs.json'
    with open(input_path, 'r') as f:
        input_logs = json.load(f)
    
    expected_errors = len([entry for entry in input_logs if entry.get('level') == 'ERROR'])
    
    output_path = '/app/output/errors.json'
    with open(output_path, 'r') as f:
        output_logs = json.load(f)
    
    if len(output_logs) != expected_errors:
        print(f"FAIL: Expected {expected_errors} ERROR entries, got {len(output_logs)}")
        return False
    
    print(f"PASS: Correct number of errors filtered ({expected_errors})")
    return True

def main():
    print("Running JSON Log Processor Tests...")
    print("=" * 50)
    
    all_passed = True
    
    # Test 1: Output exists
    if not test_output_exists():
        all_passed = False
        sys.exit(1)
    
    # Test 2: Valid JSON
    valid, data = test_valid_json()
    if not valid:
        all_passed = False
        sys.exit(1)
    
    # Test 3: All entries are ERROR level
    if not test_all_errors():
        all_passed = False
        sys.exit(1)
    
    # Test 4: Correct count
    if not test_correct_count():
        all_passed = False
        sys.exit(1)
    
    print("=" * 50)
    if all_passed:
        print("PASS: All tests passed")
        # Count and display filtered errors
        output_path = '/app/output/errors.json'
        with open(output_path, 'r') as f:
            errors = json.load(f)
        print(f"Successfully filtered {len(errors)} ERROR entries")
        print("Score: 1.0")
        sys.exit(0)
    else:
        print("FAIL: Some tests failed")
        sys.exit(1)

if __name__ == '__main__':
    main()

