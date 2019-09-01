===========================
Alignment
===========================

Contains measurements for ordinal variables
  * Agreement
  * Berry Mielke: *Indices of ordinal variation, 1992*
  * Blair & Lacy: *Measure of concentration, "l" squared, 2000*
  * Consensus: *Tastle & Wierman, A measure of ordinal dispersion*
  * IQV: *Index of qualitative variation*
  * Kvalseth: *Tarald O. Kvalseth, Measuring variation for nominal data*
  * Leik: *A Measure of Ordinal Consensus, Robert K. Leik*
  * MRQ: *Montalvo J.G., Reynal-Querol M.: Ethnic diversity and economic development.*

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
