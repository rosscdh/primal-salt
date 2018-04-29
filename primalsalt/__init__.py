from services import ConfigLoaderService

service = ConfigLoaderService(config_file='primal-config.yml')
CONFIG = service.load()
