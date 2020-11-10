
========================
Maintainer documentation
========================

This document contains notes for developers and packagers. End users probably
want to read ``README.rst`` and the files in the ``doc`` directory instead.


PyPi Release
============

1. Make sure the repository is up-to date.
2. Ensure the version is incremented:
   - ``setup.py``  must be updated
   - ``doc/conf.py``  must be updated
   - ``CHANGES.txt``  must contain a summary of the changes
3. Make sure all changes are committed, including the version number changes.
4. Tag the sources with ``git tag -m 'vX.Y.Z' vX.Y.Z``.
5. Don't forget to ``git push``.
6. Temporarily modify the ``setup.cfg`` file to comment out the variables
   ``tag_build = dev`` and ``tag_date = true`` (do **not** commit this
   changes).
7. Usually it is a good idea to have a virtualenv to do all this:
   ``virtualenv venv; . venv/bin/activate``.
8. Make sure build dependencies are installed: ``pip install twine``.
9. Build the new release source distribution ``python setup.py sdist``.
10. Sign the created package: ``gpg --detach-sign -a
    dist/sphinxcontrib-aafig-X.Y.Z.tar.gz``
11. Upload using twine: ``twine upload
    dist/sphinxcontrib-aafig-X.Y.Z.tar.gz*``.

.. vim: set filetype=rst :
