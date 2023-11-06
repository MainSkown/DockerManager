import tempfile

import docker
import subprocess

client = docker.from_env()


def create_new_image(git_url: str, name: str):
    # Create directory and check if dockerfile exists
    temp_dir = tempfile.TemporaryDirectory()
    result = subprocess.run([f'./check_file.sh', git_url, temp_dir.name])
    if result.returncode == 1:
        try:
            client.images.build(path=f'{temp_dir.name}/{name}', tag=name)
            return_value = [True, 'OK']
        except Exception as exp:
            print(type(exp), exp.args)
            return_value = [False, 'Internal server error']
    else:
        return_value = [False, 'No Dockerfile']
    temp_dir.cleanup()
    return return_value


def get_all_info():
    raise NotImplemented()
    # TODO: Implement getting all info


def get_status(id: str):
    raise NotImplemented()
    # TODO: Implement getting status


def turn_on(id: str):
    raise NotImplemented()
    # TODO: Implement turning on container


def turn_of(id: str):
    raise NotImplemented()
    # TODO: Implement turning off container


def set_always_on(id: str):
    raise NotImplemented()
    # TODO: Implement setting always on
