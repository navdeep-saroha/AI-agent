import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([abs_path_wd , target_file]) == abs_path_wd

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        

    except Exception as e:
        return f"Error: {e}"
