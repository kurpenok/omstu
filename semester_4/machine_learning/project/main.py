import sys

from streamlit.web.cli import main

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(main(prog_name="streamlit"))
