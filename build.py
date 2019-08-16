#!/usr/bin/env python3

import argparse
import logging
import subprocess
import uuid

versions = {
    'fedora': {
        '31': '31',
    },
    'openjdk8': {},
    'node': {
        '10': '10.16.2',
    },
    'gradle': {
        '4': '4.10.3',
    },
}


def exec(*args):
    cmd = ' '.join(args)
    logging.info(' execute \'{}\''.format(cmd))
    subprocess.run(cmd, shell=True, check=True)


logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description='Build docker image combining multiple templates')
parser.add_argument(
    '-n',
    '--namespace',
    default=None,
    help='namespace for the docker image')
parser.add_argument(
    '-v',
    '--version',
    default='alpha',
    help='version to add to the tag for the image')
parser.add_argument(
    'template',
    metavar='TEMPLATE',
    nargs='+',
    help='a list of templates to combine in the same order')
parser.add_argument(
    '-p',
    '--push',
    action='store_true',
    default=False,
    help='push image after building it'
)
args = parser.parse_args()

image = None
name = None
tag = []
for template in args.template:
    version = None
    if len(template.split(':')) != 1:
        (template, version) = template.split(':')

    if versions.get(template) is None:
        logging.error(' invalid template \'{}\''.format(template))
        exit(1)

    if version is not None and versions[template].get(version) is None:
        logging.error(
            ' invalid version \'{}\' for template \'{}\''.format(version, template))
        exit(1)

    from_image = image or ''

    logging.info(' building \'{}\' with version \'{}\' from \'{}\''.format(
        template, version, from_image))

    image = str(uuid.uuid4())
    exec('docker', 'build',
         '--build-arg', 'FROM_IMAGE={}'.format(from_image),
         '--build-arg', '{}_VERSION={}'.format(
             template.upper(), versions[template][version] if version is not None else ''),
         '--tag', image,
         './{}'.format(template))

    if from_image != '':
        exec('docker', 'rmi', from_image)

    name = template
    tag.append('{}{}'.format(template, version or ''))

namespace = '{}/'.format(args.namespace) if args.namespace is not None else ''
tag = '{}{}:{}-{}'.format(namespace, name, args.version, '-'.join(tag))

logging.info(' tagging \'{}\''.format(tag))

exec('docker', 'tag', image, tag)
exec('docker', 'rmi', image)

logging.info(' successfully builded \'{}\' '.format(tag))

if args.push:
    logging.info(' pushing image')
    exec('docker', 'push', tag)
    logging.info(' successfully pushed')
