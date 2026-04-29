import subprocess
import os
import logging

# Ensure project root is in PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    filename=os.path.join(PROJECT_ROOT, "logs/pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_git_command(args, check=True, capture_output=False):
    """Run a git command with the given arguments."""
    cmd = ["git"] + args
    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        check=check,
        capture_output=capture_output,
        text=True
    )
    return result


def configure_git_user(name="CI/CD Pipeline", email="pipeline@example.com"):
    """Configure git user if not already set."""
    try:
        # Check if user name is set
        result = run_git_command(["config", "user.name"], check=False, capture_output=True)
        if not result.returncode == 0 or not result.stdout.strip():
            run_git_command(["config", "user.name", name])
            logging.info(f"Git user name set to: {name}")
        
        # Check if user email is set
        result = run_git_command(["config", "user.email"], check=False, capture_output=True)
        if not result.returncode == 0 or not result.stdout.strip():
            run_git_command(["config", "user.email", email])
            logging.info(f"Git user email set to: {email}")
            
    except Exception as e:
        logging.warning(f"Could not configure git user: {e}")


def check_git_status():
    """Check the current git status."""
    logging.info("Checking git status")
    result = run_git_command(["status"], capture_output=True)
    logging.info(f"Git status:\n{result.stdout}")
    return result.stdout


def git_add(files=None):
    """Add files to git staging. If files is None, add all files."""
    logging.info("Adding files to git staging")
    if files is None:
        run_git_command(["add", "."])
        logging.info("Added all files to staging")
    else:
        if isinstance(files, str):
            files = [files]
        for file in files:
            run_git_command(["add", file])
        logging.info(f"Added files to staging: {files}")


def git_commit(message="Automated commit from CI/CD pipeline"):
    """Commit staged changes with the given message."""
    logging.info(f"Committing changes with message: {message}")
    result = run_git_command(["commit", "-m", message])
    logging.info(f"Commit result: {result.stdout}")
    return result


def git_push(remote="origin", branch="main"):
    """Push commits to the remote repository."""
    logging.info(f"Pushing to {remote}/{branch}")
    result = run_git_command(["push", remote, branch])
    logging.info(f"Push result: {result.stdout}")
    return result


def git_pull(remote="origin", branch="main"):
    """Pull changes from the remote repository."""
    logging.info(f"Pulling from {remote}/{branch}")
    result = run_git_command(["pull", remote, branch])
    logging.info(f"Pull result: {result.stdout}")
    return result


def git_add_commit_push(message="Automated commit from CI/CD pipeline", files=None):
    """Convenience function to add, commit, and push in one go."""
    configure_git_user()
    check_git_status()
    git_add(files)
    git_commit(message)
    git_push()
    logging.info("Git add-commit-push completed successfully")


def is_git_repo():
    """Check if the current directory is a git repository."""
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )
    return result.returncode == 0 and result.stdout.strip() == "true"
