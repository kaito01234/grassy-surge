#!/usr/bin/env python3

from flask_frozen import Freezer
from app import app
import os
import shutil

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

def clean_build_directory():
    if os.path.exists('build'):
        shutil.rmtree('build')

def build_static_site():
    print("Build started")
    
    clean_build_directory()
    
    freezer.freeze()
    
    print("Build completed")

if __name__ == '__main__':
    build_static_site()