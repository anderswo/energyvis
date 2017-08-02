#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Project configuration file"""

import os
import logging

#  get the absolute path of the directory to the config file
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration"""
    print('Initialize base configuration...')
    NAME = 'Base configuration'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    LOGGING_FORMAT = '%(asctime)s ' \
                     '%(name)s ' \
                     '%(processName)s:%(process)d ' \
                     '%(threadName)s:%(thread)d ' \
                     '%(levelname)s:%(message)s'
    LOGGING_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
    LOGGING_LOCATION = 'log'  # use app.log to log into the app folder
    LOGGING_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    """Configuration for development"""
    NAME = 'Development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite:///data/energy.db'
    LOGGING_LEVEL = logging.INFO


class TestingConfig(BaseConfig):
    NAME = 'Testing'
    DEBUG = False
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'
    LOGGING_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    NAME = 'Production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///energy.db'
    LOGGING_LEVEL = logging.INFO


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
    "default": "config.ProductionConfig"
}


def configure_app(app):
    # Set configuration (development, testing, production, etc.)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    # preload config from module
    app.config.from_object(config[config_name])
    # override config from a file if a config folder exists
    app.config.from_pyfile('config.cfg', silent=True)
    # log config loading
    print('Loaded configuration: %s' % config_name)
    app.logger.info('Loaded configuration: %s' % config_name)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
