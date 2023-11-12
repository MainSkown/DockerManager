import tempfile
from typing import Final

import docker
import docker.errors
import subprocess

client = docker.from_env()

path_to_bash: Final[str] = 'Repository/check_file.sh'


def create_new_container(git_url: str, name: str):
    # Create directory and check if dockerfile exists
    temp_dir = tempfile.TemporaryDirectory()

    # Clone git repository and check if dockerfile exists
    result = subprocess.run([path_to_bash, git_url, temp_dir.name])

    # If docker file exists:
    if result.returncode == 1:
        try:
            # Check if image exists
            try:
                client.images.get(name)

            # If not create new
            except docker.errors.ImageNotFound:
                client.images.build(path=f'{temp_dir.name}/{name}', tag=name)

            # Create container using downloaded image and run it
            client.containers.run(name, detach=True)

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
