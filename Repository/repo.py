import docker

client = docker.from_env()

def create_new_container(git_url:str, env: 'node' | 'pipenv'):
    raise NotImplemented()
    # TODO: Implement creating new container

def get_all_info():
    raise NotImplemented()
    # TODO: Implement getting all info

def get_status(id:str):
    raise NotImplemented()
    # TODO: Implement getting status

def turn_on(id:str):
    raise NotImplemented()
    # TODO: Implement turning on container

def turn_of(id:str):
    raise NotImplemented()
    # TODO: Implement turning off container

def set_always_on(id:str):
    raise NotImplemented()
    # TODO: Implement setting always on