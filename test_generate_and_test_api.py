#!/usr/bin/env python3
"""
Test script to verify the generate-and-test API endpoint.

This script:
1. Starts the Flask API server
2. Sends the Travelhive XML to the /api/v1/translate/generate-and-test endpoint
3. Displays the results including test execution output
"""
import sys
import os
import json
import requests
import time
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

API_BASE_URL = "http://localhost:5000"


def start_api_server():
    """Start the Flask API server in background."""
    print("Starting API server...")
    process = subprocess.Popen(
        [sys.executable, "-m", "src.api.app"],
        cwd=str(PROJECT_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Wait for server to start
    time.sleep(3)
    return process


def stop_api_server(process):
    """Stop the API server."""
    process.terminate()
    process.wait(timeout=5)


def test_generate_and_test():
    """Test the generate-and-test endpoint."""
    xml_file = PROJECT_ROOT / 'data' / 'Travelhive_final_model.xml'

    if not xml_file.exists():
        print(f"Error: XML file not found: {xml_file}")
        return False

    print(f"\nReading XML file: {xml_file}")
    with open(xml_file, 'r') as f:
        xml_content = f.read()

    print(f"XML content size: {len(xml_content)} bytes")

    # Send request to generate-and-test endpoint
    print("\n--- Calling /api/v1/translate/generate-and-test ---")

    try:
        response = requests.post(
            f"{API_BASE_URL}/api/v1/translate/generate-and-test",
            json={
                'xml_content': xml_content,
                'network': 'hardhat'
            },
            timeout=600  # 10 minute timeout for test execution
        )
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API server. Is it running?")
        return False

    print(f"Response status: {response.status_code}")

    result = response.json()

    # Display results
    if response.status_code == 200:
        print("\n=== SUCCESS ===")
        print(f"Contracts generated: {len(result.get('contracts', {}))}")
        for name in result.get('contracts', {}).keys():
            print(f"  - {name}")

        print(f"\nTests generated: {len(result.get('tests', {}))}")
        for name in result.get('tests', {}).keys():
            print(f"  - {name}")

        test_result = result.get('test_result', {})
        if test_result:
            print(f"\n--- Test Results ---")
            print(f"Passed: {test_result.get('passed')}")
            print(f"Total tests: {test_result.get('total_tests')}")
            print(f"Passed tests: {test_result.get('passed_tests')}")
            print(f"Failed tests: {test_result.get('failed_tests')}")
            print(f"Duration: {test_result.get('duration_ms')}ms")

            if test_result.get('errors'):
                print(f"\nErrors:")
                for error in test_result.get('errors', []):
                    print(f"  - {error[:200]}...")

        artifacts = result.get('artifacts', {})
        if artifacts:
            print(f"\n--- Compiled Artifacts ---")
            for name, data in artifacts.items():
                print(f"  - {name}: {len(data.get('abi', []))} ABI entries")

        print(f"\nOutput directory: {result.get('output_dir')}")
        return True
    else:
        print("\n=== FAILED ===")
        print(f"Error: {result.get('error')}")
        if result.get('errors'):
            print("Details:")
            for error in result.get('errors', []):
                print(f"  - {error[:500]}")
        if result.get('traceback'):
            print(f"\nTraceback:\n{result.get('traceback')}")
        return False


def test_health_check():
    """Test health check endpoint."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/health")
        if response.status_code == 200:
            print("Health check: OK")
            return True
        else:
            print(f"Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Health check failed: Connection refused")
        return False


def main():
    """Main test function."""
    print("=" * 60)
    print("Testing Generate-and-Test API Pipeline")
    print("=" * 60)

    # Check if server is already running
    if test_health_check():
        print("\nAPI server is already running. Running tests...")
        success = test_generate_and_test()
    else:
        # Start server
        process = start_api_server()
        try:
            # Wait and check health
            for _ in range(10):
                if test_health_check():
                    break
                time.sleep(1)
            else:
                print("Failed to start API server")
                stop_api_server(process)
                return 1

            # Run test
            success = test_generate_and_test()
        finally:
            print("\nStopping API server...")
            stop_api_server(process)

    print("\n" + "=" * 60)
    if success:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    print("=" * 60)

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
