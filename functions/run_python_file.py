import os
import subprocess
def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:   
        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([abs_path_wd , target_file]) == abs_path_wd
    
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python",target_file]
        if args:
            command.extend(args)
        
        result = subprocess.run(command, capture_output=True, timeout=30, text=True)
        out_str = ""
        if result.returncode != 0:
            out_str = f"Process exited with code {result.returncode}\n"
        if not result.stdout and not result.stderr:
            out_str += "No output produced"
        else:
            out_str += f"STDOUT: {result.stdout}\n"
            out_str += f"STDERR: {result.stderr}\n"
        return out_str

    except subprocess.TimeoutExpired as e:
        return "Error: Python file timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"
