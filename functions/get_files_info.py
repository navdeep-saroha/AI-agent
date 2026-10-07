import os
from openai.types.chat import ChatCompletionFunctionToolParam

schema_get_files_info: ChatCompletionFunctionToolParam = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path_wd, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path_wd , target_dir]) == abs_path_wd

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # return f'Success: "{directory}" is within the working directory'
    
        results = []
        for item in os.listdir(target_dir):
            
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            is_item_dir = os.path.isdir(item_path)

            results.append(f"- {item}: file_size={item_size} bytes, is_dir={is_item_dir}") 
        return "\n".join(results)


    except Exception as e:
        return f"Error: {e}"