import os
import pkgutil
import asyncio
import httpx
import json
import string
import hashlib
import re
import random

from bs4 import BeautifulSoup
from rich import print
from argparse import ArgumentParser
from importlib import import_module

__version__ = '0.1'
__author__  = 'CyberDefenseHub'

EMAIL_FORMAT = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

MODULES_DIR = './modules'

def import_submodules(package, recursive=True):
    '''Get all the holehe submodules'''
    results = {}

    if isinstance(package, str): package = import_module(package)

    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = import_module(full_name)
        if recursive and is_pkg: results.update(import_submodules(full_name))

    return results

def get_functions(modules):
    '''Transform the modules objects to functions'''
    websites = []

    for module in modules:
        if len(module.split('.')) > 2:
            _module = modules[module]
            site = module.split('.')[-1]
            websites.append(_module.__dict__[site])

    return websites

async def process_website(email, website, client, output):
    try:
        await website(email=email, client=client, out=output)
    except Exception as e:
        print(f'Error processing website: {website.__name__}, Error: {e}')
        pass

def print_result(output, email, args):
    for result in output:
        if result.get('rateLimit') and not args.onlyused:
            print(':warning: ' + result.get('domain'))
        elif result.get('error') and not args.onlyused:
            error_message = result.get('others', {}).get('errorMessage', '')
            print(f':warning: {result.get('domain')} Error message: {error_message}')
        elif not result.get('exists') and not args.onlyused:
            print(':x: ' + result.get('domain'))
        elif result.get('exists'):
            other_details = {
                key: value
                for key, value in {
                    'recovery_email': result.get('emailrecovery'),
                    'recovery_phone': result.get('phoneNumber'),
                    'other_details': result.get('others')
                }.items() if value is not None
            }
            
            if other_details:
                print(f':white_check_mark: {result.get('domain')} {other_details}')
            else:
                print(f':white_check_mark: {result.get('domain')}')

async def main():
    output = []
    print(random.randrange(int(1.5E12), int(2E12)))
    parser = ArgumentParser(description=f'Holehe-x v{__version__} by {__author__}')

    parser.add_argument('email', nargs='+', help='Target email address(es).')
    parser.add_argument('-U', '--only-used', default=False, required=False, action='store_true', dest='onlyused', help='Display only registered sites used by the target email address.')
    parser.add_argument('-NP', '--no-password-recovery', default=False, required=False, action='store_true', dest='nopasswordrecovery', help='Do not attempt password recovery on the websites (may alert the user via email).')
    parser.add_argument('-X', '--export', default=False, required=False, action='store_true', dest='output', help='Output results in JSON, CSV, or XML format.')
    parser.add_argument('-T', '--timeout', type=int , default=10, required=False, dest='timeout', help='Set the maximum timeout value for requests (default 10 seconds).')

    args  = parser.parse_args()
    email = args.email[0]

    async with httpx.AsyncClient(timeout=args.timeout) as client:
        modules = import_submodules('modules')
        websites = get_functions(modules)

        print(':globe_with_meridians: Checking {} on {} sites!'.format(email, len(websites)))

        # Inject dependencies into each module's namespace
        for website in websites:
            website.__globals__.update(
                {
                    'httpx': httpx, 
                    'ArgumentParser': ArgumentParser, 
                    'hashlib': hashlib, 
                    'json': json, 
                    'string': string, 
                    'BeautifulSoup': BeautifulSoup, 
                    're': re
                }
            )

        tasks = []
        for website in websites:
            tasks.append(process_website(email, website, client, output))
        
        await asyncio.gather(*tasks)

    print_result(output, email, args)

if __name__ == '__main__':
    asyncio.run(main())
