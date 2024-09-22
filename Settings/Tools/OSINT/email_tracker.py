from Settings.Utils import *

print(banner)

try: 
    import importlib.util
    import concurrent.futures
    from tqdm import tqdm

except ImportError:
    module_error()

# Dictionary to store imported modules
imported_modules = {}

def import_crawlers_scripts(folder=f"{tool_path}Settings/Tools/OSINT/account_crawlers"):
    try: 
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":  # Ignore init files
                    file_path = os.path.join(root, file)

                    # Get the module name by stripping ".py" and converting to a module-friendly path
                    module_name = file_path.replace("/", ".").replace("\\", ".").replace(".py", "")
                    
                    # Load the module dynamically
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Store the module in the dictionary with the module name as key
                    imported_modules[module_name] = module

    except Exception as e:
        print(f"Error importing scripts: {e}")
        exit(1)

def crawler_function(email):
    """Call functions that have the same name as the file they are in in parallel"""

    results = {}

    def call_function(module_name, module):
        function_name = module_name.split('.')[-1]
        func = getattr(module, function_name, None)
        if func:
            try:
                res = func(email)
                return function_name, res
            except Exception as e:
                return function_name, f"An error occurred: {e}"
        return function_name, None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_module = {executor.submit(call_function, module_name, module): module_name for module_name, module in imported_modules.items()}

        with tqdm(total=len(future_to_module), desc="Processing", unit="module") as pbar:
            for future in concurrent.futures.as_completed(future_to_module):
                function_name, result = future.result()
                results[function_name] = result

                pbar.update(1)

    print(f"\n{message_start} Results: {reset}")
    for key, value in results.items():
        if value is not None:
            if value:
                print(f"{bright}{green} {key.capitalize()}: {reset_all} Account found")
            else:
                print(f"{bright}{red} {key.capitalize()}: {reset_all} No results")
        else:
            print(f"{bright}{red} {key.capitalize()}: {reset_all} An error occurred")


def main():
    print(f"""{red}
                                                                ========================================
                                                                |{green}             Email Tracker            {red}|
                                                                ========================================          
    {reset}""")

    # Import all the crawler scripts
    import_crawlers_scripts()
    while True:
        email = input(f"{message_start} Enter the email address you want to track (or Q to quit): {reset}")

        if email == "Q" or email == "q":
            return
        
        elif validate_email(email):
            break

    crawler_function(email)

    wait_user()

try:
    main()
except Exception as e:
    print_error(f"An error occurred: {e}")
    wait_user()