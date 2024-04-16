#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""recognize package"""

from flask import Flask

app = Flask(__name__)

from app import routes
