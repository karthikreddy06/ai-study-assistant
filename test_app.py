#!/usr/bin/env python
"""
Test script to demonstrate AI Study Assistant functionality
This runs the application with mock inputs to show the full workflow
"""

import subprocess
import sys
import os
from pathlib import Path

# Get the project directory
project_dir = Path(__file__).parent

def run_application():
    """Run the main application with test input"""
    print("=" * 80)
    print("AI STUDY ASSISTANT - TEST RUN")
    print("=" * 80)
    print("\nRunning application with test topic: 'Python Functions'\n")
    
    # Create a test input: topic + answers
    test_input = "Python Functions\nyes\n"  
    
    # Run the application
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=test_input,
        cwd=project_dir,
        capture_output=False,
        text=True,
        timeout=30
    )
    
    return result.returncode

if __name__ == "__main__":
    print("\n[TEST] Starting AI Study Assistant Test...\n")
    
    try:
        exit_code = run_application()
        print("\n" + "=" * 80)
        if exit_code == 0:
            print("✓ TEST PASSED: Application completed successfully")
        else:
            print(f"✗ TEST FAILED: Application exited with code {exit_code}")
        print("=" * 80)
        sys.exit(exit_code)
    except subprocess.TimeoutExpired:
        print("✗ TEST FAILED: Application timed out")
        sys.exit(1)
    except Exception as e:
        print(f"✗ TEST FAILED: {type(e).__name__}: {e}")
        sys.exit(1)
