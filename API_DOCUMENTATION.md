# DAO Deployment Platform API Documentation

## Overview

The DAO Deployment Platform API provides endpoints for translating DAO-ML XML models into Solidity smart contracts, running tests, and deploying to blockchain networks.

## Base URL

```
http://localhost:5000/api/v1
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API server
python run_api.py

# Or with custom host/port
python run_api.py --host 0.0.0.0 --port 8080
```

## Endpoints

### Health & Status

#### `GET /api/v1/health`
Basic health check.

**Response:**
```json
{
  "status": "healthy",
  "service": "dao-deployment-platform"
}
```

#### `GET /api/v1/status`
Detailed system status including dependency checks.

**Response:**
```json
{
  "status": "healthy",
  "dependencies": {
    "node": {"available": true, "version": "v18.17.0"},
    "npm": {"available": true, "version": "9.6.7"},
    "hardhat": {"available": true, "version": "2.19.0"}
  },
  "config": {
    "max_concurrent_jobs": 5,
    "default_network": "localhost",
    "available_networks": ["localhost", "sepolia", "goerli", "mainnet"]
  }
}
```

#### `GET /api/v1/networks`
List available blockchain networks.

---

### Synchronous Translation

#### `POST /api/v1/translate/validate`
Validate DAO-ML XML without generating contracts.

**Request (JSON):**
```json
{
  "xml_content": "<?xml version=\"1.0\"?>..."
}
```

**Request (Form):**
```bash
curl -X POST -F "file=@dao.xml" http://localhost:5000/api/v1/translate/validate
```

**Response:**
```json
{
  "valid": true,
  "errors": []
}
```

#### `POST /api/v1/translate/model`
Generate internal model from XML and return as JSON.

**Request:**
```json
{
  "xml_content": "<?xml version=\"1.0\"?>..."
}
```

**Response:**
```json
{
  "model": {
    "daos": [...],
    "roles": [...],
    "committees": [...]
  }
}
```

#### `POST /api/v1/translate/contracts`
Generate Solidity contracts synchronously (without tests/deployment).

**Request:**
```json
{
  "xml_content": "<?xml version=\"1.0\"?>...",
  "generate_tests": true
}
```

**Response:**
```json
{
  "contracts": {
    "MyDAO.sol": "// SPDX-License-Identifier: MIT...",
    "MyDAOPermissionManager.sol": "..."
  },
  "tests": {
    "MyDAO.test.js": "const { ethers } = require('hardhat')..."
  },
  "contract_count": 3,
  "test_count": 1
}
```

---

### Asynchronous Jobs (Full Pipeline)

#### `POST /api/v1/jobs`
Create a new deployment job that executes the full pipeline.

**Request (JSON):**
```json
{
  "xml_content": "<?xml version=\"1.0\"?>...",
  "network": "localhost",
  "run_tests": true,
  "deploy": true,
  "deployer_private_key": "0x..."
}
```

**Request (Form):**
```bash
curl -X POST \
  -F "file=@dao.xml" \
  -F "network=localhost" \
  -F "run_tests=true" \
  -F "deploy=true" \
  http://localhost:5000/api/v1/jobs
```

**Response:**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "queued",
  "message": "Job created and queued for processing"
}
```

#### `GET /api/v1/jobs`
List all jobs.

**Query Parameters:**
- `limit`: Maximum jobs to return (default: 100)

**Response:**
```json
{
  "jobs": [...],
  "total": 5
}
```

#### `GET /api/v1/jobs/{job_id}`
Get job status and details.

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "completed",
  "created_at": "2024-01-15T10:30:00.000Z",
  "updated_at": "2024-01-15T10:32:15.000Z",
  "current_phase": null,
  "progress_percent": 100,
  "message": "Job completed successfully",
  "validation_errors": [],
  "generated_contracts": ["/output/abc123/contracts/MyDAO.sol"],
  "generated_tests": ["/output/abc123/test/MyDAO.test.js"],
  "test_result": {
    "passed": true,
    "total_tests": 15,
    "passed_tests": 15,
    "failed_tests": 0,
    "duration_ms": 2340
  },
  "deployment_result": {
    "success": true,
    "network": "localhost",
    "contracts": {
      "MyDAO": "0x5FbDB2315678afecb367f032d93F642f64180aa3"
    }
  },
  "frontend_manifest": {
    "network": "localhost",
    "chainId": 31337,
    "contracts": {...}
  }
}
```

#### `POST /api/v1/jobs/{job_id}/cancel`
Cancel a running job.

#### `GET /api/v1/jobs/{job_id}/contracts`
Get generated contract source code.

#### `GET /api/v1/jobs/{job_id}/tests`
Get generated test files.

#### `GET /api/v1/jobs/{job_id}/artifacts`
Get compiled artifacts (ABI, bytecode).

#### `GET /api/v1/jobs/{job_id}/manifest`
Get frontend deployment manifest with contract addresses and ABIs.

#### `GET /api/v1/jobs/{job_id}/download`
Download all job outputs as a ZIP file.

---

## Job Status Flow

```
QUEUED → VALIDATING → GENERATING → TESTING → DEPLOYING → COMPLETED
                 ↓           ↓          ↓           ↓
              FAILED      FAILED     FAILED      FAILED
```

## Job Phases

1. `input_validation` - Validating XML against schema
2. `contract_generation` - Generating Solidity contracts
3. `test_generation` - Setting up test environment
4. `test_execution` - Running Hardhat tests
5. `compilation` - Compiling contracts
6. `deployment` - Deploying to blockchain
7. `frontend_generation` - Creating frontend manifest

---

## Configuration Options

### Job Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `network` | string | `localhost` | Target blockchain network |
| `run_tests` | boolean | `true` | Run generated tests |
| `deploy` | boolean | `false` | Deploy contracts after tests pass |
| `deployer_private_key` | string | `""` | Private key for deployment |

### Available Networks

- `localhost` - Local Hardhat node (chainId: 31337)
- `sepolia` - Sepolia testnet (chainId: 11155111)
- `goerli` - Goerli testnet (chainId: 5)
- `mainnet` - Ethereum mainnet (chainId: 1)

---

## Error Responses

All errors follow this format:

```json
{
  "error": "Error type",
  "message": "Detailed error message",
  "errors": ["List of specific errors"]
}
```

### Common Status Codes

- `200` - Success
- `202` - Accepted (job created)
- `400` - Bad request (invalid input)
- `404` - Not found
- `500` - Internal server error

---

## Frontend Integration

After successful deployment, use the manifest to integrate with your frontend:

```javascript
// Fetch manifest
const response = await fetch(`/api/v1/jobs/${jobId}/manifest`);
const manifest = await response.json();

// Use in ethers.js
import { ethers } from 'ethers';

const provider = new ethers.JsonRpcProvider(manifest.network);
const daoContract = new ethers.Contract(
  manifest.contracts.MyDAO.address,
  manifest.contracts.MyDAO.abi,
  provider
);
```

---

## Production Deployment

```bash
# Set environment variables
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 'src.api.app:create_app()'
```

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm 8+
- Hardhat (installed automatically during test execution)
