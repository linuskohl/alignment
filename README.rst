===========================
Alignment
===========================

Contains measurements for ordinal variables
  * Agreement
  * Berry Mielke
  * Blair Lacy
  * Consensus
  * IQV
  * Kvalseth
  * Leik
  * Mrq

Installation
------------

The easiest way to install the package is via ``easy_install`` or ``pip``::

    $ pip install alignment
    
Usage
-----
.. code-block:: python
   from alignment import consensus
 
   dist = [9,0,0,3]
   r = consensus(dist)



Copyright & License
-------------------

Copyright (c) 2019, `Linus Kohl <https://munichresearch.com/>`_. `GPLv3 License <LICENSE.md>`_.
