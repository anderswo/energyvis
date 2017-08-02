#!flask/bin/python
# -*- coding: utf-8 -*-

""" Script to run the application"""

import os
from app import app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print('Debug Mode: %s' % app.config['DEBUG'])
    app.run(host='0.0.0.0', port=port)
