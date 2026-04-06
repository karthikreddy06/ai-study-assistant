"""Quick start script for AI Study Assistant."""

import os
import sys
from pathlib import Path


def setup_environment():
    """Set up the project environment."""
    print("🚀 AI Study Assistant - Quick Setup")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("❌ Python 3.10+ is required. Please upgrade Python.")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Check if venv exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("\n📦 Creating virtual environment...")
        os.system(f"{sys.executable} -m venv venv")
        print("✓ Virtual environment created")
    else:
        print("✓ Virtual environment already exists")
    
    # Check if dependencies are installed
    print("\n📚 Installing dependencies...")
    venv_executable = venv_path / "Scripts" / "python" if os.name == "nt" else venv_path / "bin" / "python"
    os.system(f"{venv_executable} -m pip install -q -r requirements.txt")
    print("✓ Dependencies installed")
    
    # Check .env file
    env_file = Path(".env")
    if not env_file.exists():
        print("\n⚙️ Setting up environment file...")
        env_example = Path(".env.example")
        if env_example.exists():
            with open(env_example, "r") as f:
                content = f.read()
            with open(env_file, "w") as f:
                f.write(content)
            print("✓ Created .env file")
            print("⚠️ Please edit .env file and add your OpenAI API key")
        else:
            print("⚠️ .env.example not found")
    else:
        print("✓ .env file already exists")
    
    print("\n" + "=" * 60)
    print("✅ Setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file with your OpenAI API key")
    print("2. Activate virtual environment:")
    if os.name == "nt":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Run the application:")
    print("   python main.py")
    print("=" * 60)


if __name__ == "__main__":
    setup_environment()
