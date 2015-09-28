# -*- coding: utf-8 -*-

import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s -- %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )
logger = logging.getLogger(__name__)
