import shutil

# Create a ZIP archive
# shutil.make_archive(
#     r'C:\Users\91808\Downloads\End-to-End-with-mlflow-dvc\research\chest-ctscan',
#     'zip',
#     r'C:\Users\91808\Downloads\End-to-End-with-mlflow-dvc\research'
# )

# Unpack the ZIP archive
shutil.unpack_archive(
    r'C:\Users\91808\Downloads\End-to-End-with-mlflow-dvc\research\chest-ctscan.zip',
    r'C:\Users\91808\Downloads\End-to-End-with-mlflow-dvc\config'
)
