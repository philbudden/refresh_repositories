import configparser
from configparser import ExtendedInterpolation


def get_config(path):
    """
    Return config variables
    :param path(String): path to config file
    :return configparser: user settings
    :return configparser: developer settings
    """

    config = configparser.ConfigParser(
        interpolation=ExtendedInterpolation())

    config.read(path)

    config_user = config['user_settings']
    config_dev = config['developer_settings']

    return config_user, config_dev
