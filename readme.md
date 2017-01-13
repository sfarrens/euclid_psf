# PSF Interpolation Tests

> Author: **Samuel Farrens**

> Year: **2017**

> Version: **1.0**

> Email: **[samuel.farrens@gmail.com](mailto:samuel.farrens@gmail.com)**

## Q Metric Script

The file `script.py` reads a stack of interpolated PSF images and a stack of true PSF images (both in numpy binary format) and outputs the Q value for the whole sample.

To execute the code run

```bash
$ ./script.py -i INTERPOLATED_PSF_FILE.npy -t TRUE_PSF_FILE.npy
```

This script will output the Q value to the terminal.

All of the script options can be displayed by running

```bash
$ ./script --help
```

### Q Metric

The metric used was derived from that of [Mandelbaum et al. (2015)](https://arxiv.org/pdf/1412.1825v2.pdf) by T. Kuntzer.

The default target values for the PSF ellipticity and size stabilities are **2e-4** and **1e-3** respectively, as decribed in the [Euclid Redbook](https://arxiv.org/abs/1110.3193).
