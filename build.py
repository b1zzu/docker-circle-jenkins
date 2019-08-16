#!/usr/bin/env python3

import argparse
import logging
import subprocess
import uuid
import yaml

logging.basicConfig(level=logging.INFO)


def parser():
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
        help='the template to build from templates.yml')
    parser.add_argument(
        'variant',
        metavar='VARIANT',
        help='the variant of the template to build')
    parser.add_argument(
        '-p',
        '--push',
        action='store_true',
        default=False,
        help='push image after building it'
    )
    return parser.parse_args()


arguments = parser()


def exec(*args):
    c = ' '.join(args)
    logging.info(' execute \'{}\''.format(c))
    subprocess.run(c, shell=True, check=True)


def templates():
    logging.info(' load templates from ./templates.yml')
    f = open('./templates.yml', 'r')
    t = yaml.load(f.read(), Loader=yaml.Loader)
    logging.info(' founded {} templates'.format(len(t)))
    return t


templates = templates()


def delete_image(image):
    exec('docker', 'rmi', image)


def tag_image(image, tag):
    exec('docker', 'tag', image, tag)


def push_image(image):
    exec('docker', 'push', image)


def get_info(template, variant):
    if template not in templates:
        logging.error(' the template {} does not exists'.format(template))
        exit(1)

    if variant not in templates[template]:
        logging.error(
            ' the variant {} does not exists in the template {}'.format(variant, template))
        exit(1)

    return templates[template][variant]


def build_variant_from(template, variant, info, from_image=''):
    logging.info(' start building variant {} {} from {}'.format(
        template, variant, from_image))

    name = template
    template = info.get('template', template)
    version = info.get('version', '')
    image = str(uuid.uuid4())

    exec('docker', 'build',
         '--build-arg', 'FROM_IMAGE={}'.format(from_image),
         '--build-arg', '{}_VERSION={}'.format(name.upper(), version),
         '--tag', image,
         './{}'.format(template))

    return image


def build_variant(template, variant):
    logging.info(' start building variant {} {}'.format(template, variant))

    info = get_info(template, variant)

    images = {}
    if 'from' in info:
        for from_template, from_variants in info['from'].items():
            for from_variant in from_variants:
                from_images = build_variant(
                    from_template,
                    from_variant)

                for from_tag, from_image in from_images.items():
                    image = build_variant_from(
                        template,
                        variant,
                        info,
                        from_image)
                    delete_image(from_image)
                    tag = '{}-{}{}'.format(from_tag, template, variant)
                    images[tag] = image
    else:
        image = build_variant_from(template, variant, info)
        tag = '{}{}'.format(template, variant)
        images[tag] = image

    return images


template = arguments.template

variant = arguments.variant

namespace = arguments.namespace
namespace = '{}/'.format(namespace) if namespace is not None else ''

version = arguments.version

images = build_variant(template, variant)
for tag, image in images.items():
    tag = '{}{}:{}-{}'.format(namespace, template, version, tag)
    tag_image(image, tag)
    delete_image(image)
    logging.info(' built image {}'.format(tag))

    if arguments.push:
        push_image(tag)
        logging.info(' successfully pushed image {}'.format(tag))
