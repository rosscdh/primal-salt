import os
import yaml
import shutil
from pathlib import Path

path = os.path.abspath(__file__)
cwd = os.path.dirname(path)


class ConfigLoaderService():
    def __init__(self, *args, **kwargs):
        self.config_file = Path(kwargs.get('config_file', 'primal.yml'))

        if kwargs.get('config_file', False) is False:
            self.config_paths = kwargs.get('config_paths', [cwd,
                                                            str(Path.home()),
                                                            '/etc/primalsalt'])
        else:
            self.config_paths = [str(self.config_file.parent)]

    def load(self):
        primal_config = None

        for dirname in self.config_paths:

            config_file = Path(os.path.join(dirname, self.config_file))
            if config_file.is_file():
                with open(config_file, 'r') as stream:
                    primal_config = yaml.load(stream)
                    break

        assert primal_config, '{config_file} must exist and be valid yaml at: {locations}'.format(config_file=self.config_file,
                                                                                                  locations=','.join(self.config_paths))
        return primal_config


class ConfigCreatorService():
    def __init__(self, path, *args, **kwargs):
        self.config_filename = kwargs.get('config_file', 'primal.yml')
        self.config_file = Path(os.path.join(path, self.config_filename))
        assert not self.config_file.exists(), 'There already appears to be file: {}'.format(self.config_file)

    def create(self):
        shutil.copyfile(os.path.join(cwd, 'example.primal.yml'), self.config_file)


class BuildFromConfigService():
    def __init__(self, config_file, *args, **kwargs):
        self.config = None
        self.config_file = Path(config_file)
        self.parent_directory = self.config_file.parent
        assert self.config_file.exists(), 'There does not appear to be a file: {}'.format(self.config_file)
        self._load()

    def _load(self):
        config_service = ConfigLoaderService(config_file=self.config_file)
        self.config = config_service.load()

    def build(self):
        salt = self.config.get('primal').get('salt')
        for directory in salt.keys():
            directory_path = os.path.join(self.parent_directory, directory)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
