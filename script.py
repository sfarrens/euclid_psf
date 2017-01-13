#! /usr/bin/env Python
# -*- coding: utf-8 -*-

"""PSF INTERPOLATION TEST SCRIPT

This module ...

:Author: Samuel Farrens <samuel.farrens@gmail.com>

:Version: 1.0

:Date: 12/01/2017

"""

import numpy as np
import argparse as ap
from argparse import ArgumentDefaultsHelpFormatter as formatter
from src.metric import get_q


def get_opts():

    """Get script options

    This method sets the script options

    """

    # Set up argument parser

    parser = ap.ArgumentParser(add_help=False, usage='%(prog)s [options]',
                               description='PSF Metric Script',
                               formatter_class=formatter)
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Add arguments

    optional.add_argument('-h', '--help', action='help',
                          help='show this help message and exit')

    required.add_argument('-i', '--psf_int', dest='psf_int', required=True,
                          help='Interpolated PSF images file.')

    required.add_argument('-t', '--psf_true', dest='psf_true', required=True,
                          help='True PSF images file.')

    optional.add_argument('-e', '--target_ellip', dest='target_ellip',
                          default=2e-4, type=float, required=False,
                          help='Target PSF ellipticity stability.')

    optional.add_argument('-r', '--target_size', dest='target_size',
                          default=1e-3, type=float, required=False,
                          help='Target PSF size stability.')

    optional.add_argument('-n', '--eta', dest='eta',
                          default=2e3, type=int, required=False,
                          help='Normalisation parameter.')

    optional.add_argument('-s', '--sigma', dest='sigma',
                          default=1, type=int, required=False,
                          help='Dispersion due to pixel noise.')

    return parser.parse_args()


def run_script():

    psf_true = np.load(opts.psf_true)
    print 'True PSFs:', opts.psf_true

    psf_int = np.load(opts.psf_int)
    print 'Interpolated PSFs:', opts.psf_int

    print 'Q Value:', get_q(psf_int, psf_true, opts.target_ellip,
                            opts.target_size, opts.eta, opts.sigma)


def main():

    global opts
    opts = get_opts()
    run_script()


if __name__ == "__main__":
    main()
