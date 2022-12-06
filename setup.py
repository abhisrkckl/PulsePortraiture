#!/usr/bin/env python

from distutils.core import setup
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    scripts=[
        "PulsePortraiture/ppalign.py",
        "PulsePortraiture/ppgauss.py",
        "PulsePortraiture/ppspline.py",
        "PulsePortraiture/pptoas.py",
        "PulsePortraiture/ppzap.py",
    ],
)
