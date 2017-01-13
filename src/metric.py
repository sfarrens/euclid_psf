# -*- coding: utf-8 -*-

"""PSF INTERPOLATION METRIC

This module contains methods and classes for assessing the quality of image
reconstructions.

:Author: Samuel Farrens <samuel.farrens@gmail.com>

:Version: 1.0

:Date: 12/01/2017

Notes
-----
Metric equation by Thibault Kuntzer <thibault.kuntzer@epfl.ch>

References
----------

.. [M2015] Mandelbaum et al., GREAT3 results I: systematic errors in shear
   estimation and the impact of real galaxy morphology, 2015, MNRAS, 450, 2963.
   [https://arxiv.org/pdf/1412.1825v2.pdf]

"""

import numpy as np
from shape import Ellipticity


def get_ellipticities(data):
    """Get ellipticity values

    This method calculates the values of e1, e2 and R^2 for each input image

    Parameters
    ----------
    data : np.ndarray
        Input data, 3D array of 2D images

    Returns
    -------
    np.ndarray [e1, e2, R^2] values for each image in the data array

    """

    instances = np.array([Ellipticity(image) for image in data])

    return np.array([[inst.e[0], inst.e[1], inst.r2] for inst in instances]).T


def get_q(psf_int, psf_true, e_target=2e-4, size_target=1e-3, eta=2e3,
          sigma2=1):
    """Get Q mertic value

    This method calculates the Q metric for a sample of interpolated PSF images
    when the true PSF image at the corresponding position is known

    Parameters
    ----------
    psf_int : np.ndarray
        Interpolated PSFs, 3D array of 2D images
    psf_true : np.ndarray
        True PSFs, 3D array of 2D images
    e_target : float, optional
        Target value for the PSF ellipticity stability (the default is '2e-4')
    size_target : float, optional
        Target value for the PSF size stability (the default is '1e-3')
    eta : float, optional
        Normalisation parameter (the default is '2e3')
    sigma2 : float, optional
        Dispersion due to pixel noise (the default is '1')

    Returns
    -------
    float Q metric value

    Notes
    -----
    The Q metric was derived from eq.8 in [M2015]_ and is calculated as
    follows:

    .. math::

        Q = \frac{\eta}{\sqrt{\sigma_{min}^2 + \frac{1}{m}\sum_{i=1}^m\left[
                        \left(\frac{e_{1, i}^{int}-e_{1, i}^{true}}
                        {\alpha}\right)^2 +
                        \left(\frac{e_{2, i}^{int}-e_{2, i}^{true}}
                        {\alpha}\right)^2 +
                        \left(\frac{(R_i^{int}-R_i^{true})}{<R^2>^{int}}
                        \beta\right)^2
                        \right]}}

    where :math:`\alpha = \sigma(e)` is target ellipticity stability and
    :math:`\beta = \sigma(R^2)/<R^2>` is the target size stability.

    """

    er_int = get_ellipticities(psf_int)
    er_true = get_ellipticities(psf_true)

    diff = er_int - er_true

    a, b = diff[:2] / e_target
    c = diff[2] / (size_target * np.mean(er_true[2]))
    # c = diff[2] / (size_target * np.mean(er_int[2]))

    return eta / np.sqrt(sigma2 + np.mean(a ** 2 + b ** 2 + c ** 2))
