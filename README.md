# CI/CD Automation with Git Deployment

A comprehensive CI/CD pipeline automation framework with git integration for automated testing, building, and deployment workflows.

## Project Overview

This project provides an automated CI/CD pipeline that orchestrates the complete software delivery lifecycle, including:
- Automated testing with pytest and unittest
- Dependency management and installation
- Build artifact generation
- Git-based version control integration
- Deployment automation
- Application monitoring

## Directory Structure

```
ci_cd_2-master/
├── index.py                # Entry point for running tests
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
├── TODO.md                 # Project tasks and checklist
├── topics.txt              # Project topics/keywords
├── notes.txt               # Project notes and documentation
├── app/                    # Application source code
│   ├── __init__.py
│   └── calculator.py       # Calculator utility module
├── build/                  # Build artifacts
│   └── calculator.py
├── logs/                   # Pipeline execution logs
└── pipeline/               # CI/CD pipeline modules
    ├── pipeline.py         # Main pipeline orchestrator
    ├── git_utils.py        # Git operations utilities
    ├── deploy.py           # Deployment functions
    └── monitor.py          # Monitoring and health checks
└── tests/                  # Test suites
    ├── test_pytest.py      # Pytest test cases
    └── test_unittest.py    # Unittest test cases
```

## Features

### Testing
- **Pytest**: Modern Python testing framework with detailed test output
- **Unittest**: Standard Python unit testing framework
- Run tests via `python index.py`

### Pipeline Management
- Automated dependency installation
- Test execution and reporting
- Build process automation
- Deployment coordination
- Centralized logging to `logs/pipeline.log`

### Git Integration
- Configure git user settings
- Check repository status
- Stage and commit changes
- Push/pull operations
- Automated deployment to remote repositories

### Monitoring
- Application health checks
- Pipeline status monitoring
- Performance tracking

## Installation

### Prerequisites
- Python 3.8 or higher
- Git installed and configured

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ci_cd_2-master
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Tests
```bash
python index.py
```

### Running Pipeline
```bash
python pipeline/pipeline.py
```

### Git Operations
Import and use git utilities:
```python
from pipeline.git_utils import configure_git_user, git_add, git_commit, git_push

configure_git_user()
git_add()
git_commit("Automated commit message")
git_push()
```

### Deployment
```bash
python pipeline/deploy.py
```

### Monitoring
```bash
python pipeline/monitor.py
```

## Dependencies

Key dependencies include:
- **pytest** - Testing framework
- **fabric** - Remote execution and deployment
- **paramiko** - SSH protocol implementation
- **cryptography** - Encryption utilities
- **bcrypt** - Password hashing
- **requests** - HTTP client

See `requirements.txt` for complete list.

## Configuration

- **Pytest Configuration**: See `pytest.ini` for test runner settings
- **Pipeline Logging**: Logs are stored in `logs/pipeline.log`
- **Git Configuration**: Use git utilities to configure user settings

## Project Tasks

- [x] Create git utility functions (`pipeline/git_utils.py`)
- [ ] Integrate git operations into main pipeline
- [ ] Verify deployment changes

### Git Utils Functions Implemented
- ✓ `configure_git_user()` - Configure git user if not set
- ✓ `check_git_status()` - Check git status
- ✓ `git_add()` - Add files to staging
- ✓ `git_commit()` - Commit changes with message
- ✓ `git_push()` - Push to remote
- ✓ `git_pull()` - Pull latest changes

## Logging

All pipeline activities are logged to `logs/pipeline.log` with timestamps and severity levels:
- DEBUG: Detailed diagnostic information
- INFO: Informational messages about pipeline steps
- WARNING: Warning messages for potential issues
- ERROR: Error messages for failures

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure nothing breaks
4. Commit changes with meaningful messages
5. Push to remote repository

## Troubleshooting

### Tests Failing
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify test files are in the `tests/` directory
- Check `logs/pipeline.log` for detailed error messages

### Git Operations Failing
- Ensure git is installed and configured globally
- Check repository permissions and authentication
- Verify remote repository URL is correct

### Deployment Issues
- Check system logs for errors
- Verify deployment target is accessible
- Ensure proper permissions for deployment

## License

[Add your license information here]

## Support

For issues or questions, please refer to the project documentation or contact the development team.
