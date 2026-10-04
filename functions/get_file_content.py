import os
def get_file_content(working_directory: str, file_path: str) -> str:
    try:

        abs_path_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path_wd, file_path))
        # Will be True or False
        valid_target_file = os.path.commonpath([abs_path_wd , target_file]) == abs_path_wd

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        MAX_CHARS = 10000

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    return file_content_string
            return file_content_string

        # After reading the first MAX_CHARS...
        
    except Exception as e:
        return f"Error: {e}"