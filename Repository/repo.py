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


def get_all_info() -> list[str]:
    containers = client.containers.list(all=True)
    result: list[str] = []

    for container in containers:
        result.append(f'Short ID: {container.short_id} Tag: {container.name} Status: {container.status}')

    return result


def get_status(container_id: str) -> str:
    return client.containers.get(container_id).status


class AlreadyRunning(Exception):
    pass


def turn_on(container_id: str) -> bool:
    container = client.containers.get(container_id)
    if container.status == 'running':
        raise AlreadyRunning()
    else:
        container.start()
        return True


class AlreadyDead(Exception):
    pass


def turn_off(container_id: str) -> bool:
    container = client.containers.get(container_id)
    if container.status != 'running':
        raise AlreadyDead
    else:
        container.kill()
        return True
