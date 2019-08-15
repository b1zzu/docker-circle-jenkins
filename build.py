#!/usr/bin/env python3

import argparse
import docker
import logging

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description='Build docker image combining multiple templates')
parser.add_argument(
    '-n',
    '--namespace',
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
args = parser.parse_args()

client = docker.from_env()

image = None
name = None
tag = []
for template in args.template:
    version = None
    if len(template.split(':')) != 1:
        (template, version) = template.split(':')

    from_image = image.id if image is not None else ''

    logging.info(' building \'{}\' with version \'{}\' from \'{}\''.format(
        template, version, from_image))

    (image, _) = client.images.build(
        path=template,
        buildargs={
            'FROM_IMAGE': from_image,
            template.upper() + '_VERSION': version
        })

    name = template
    tag.append('{}{}'.format(template, version or ''))

namespace = '{}/'.format(args.namespace) if args.namespace is not None else ''
tag = '{}{}:{}-{}'.format(namespace, name, args.version, '-'.join(tag))

logging.info(' tagging \'{}\''.format(tag))

image.tag(tag)

logging.info(' successfully builded \'{}\' '.format(tag))
